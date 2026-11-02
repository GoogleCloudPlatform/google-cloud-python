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

import unittest
from unittest import mock

from google.cloud.spanner_v1.omni import opaque
from google.cloud.spanner_v1.omni.proto import authentication_pb2, login_pb2


class TestOpaqueCrypto(unittest.TestCase):
    def test_random_oracle_sha256(self):
        max_val = 1 << 63
        test_inputs = [b"key", b"key2", bytes([97, 97, 98, 99, 100, 101])]
        for inp in test_inputs:
            expected = opaque.random_oracle_sha256(inp, max_val)
            self.assertEqual(len(expected), 32)
            for _ in range(10):
                out = opaque.random_oracle_sha256(inp, max_val)
                self.assertEqual(out, expected)

    def test_random_oracle_sha256_large_domain_raises(self):
        max_val = 1 << 65500
        with self.assertRaises(ValueError) as cm:
            opaque.random_oracle_sha256(b"key", max_val)
        self.assertIn(
            "Domain bit length must not be greater than 65280", str(cm.exception)
        )

    def test_mac(self):
        tests = [
            (b"key", b"data"),
            (b"key", b"data2"),
            (
                bytes([97, 97, 98, 99, 100, 101]),
                bytes([102, 103, 104, 105, 106, 107]),
            ),
        ]
        for k, d in tests:
            m1 = opaque.mac(k, d)
            m2 = opaque.mac(k, d)
            self.assertEqual(m1, m2)
            self.assertEqual(len(m1), 32)

    def test_xor_bytes(self):
        tests = [
            (b"abc", b"def", False),
            (
                bytes([97, 97, 98, 99, 100, 101]),
                bytes([102, 103, 104, 105, 106, 107]),
                False,
            ),
            (
                bytes([97, 97, 98, 99, 100, 101]),
                bytes([0, 0, 0, 0, 0, 0]),
                False,
            ),
            (b"abc", b"defghi", True),
            (b"abcdefghi", b"jklmnop", True),
            (b"", b"", False),
        ]
        for a, b, want_err in tests:
            if want_err:
                with self.assertRaises(ValueError):
                    opaque.xor_bytes(a, b)
            else:
                xored = opaque.xor_bytes(a, b)
                self.assertEqual(len(xored), len(a))
                orig = opaque.xor_bytes(xored, b)
                self.assertEqual(orig, a)

    def test_stretch(self):
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=5,
                memory_usage=7 * 1024,
                parallelism=1,
                hash_size=32,
            )
        )
        long_input = bytes(range(256)) * 4

        tests = [
            (
                b"",
                bytes(
                    [
                        58,
                        42,
                        135,
                        162,
                        54,
                        231,
                        153,
                        103,
                        111,
                        241,
                        220,
                        39,
                        245,
                        158,
                        231,
                        5,
                        157,
                        108,
                        133,
                        178,
                        37,
                        97,
                        185,
                        220,
                        104,
                        13,
                        66,
                        147,
                        221,
                        19,
                        198,
                        9,
                    ]
                ),
            ),
            (
                b"input",
                bytes(
                    [
                        177,
                        173,
                        204,
                        142,
                        245,
                        214,
                        91,
                        164,
                        139,
                        85,
                        150,
                        101,
                        204,
                        187,
                        48,
                        176,
                        251,
                        7,
                        154,
                        247,
                        251,
                        35,
                        241,
                        135,
                        99,
                        117,
                        14,
                        121,
                        182,
                        124,
                        87,
                        46,
                    ]
                ),
            ),
            (
                bytes([97, 97, 98, 99, 100, 101]),
                bytes(
                    [
                        164,
                        94,
                        8,
                        109,
                        17,
                        19,
                        42,
                        55,
                        86,
                        44,
                        54,
                        89,
                        255,
                        148,
                        130,
                        248,
                        133,
                        4,
                        40,
                        24,
                        246,
                        27,
                        81,
                        56,
                        231,
                        137,
                        238,
                        30,
                        67,
                        159,
                        3,
                        157,
                    ]
                ),
            ),
            (
                long_input,
                bytes(
                    [
                        132,
                        52,
                        182,
                        135,
                        97,
                        18,
                        8,
                        254,
                        10,
                        1,
                        94,
                        98,
                        78,
                        193,
                        246,
                        160,
                        12,
                        209,
                        142,
                        253,
                        247,
                        115,
                        4,
                        149,
                        141,
                        2,
                        105,
                        159,
                        139,
                        94,
                        161,
                        116,
                    ]
                ),
            ),
        ]
        for inp, expected in tests:
            stretched = opaque.stretch(inp, params)
            self.assertEqual(len(stretched), 32)
            self.assertEqual(stretched, expected)

    def test_extract(self):
        long_input = bytes(range(256)) * 4
        tests = [
            (
                b"",
                bytes(
                    [
                        99,
                        252,
                        241,
                        111,
                        84,
                        209,
                        178,
                        181,
                        88,
                        96,
                        91,
                        194,
                        149,
                        79,
                        240,
                        143,
                        252,
                        68,
                        135,
                        177,
                        69,
                        144,
                        33,
                        115,
                        195,
                        224,
                        100,
                        31,
                        46,
                        160,
                        150,
                        41,
                    ]
                ),
            ),
            (
                b"input",
                bytes(
                    [
                        94,
                        113,
                        123,
                        114,
                        170,
                        250,
                        213,
                        241,
                        247,
                        203,
                        160,
                        141,
                        111,
                        233,
                        68,
                        240,
                        123,
                        33,
                        207,
                        139,
                        115,
                        44,
                        249,
                        217,
                        77,
                        34,
                        6,
                        254,
                        77,
                        75,
                        20,
                        99,
                    ]
                ),
            ),
            (
                bytes([97, 97, 98, 99, 100, 101]),
                bytes(
                    [
                        48,
                        112,
                        244,
                        9,
                        53,
                        2,
                        10,
                        147,
                        218,
                        132,
                        43,
                        198,
                        200,
                        101,
                        20,
                        3,
                        71,
                        158,
                        227,
                        3,
                        161,
                        15,
                        215,
                        112,
                        251,
                        195,
                        187,
                        96,
                        11,
                        203,
                        226,
                        210,
                    ]
                ),
            ),
            (
                long_input,
                bytes(
                    [
                        246,
                        148,
                        220,
                        16,
                        96,
                        62,
                        53,
                        189,
                        96,
                        83,
                        146,
                        84,
                        233,
                        183,
                        89,
                        12,
                        235,
                        31,
                        24,
                        113,
                        148,
                        25,
                        213,
                        33,
                        167,
                        78,
                        147,
                        162,
                        223,
                        115,
                        38,
                        117,
                    ]
                ),
            ),
        ]
        for inp, expected in tests:
            extracted = opaque.extract(inp)
            self.assertEqual(len(extracted), 32)
            self.assertEqual(extracted, expected)

    def test_derive_key_pair(self):
        tests = [
            (b"seed", b"info", b"seed", b"info", False),
            (b"seed2", b"info", b"seed2", b"info", False),
            (b"seed", b"info2", b"seed", b"info2", False),
            (b"seed", b"info2", b"different", b"info2", True),
            (b"seed", b"info2", b"seed", b"info1", True),
        ]
        for s1, i1, s2, i2, want_diff in tests:
            pub1, priv1 = opaque.derive_key_pair(s1, i1)
            pub2, priv2 = opaque.derive_key_pair(s2, i2)
            self.assertEqual(len(pub1), 33)
            self.assertEqual(len(priv1), 32)
            if want_diff:
                self.assertNotEqual(priv1, priv2)
                self.assertNotEqual(pub1, pub2)
            else:
                self.assertEqual(priv1, priv2)
                self.assertEqual(pub1, pub2)

    def test_diffie_hellman(self):
        tests = [
            (b"", b""),
            (b"server-seed", b"client-seed"),
            (b"server-seed2", b"client-seed2"),
            (b"no-need-to-be-the-same-length", b"im-a-shorter-seed"),
        ]
        for server_seed, client_seed in tests:
            server_pub, server_priv = opaque.derive_key_pair(
                server_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
            )
            client_pub, client_priv = opaque.derive_key_pair(
                client_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
            )

            server_shared = opaque.diffie_hellman(server_priv, client_pub)
            client_shared = opaque.diffie_hellman(client_priv, server_pub)
            self.assertEqual(server_shared, client_shared)

    def test_oprf_evaluate(self):
        username = "username"
        password = b"password1234"
        oprf_seed = opaque.nonce()
        seed = opaque.expand(oprf_seed, (username + "OprfKey").encode("utf-8"), 32)
        _, server_priv = opaque.derive_key_pair(seed, b"OPAQUE-DeriveKeyPair")

        blinded_element, blind_scalar = opaque.blind(password)

        # Server blind evaluation
        blinded_pt = opaque.unmarshal_compressed(blinded_element)
        evaluated_pt = opaque.point_mul(blinded_pt, int.from_bytes(server_priv, "big"))
        evaluated_element = opaque.marshal_compressed(evaluated_pt)

        # Client finalization
        oprf = opaque.finalize(blind_scalar, evaluated_element)

        # Direct evaluation
        h_pt = opaque.hash_to_curve_p256(password, opaque.LOGIN_DOMAIN_SEPARATION_TAG)
        prf_pt = opaque.point_mul(h_pt, int.from_bytes(server_priv, "big"))
        prf = opaque.marshal_compressed(prf_pt)

        self.assertEqual(oprf, prf)

    def test_authenticator_validation(self):
        valid_params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )

        with self.assertRaises(ValueError):
            opaque.UserAuthenticator("", b"pass", valid_params)

        with self.assertRaises(ValueError):
            opaque.UserAuthenticator("user", b"", valid_params)

        with self.assertRaises(ValueError):
            opaque.UserAuthenticator("user", b"pass", None)

        with self.assertRaises(ValueError):
            opaque.UserAuthenticator(
                "user",
                b"pass",
                authentication_pb2.HashParameters(),
            ).initial_request()

    def test_authenticator_state_errors(self):
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )
        auth = opaque.UserAuthenticator("user", "password", params)

        # Final before initial
        resp = login_pb2.LoginResponse(
            opaque_response=login_pb2.OpaqueLoginResponse(
                initial_response=login_pb2.InitialOpaqueLoginResponse()
            )
        )
        with self.assertRaises(ValueError):
            auth.final_request(resp)

        # First initial works
        req1 = auth.initial_request()
        self.assertEqual(req1.username, "user")
        self.assertTrue(req1.opaque_request.HasField("initial_request"))

        # Second initial fails
        with self.assertRaises(ValueError):
            auth.initial_request()

    def test_user_authenticator_clear_and_del(self):
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )
        auth = opaque.UserAuthenticator("user", "password", params)
        auth.initial_request()

        pw_ref = auth._password
        blind_ref = auth._blind
        priv_keyshare_ref = auth._client_private_keyshare

        # Test clear() zeroizes buffers and sets them to None
        auth.clear()
        self.assertIsNone(auth._password)
        self.assertIsNone(auth._blind)
        self.assertIsNone(auth._client_private_keyshare)
        if pw_ref is not None:
            self.assertEqual(pw_ref, bytearray(len(pw_ref)))
        if blind_ref is not None:
            self.assertEqual(blind_ref, bytearray(len(blind_ref)))
        if priv_keyshare_ref is not None:
            self.assertEqual(priv_keyshare_ref, bytearray(len(priv_keyshare_ref)))

        # Calling clear again is safe
        auth.clear()

        # Test __del__ calls clear
        auth2 = opaque.UserAuthenticator("user", "password", params)
        auth2.initial_request()
        pw_ref2 = auth2._password
        auth2.__del__()
        self.assertIsNone(auth2._password)
        if pw_ref2 is not None:
            self.assertEqual(pw_ref2, bytearray(len(pw_ref2)))

    def test_full_opaque_handshake_simulation(self):
        username = "alice"
        password = b"secret_password_123"

        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )

        # 1. Server setup user registration:
        # oprf_key
        oprf_seed = opaque.nonce()
        oprf_key_seed = opaque.expand(
            oprf_seed, (username + "OprfKey").encode("utf-8"), 32
        )
        _, oprf_priv = opaque.derive_key_pair(oprf_key_seed, b"OPAQUE-DeriveKeyPair")

        # Direct prf for enrollment
        h_pt = opaque.hash_to_curve_p256(password, opaque.LOGIN_DOMAIN_SEPARATION_TAG)
        prf_pt = opaque.point_mul(h_pt, int.from_bytes(oprf_priv, "big"))
        prf = opaque.marshal_compressed(prf_pt)

        stretched_oprf = opaque.stretch(prf, params)
        randomized_password = opaque.extract(opaque.concat(prf, stretched_oprf))

        # Server keypair
        server_key_seed = opaque.nonce()
        server_pub, server_priv = opaque.derive_key_pair(
            server_key_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )

        # Client keypair & envelope
        envelope_nonce = opaque.nonce()
        auth_key = opaque.expand(
            randomized_password, envelope_nonce + opaque.AUTH_KEY_INFO, 32
        )
        auth_tag = opaque.mac(
            auth_key, envelope_nonce + server_pub + username.encode("utf-8")
        )
        serialized_envelope = opaque.concat(server_pub, envelope_nonce, auth_tag)

        masking_key = opaque.expand(randomized_password, opaque.MASKING_KEY_INFO, 32)
        masking_nonce = opaque.nonce()
        credential_pad = opaque.expand(
            masking_key,
            opaque.concat(masking_nonce, b"CredentialResponsePad"),
            len(serialized_envelope),
        )
        masked_response = opaque.xor_bytes(serialized_envelope, credential_pad)

        # 2. Client starts login
        client_auth = opaque.UserAuthenticator(username, password, params)
        client_req1 = client_auth.initial_request()

        blinded_msg = client_req1.opaque_request.initial_request.blinded_message
        client_nonce = client_req1.opaque_request.initial_request.client_nonce
        client_pub_keyshare = (
            client_req1.opaque_request.initial_request.client_public_keyshare
        )

        # 3. Server processes initial request:
        blinded_pt = opaque.unmarshal_compressed(blinded_msg)
        eval_pt = opaque.point_mul(blinded_pt, int.from_bytes(oprf_priv, "big"))
        evaluated_msg = opaque.marshal_compressed(eval_pt)

        server_ephemeral_seed = opaque.nonce()
        server_ephemeral_pub, server_ephemeral_priv = opaque.derive_key_pair(
            server_ephemeral_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )
        server_login_nonce = opaque.nonce()

        # Server computes shared keys
        # Client recovered pub key from envelope
        seed = opaque.expand(
            randomized_password, envelope_nonce + opaque.PRIVATE_KEY_INFO, 32
        )
        client_pub, client_priv = opaque.derive_key_pair(
            seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )

        s_dh1 = opaque.diffie_hellman(server_ephemeral_priv, client_pub_keyshare)
        s_dh2 = opaque.diffie_hellman(server_priv, client_pub_keyshare)
        s_dh3 = opaque.diffie_hellman(server_ephemeral_priv, client_pub)
        s_ikm = opaque.concat(s_dh1, s_dh2, s_dh3)

        preamble = opaque.concat(
            b"OPAQUEv1-",
            username.encode("utf-8"),
            client_nonce,
            client_pub_keyshare,
            server_pub,
            evaluated_msg,
            server_login_nonce,
            server_ephemeral_pub,
        )

        s_km2, s_km3, _ = opaque.derive_shared_keys(s_ikm, preamble)
        server_mac = opaque.mac(s_km2, opaque.sha256_hash(preamble))

        server_resp1 = login_pb2.LoginResponse(
            opaque_response=login_pb2.OpaqueLoginResponse(
                initial_response=login_pb2.InitialOpaqueLoginResponse(
                    server_nonce=server_login_nonce,
                    server_public_keyshare=server_ephemeral_pub,
                    server_mac=server_mac,
                    evaluated_message=evaluated_msg,
                    masking_nonce=masking_nonce,
                    masked_response=masked_response,
                )
            )
        )

        # 4. Client completes handshake
        client_req2 = client_auth.final_request(server_resp1)
        client_mac = client_req2.opaque_request.final_request.client_mac

        # 5. Server verifies client MAC
        expected_client_mac = opaque.mac(
            s_km3,
            opaque.sha256_hash(opaque.concat(preamble, server_mac)),
        )
        self.assertEqual(client_mac, expected_client_mac)

    def test_final_request_invalid_masked_response_length(self):
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )
        auth = opaque.UserAuthenticator("user", "pass", params)
        auth.initial_request()

        resp = login_pb2.LoginResponse(
            opaque_response=login_pb2.OpaqueLoginResponse(
                initial_response=login_pb2.InitialOpaqueLoginResponse(
                    masked_response=b"invalid_len",
                )
            )
        )
        with self.assertRaises(ValueError) as cm:
            auth.final_request(resp)
        self.assertIn("Invalid masked response length", str(cm.exception))

    def test_clear(self):
        opaque._clear(None)
        b = bytearray(b"hello")
        opaque._clear(b)
        self.assertEqual(b, bytearray(5))

    def test_point_add_identity_and_inversion(self):
        pt = (opaque.GX, opaque.GY)
        self.assertEqual(opaque.point_add(None, pt), pt)
        self.assertEqual(opaque.point_add(pt, None), pt)
        self.assertIsNone(opaque.point_add(None, None))

        inv_pt = (opaque.GX, (opaque.P - opaque.GY) % opaque.P)
        self.assertIsNone(opaque.point_add(pt, inv_pt))

    def test_point_mul_infinity_and_zero(self):
        self.assertIsNone(opaque.point_mul(None, 5))
        self.assertIsNone(opaque.point_mul(opaque.G, 0))

    def test_marshal_compressed_none(self):
        with self.assertRaises(ValueError) as cm:
            opaque.marshal_compressed(None)
        self.assertIn("Point at infinity cannot be compressed", str(cm.exception))

    def test_unmarshal_compressed_errors(self):
        # Invalid length
        with self.assertRaises(ValueError) as cm:
            opaque.unmarshal_compressed(b"\x02" * 32)
        self.assertIn("Invalid compressed point length", str(cm.exception))

        # Invalid prefix
        with self.assertRaises(ValueError) as cm:
            opaque.unmarshal_compressed(b"\x04" + b"\x00" * 32)
        self.assertIn("Invalid compressed point prefix", str(cm.exception))

        # x coordinate exceeds P
        with self.assertRaises(ValueError) as cm:
            opaque.unmarshal_compressed(b"\x02" + (opaque.P + 1).to_bytes(32, "big"))
        self.assertIn("x coordinate exceeds field prime", str(cm.exception))

        # Point not on curve (find an x that produces a quadratic non-residue)
        for candidate_x in range(1, 100):
            rhs = (
                pow(candidate_x, 3, opaque.P) + opaque.A * candidate_x + opaque.B
            ) % opaque.P
            if pow(rhs, opaque.P_MINUS_1_OVER_2, opaque.P) != 1:
                with self.assertRaises(ValueError) as cm:
                    opaque.unmarshal_compressed(
                        b"\x02" + candidate_x.to_bytes(32, "big")
                    )
                self.assertIn("Point is not on curve", str(cm.exception))
                break

    def test_expand_message_xmd_oversize_dst(self):
        res = opaque.expand_message_xmd(b"msg", b"D" * 256, 32)
        self.assertEqual(len(res), 32)

    def test_expand_message_xmd_bytearray_input(self):
        res_ba = opaque.expand_message_xmd(bytearray(b"msg"), b"dst", 32)
        res_bytes = opaque.expand_message_xmd(b"msg", b"dst", 32)
        self.assertEqual(res_ba, res_bytes)
        self.assertEqual(len(res_ba), 32)

    def test_map_to_curve_sswu_zero(self):
        pt = opaque.map_to_curve_sswu(0)
        self.assertIsInstance(pt, tuple)
        self.assertEqual(len(pt), 2)

    def test_hash_to_curve_p256_infinity(self):
        from unittest import mock

        with mock.patch(
            "google.cloud.spanner_v1.omni.opaque.point_add", return_value=None
        ):
            with self.assertRaises(ValueError) as cm:
                opaque.hash_to_curve_p256(b"msg", b"dst")
            self.assertIn("Hash to curve produced point at infinity", str(cm.exception))

    def test_validate_hash_parameters_errors(self):
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(None)
        self.assertIn("hash_parameters cannot be None", str(cm.exception))

        # Missing argon2_id_parameters on proto message
        proto_empty = authentication_pb2.HashParameters()
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(proto_empty)
        self.assertIn(
            "hash_parameters must contain non-nil argon2_id_parameters",
            str(cm.exception),
        )

        # Missing argon2_id_parameters on non-proto object
        class EmptyParams:
            argon2_id_parameters = None

        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(EmptyParams())
        self.assertIn(
            "hash_parameters must contain non-nil argon2_id_parameters",
            str(cm.exception),
        )

        # Invalid memory usage
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=3,
                memory_usage=7,
                parallelism=4,
                hash_size=32,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params)
        self.assertIn("Invalid Argon2Id memory usage", str(cm.exception))

        # Invalid parallelism
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=3,
                memory_usage=64 * 1024,
                parallelism=0,
                hash_size=32,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params)
        self.assertIn("Invalid Argon2Id parallelism", str(cm.exception))

        # Invalid iteration count (0 and 11)
        params_low = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=0,
                memory_usage=64 * 1024,
                parallelism=4,
                hash_size=32,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params_low)
        self.assertIn("Invalid Argon2Id iteration count", str(cm.exception))

        params_high = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=11,
                memory_usage=64 * 1024,
                parallelism=4,
                hash_size=32,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params_high)
        self.assertIn("Invalid Argon2Id iteration count", str(cm.exception))

        # Valid non-proto hash parameters
        class ValidNonProtoParams:
            argon2_id_parameters = authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=3,
                memory_usage=64 * 1024,
                parallelism=4,
                hash_size=32,
            )

        opaque._validate_hash_parameters(ValidNonProtoParams())

        # Invalid hash_size (< 8 and > 512)
        params_low = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=3,
                memory_usage=64 * 1024,
                parallelism=4,
                hash_size=7,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params_low)
        self.assertIn("Invalid Argon2Id hash size", str(cm.exception))

        params_high = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=3,
                memory_usage=64 * 1024,
                parallelism=4,
                hash_size=513,
            )
        )
        with self.assertRaises(ValueError) as cm:
            opaque._validate_hash_parameters(params_high)
        self.assertIn("Invalid Argon2Id hash size", str(cm.exception))

    def test_random_oracle_sha256_large_max_val(self):
        max_val = (1 << 264) + 1
        res = opaque.random_oracle_sha256(b"seed", max_val)
        self.assertEqual(len(res), 34)

    def test_derive_key_pair_zero_priv(self):
        from unittest import mock

        with mock.patch(
            "google.cloud.spanner_v1.omni.opaque.random_oracle_sha256",
            return_value=b"\x00" * 32,
        ):
            pub, priv = opaque.derive_key_pair(b"seed", b"info")
            self.assertEqual(priv, (1).to_bytes(32, "big"))
            self.assertEqual(pub, opaque.marshal_compressed(opaque.G))

    def test_blind_and_finalize_edge_cases(self):
        with self.assertRaises(ValueError) as cm:
            opaque.blind(b"")
        self.assertIn("Password cannot be empty", str(cm.exception))

        # Explicit blind scalar
        explicit_scalar = (5).to_bytes(32, "big")
        blinded, returned_scalar = opaque.blind(b"pass", blind_scalar=explicit_scalar)
        self.assertEqual(returned_scalar, explicit_scalar)

        with self.assertRaises(ValueError) as cm:
            opaque.finalize(b"", b"evaluated")
        self.assertIn("Blind scalar cannot be empty", str(cm.exception))

    def test_recover_client_mismatched_auth_tag(self):
        with self.assertRaises(ValueError) as cm:
            opaque.recover_client(
                "user",
                b"\x01" * 32,
                b"\x02" * 32,
                b"\x00" * 32,
                opaque.marshal_compressed(opaque.G),
            )
        self.assertIn("Auth tag mismatch", str(cm.exception))

    def test_final_request_edge_cases(self):
        from unittest import mock

        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )
        auth = opaque.UserAuthenticator("user", "pass", params)
        auth.initial_request()

        with self.assertRaises(ValueError) as cm:
            auth.final_request(None)
        self.assertIn("initial_response cannot be None", str(cm.exception))

        empty_resp = login_pb2.LoginResponse()
        with self.assertRaises(ValueError) as cm:
            auth.final_request(empty_resp)
        self.assertIn("Expected initial opaque response from server", str(cm.exception))

        final_only_resp = login_pb2.LoginResponse()
        final_only_resp.opaque_response.final_response.SetInParent()
        with self.assertRaises(ValueError) as cm:
            auth.final_request(final_only_resp)
        self.assertIn("Expected initial opaque response from server", str(cm.exception))

        # Test blind when secrets.randbelow initially returns 0
        with mock.patch("secrets.randbelow", side_effect=[0, 7]):
            blinded_msg, blind_s = opaque.blind(b"testpass")
            self.assertEqual(blind_s, (7).to_bytes(32, "big"))

        # Test server MAC mismatch
        oprf_seed = opaque.nonce()
        oprf_key_seed = opaque.expand(oprf_seed, b"userOprfKey", 32)
        _, oprf_priv = opaque.derive_key_pair(oprf_key_seed, b"OPAQUE-DeriveKeyPair")
        h_pt = opaque.hash_to_curve_p256(b"pass", opaque.LOGIN_DOMAIN_SEPARATION_TAG)
        prf_pt = opaque.point_mul(h_pt, int.from_bytes(oprf_priv, "big"))
        prf = opaque.marshal_compressed(prf_pt)
        stretched_oprf = opaque.stretch(prf, params)
        randomized_password = opaque.extract(opaque.concat(prf, stretched_oprf))

        server_key_seed = opaque.nonce()
        server_pub, _ = opaque.derive_key_pair(
            server_key_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )
        envelope_nonce = opaque.nonce()
        auth_key = opaque.expand(
            randomized_password, envelope_nonce + opaque.AUTH_KEY_INFO, 32
        )
        auth_tag = opaque.mac(auth_key, envelope_nonce + server_pub + b"user")
        serialized_envelope = opaque.concat(server_pub, envelope_nonce, auth_tag)
        masking_key = opaque.expand(randomized_password, opaque.MASKING_KEY_INFO, 32)
        masking_nonce = opaque.nonce()
        credential_pad = opaque.expand(
            masking_key,
            opaque.concat(masking_nonce, b"CredentialResponsePad"),
            len(serialized_envelope),
        )
        masked_response = opaque.xor_bytes(serialized_envelope, credential_pad)

        blinded_pt = opaque.point_mul(h_pt, int.from_bytes(auth._blind, "big"))
        eval_pt = opaque.point_mul(blinded_pt, int.from_bytes(oprf_priv, "big"))
        server_ephemeral_pub, _ = opaque.derive_key_pair(
            opaque.nonce(), opaque.DIFFIE_HELLMAN_KEY_INFO
        )

        resp = login_pb2.LoginResponse(
            opaque_response=login_pb2.OpaqueLoginResponse(
                initial_response=login_pb2.InitialOpaqueLoginResponse(
                    server_nonce=opaque.nonce(),
                    server_public_keyshare=server_ephemeral_pub,
                    server_mac=b"bad_server_mac" * 2 + b"\x00" * 4,
                    evaluated_message=opaque.marshal_compressed(eval_pt),
                    masking_nonce=masking_nonce,
                    masked_response=masked_response,
                )
            )
        )

        # Test server MAC mismatch on auth (which matches auth._blind)
        with self.assertRaises(ValueError) as cm:
            auth.final_request(resp)
        self.assertIn("Server MAC mismatch", str(cm.exception))

        # Test xor_bytes returning invalid envelope length
        auth_short = opaque.UserAuthenticator("user", "pass", params)
        auth_short.initial_request()
        blinded_pt_short = opaque.point_mul(
            h_pt, int.from_bytes(auth_short._blind, "big")
        )
        eval_pt_short = opaque.point_mul(
            blinded_pt_short, int.from_bytes(oprf_priv, "big")
        )
        resp_short = login_pb2.LoginResponse(
            opaque_response=login_pb2.OpaqueLoginResponse(
                initial_response=login_pb2.InitialOpaqueLoginResponse(
                    server_nonce=opaque.nonce(),
                    server_public_keyshare=server_ephemeral_pub,
                    server_mac=b"bad_server_mac" * 2 + b"\x00" * 4,
                    evaluated_message=opaque.marshal_compressed(eval_pt_short),
                    masking_nonce=masking_nonce,
                    masked_response=masked_response,
                )
            )
        )
        with mock.patch(
            "google.cloud.spanner_v1.omni.opaque.xor_bytes", return_value=b"too_short"
        ):
            with self.assertRaises(ValueError) as cm:
                auth_short.final_request(resp_short)
            self.assertIn("Invalid serialized envelope length", str(cm.exception))

    def test_missing_cryptography_dependency(self):
        import importlib
        import sys

        with mock.patch.dict(
            sys.modules,
            {
                "cryptography": None,
                "cryptography.hazmat": None,
                "cryptography.hazmat.primitives": None,
                "cryptography.hazmat.primitives.kdf": None,
                "cryptography.hazmat.primitives.kdf.argon2": None,
                "cryptography.hazmat.primitives.kdf.hkdf": None,
            },
        ):
            with self.assertRaises(ImportError) as cm:
                importlib.reload(opaque)
            self.assertIn(
                "The 'cryptography' package is required for Spanner Omni authentication",
                str(cm.exception),
            )
            self.assertIn(
                "pip install google-cloud-spanner[omni]",
                str(cm.exception),
            )

        # Reload opaque cleanly
        importlib.reload(opaque)


if __name__ == "__main__":
    unittest.main()
