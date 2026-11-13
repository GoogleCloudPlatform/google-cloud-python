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

import grpc
from google.protobuf import timestamp_pb2

from google.cloud.spanner_v1.omni import opaque
from google.cloud.spanner_v1.omni.login_client import LoginClient
from google.cloud.spanner_v1.omni.proto import authentication_pb2, login_pb2


class TestLoginClient(unittest.TestCase):
    def setUp(self):
        self.mock_channel = mock.MagicMock(spec=grpc.Channel)

    def test_login_empty_inputs(self):
        client = LoginClient(self.mock_channel)
        with self.assertRaises(ValueError):
            client.login("", "password")
        with self.assertRaises(ValueError):
            client.login("user", "")

    def test_login_successful_flow(self):
        username = "admin"
        password = b"secret123"

        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )

        # Precompute server artifacts
        oprf_seed = opaque.nonce()
        oprf_key_seed = opaque.expand(
            oprf_seed, (username + "OprfKey").encode("utf-8"), 32
        )
        _, oprf_priv = opaque.derive_key_pair(oprf_key_seed, b"OPAQUE-DeriveKeyPair")

        h_pt = opaque.hash_to_curve_p256(password, opaque.LOGIN_DOMAIN_SEPARATION_TAG)
        prf_pt = opaque.point_mul(h_pt, int.from_bytes(oprf_priv, "big"))
        prf = opaque.marshal_compressed(prf_pt)

        stretched_oprf = opaque.stretch(prf, params)
        randomized_password = opaque.extract(opaque.concat(prf, stretched_oprf))

        server_key_seed = opaque.nonce()
        server_pub, server_priv = opaque.derive_key_pair(
            server_key_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )

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

        expected_access_token = login_pb2.AccessToken(
            username=username,
            creation_time=timestamp_pb2.Timestamp(seconds=1000, nanos=0),
            expiration_time=timestamp_pb2.Timestamp(seconds=4600, nanos=0),
            signature=b"valid_signature",
            key_id=1,
            access_token_type=login_pb2.AccessToken.ACCESS_TOKEN_TYPE_API,
        )

        def mock_login_rpc(request_iterator, timeout=None):
            # Step 1: receive handshake request
            req1 = next(request_iterator)
            self.assertEqual(req1.username, username)
            self.assertTrue(req1.HasField("handshake_request"))

            # Return Step 1 response
            yield login_pb2.LoginResponse(
                handshake_response=authentication_pb2.PasswordAuthenticationHandshakeResponse(
                    password_authentication_protocol=authentication_pb2.PasswordAuthenticationProtocol.PASSWORD_AUTHENTICATION_PROTOCOL_OPAQUE,
                    hash_parameters=params,
                )
            )

            # Step 2: receive initial opaque request
            req2 = next(request_iterator)
            init_req = req2.opaque_request.initial_request
            blinded_msg = init_req.blinded_message
            client_nonce = init_req.client_nonce
            client_pub_keyshare = init_req.client_public_keyshare

            blinded_pt = opaque.unmarshal_compressed(blinded_msg)
            eval_pt = opaque.point_mul(blinded_pt, int.from_bytes(oprf_priv, "big"))
            evaluated_msg = opaque.marshal_compressed(eval_pt)

            server_ephemeral_pub, server_ephemeral_priv = opaque.derive_key_pair(
                opaque.nonce(), opaque.DIFFIE_HELLMAN_KEY_INFO
            )
            server_login_nonce = opaque.nonce()

            seed = opaque.expand(
                randomized_password, envelope_nonce + opaque.PRIVATE_KEY_INFO, 32
            )
            client_pub, _ = opaque.derive_key_pair(seed, opaque.DIFFIE_HELLMAN_KEY_INFO)

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

            s_km2, _, _ = opaque.derive_shared_keys(s_ikm, preamble)
            server_mac = opaque.mac(s_km2, opaque.sha256_hash(preamble))

            # Return Step 2 response
            yield login_pb2.LoginResponse(
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

            # Step 3: receive final opaque request
            req3 = next(request_iterator)
            self.assertTrue(req3.opaque_request.HasField("final_request"))

            # Return Step 3 response
            yield login_pb2.LoginResponse(access_token=expected_access_token)

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.side_effect = mock_login_rpc

            client = LoginClient(self.mock_channel)
            token = client.login(username, password)

            self.assertEqual(token.username, username)
            self.assertEqual(token.signature, b"valid_signature")
            self.assertEqual(token.key_id, 1)
            self.assertEqual(token.expiration_time.seconds, 4600)

    def test_login_unsupported_protocol(self):
        def mock_login_rpc(request_iterator, timeout=None):
            next(request_iterator)
            yield login_pb2.LoginResponse(
                handshake_response=authentication_pb2.PasswordAuthenticationHandshakeResponse(
                    password_authentication_protocol=authentication_pb2.PasswordAuthenticationProtocol.PASSWORD_AUTHENTICATION_PROTOCOL_UNSPECIFIED,
                )
            )

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.side_effect = mock_login_rpc

            client = LoginClient(self.mock_channel)
            with self.assertRaises(ValueError) as cm:
                client.login("user", "pass")
            self.assertIn(
                "Unsupported password authentication protocol", str(cm.exception)
            )

    def test_login_missing_handshake_response(self):
        def mock_login_rpc(request_iterator, timeout=None):
            next(request_iterator)
            yield login_pb2.LoginResponse()

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.side_effect = mock_login_rpc

            client = LoginClient(self.mock_channel)
            with self.assertRaises(ValueError) as cm:
                client.login("user", "pass")
            self.assertIn("Failed to receive handshake response", str(cm.exception))

    def test_login_missing_hash_parameters(self):
        def mock_login_rpc(request_iterator, timeout=None):
            next(request_iterator)
            yield login_pb2.LoginResponse(
                handshake_response=authentication_pb2.PasswordAuthenticationHandshakeResponse(
                    password_authentication_protocol=authentication_pb2.PasswordAuthenticationProtocol.PASSWORD_AUTHENTICATION_PROTOCOL_OPAQUE,
                )
            )

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.side_effect = mock_login_rpc

            client = LoginClient(self.mock_channel)
            with self.assertRaises(ValueError) as cm:
                client.login("user", "pass")
            self.assertIn(
                "Handshake response missing hash_parameters", str(cm.exception)
            )

    def test_login_missing_access_token_in_final_response(self):
        username = "test_user"
        password = "test_password"
        params = authentication_pb2.HashParameters(
            argon2_id_parameters=authentication_pb2.HashParameters.Argon2IdParameters(
                iteration_count=1,
                memory_usage=8,
                parallelism=1,
                hash_size=32,
            )
        )

        oprf_seed = opaque.nonce()
        oprf_key_seed = opaque.expand(
            oprf_seed, (username + "OprfKey").encode("utf-8"), 32
        )
        _, oprf_priv = opaque.derive_key_pair(oprf_key_seed, b"OPAQUE-DeriveKeyPair")
        h_pt = opaque.hash_to_curve_p256(
            password.encode("utf-8"), opaque.LOGIN_DOMAIN_SEPARATION_TAG
        )
        prf_pt = opaque.point_mul(h_pt, int.from_bytes(oprf_priv, "big"))
        prf = opaque.marshal_compressed(prf_pt)
        stretched_oprf = opaque.stretch(prf, params)
        randomized_password = opaque.extract(opaque.concat(prf, stretched_oprf))

        server_key_seed = opaque.nonce()
        server_pub, server_priv = opaque.derive_key_pair(
            server_key_seed, opaque.DIFFIE_HELLMAN_KEY_INFO
        )
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

        def mock_login_rpc(request_iterator, timeout=None):
            next(request_iterator)
            yield login_pb2.LoginResponse(
                handshake_response=authentication_pb2.PasswordAuthenticationHandshakeResponse(
                    password_authentication_protocol=authentication_pb2.PasswordAuthenticationProtocol.PASSWORD_AUTHENTICATION_PROTOCOL_OPAQUE,
                    hash_parameters=params,
                )
            )

            req2 = next(request_iterator)
            init_req = req2.opaque_request.initial_request
            blinded_msg = init_req.blinded_message
            client_nonce = init_req.client_nonce
            client_pub_keyshare = init_req.client_public_keyshare

            blinded_pt = opaque.unmarshal_compressed(blinded_msg)
            eval_pt = opaque.point_mul(blinded_pt, int.from_bytes(oprf_priv, "big"))
            evaluated_msg = opaque.marshal_compressed(eval_pt)

            server_ephemeral_pub, server_ephemeral_priv = opaque.derive_key_pair(
                opaque.nonce(), opaque.DIFFIE_HELLMAN_KEY_INFO
            )
            server_login_nonce = opaque.nonce()
            seed = opaque.expand(
                randomized_password, envelope_nonce + opaque.PRIVATE_KEY_INFO, 32
            )
            client_pub, _ = opaque.derive_key_pair(seed, opaque.DIFFIE_HELLMAN_KEY_INFO)

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
            s_km2, _, _ = opaque.derive_shared_keys(s_ikm, preamble)
            server_mac = opaque.mac(s_km2, opaque.sha256_hash(preamble))

            yield login_pb2.LoginResponse(
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

            next(request_iterator)
            # Response without access_token
            yield login_pb2.LoginResponse()

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.side_effect = mock_login_rpc

            client = LoginClient(self.mock_channel)
            with self.assertRaises(ValueError) as cm:
                client.login(username, password)
            self.assertIn(
                "Server failed to return an access token in final response",
                str(cm.exception),
            )

    def test_request_iterator_iter_and_stop(self):
        from google.cloud.spanner_v1.omni.login_client import _RequestIterator

        req_iterator = _RequestIterator()
        self.assertIs(iter(req_iterator), req_iterator)

        req = login_pb2.LoginRequest(username="u")
        req_iterator.send(req)
        self.assertEqual(next(req_iterator), req)

        req_iterator.close()
        with self.assertRaises(StopIteration):
            next(req_iterator)

    def test_request_iterator_close_idempotent(self):
        from google.cloud.spanner_v1.omni.login_client import _RequestIterator

        req_iterator = _RequestIterator()
        req_iterator.close()
        req_iterator.close()
        self.assertEqual(req_iterator._queue.qsize(), 1)
        self.assertIsNone(req_iterator._queue.get())
        self.assertTrue(req_iterator._queue.empty())

    def test_login_exception_cancels_call(self):
        mock_call = mock.MagicMock()
        mock_call.__next__.side_effect = RuntimeError("network error")

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.return_value = mock_call

            client = LoginClient(self.mock_channel)
            with self.assertRaises(RuntimeError):
                client.login("user", "pass")

            mock_call.cancel.assert_called_once()

    def test_login_premature_stream_closure(self):
        mock_call = mock.MagicMock()
        mock_call.__next__.side_effect = StopIteration

        with mock.patch(
            "google.cloud.spanner_v1.omni.proto.login_pb2_grpc.LoginServiceStub"
        ) as mock_stub_cls:
            mock_stub = mock_stub_cls.return_value
            mock_stub.Login.return_value = mock_call

            client = LoginClient(self.mock_channel)
            with self.assertRaises(ValueError) as cm:
                client.login("user", "pass")
            self.assertIn(
                "Server closed stream prematurely during handshake", str(cm.exception)
            )

    def test_grpc_servicers_and_helpers(self):
        import grpc

        from google.cloud.spanner_v1.omni.proto import login_pb2_grpc

        servicer = login_pb2_grpc.LoginServiceServicer()
        mock_context = mock.MagicMock()
        with self.assertRaises(NotImplementedError):
            servicer.Login(iter([]), mock_context)
        mock_context.set_code.assert_called_once_with(grpc.StatusCode.UNIMPLEMENTED)
        mock_context.set_details.assert_called_once_with("Method not implemented!")

        mock_server = mock.MagicMock()
        login_pb2_grpc.add_LoginServiceServicer_to_server(servicer, mock_server)
        mock_server.add_generic_rpc_handlers.assert_called_once()
        mock_server.add_registered_method_handlers.assert_called_once()

        with mock.patch("grpc.experimental.stream_stream") as mock_ss:
            login_pb2_grpc.LoginService.Login(iter([]), "target_host")
            mock_ss.assert_called_once()

    def test_grpc_version_mismatch_paths(self):
        import importlib

        try:
            importlib.import_module("grpc._utilities")
        except ImportError:
            pass

        # Test login_pb2_grpc version mismatch check
        with mock.patch(
            "grpc._utilities.first_version_is_lower", create=True, return_value=True
        ):
            with self.assertRaises(RuntimeError) as cm:
                importlib.reload(
                    importlib.import_module(
                        "google.cloud.spanner_v1.omni.proto.login_pb2_grpc"
                    )
                )
            self.assertIn("The grpc package installed is at version", str(cm.exception))

        with mock.patch(
            "grpc._utilities.first_version_is_lower", create=True, return_value=True
        ):
            with self.assertRaises(RuntimeError) as cm:
                importlib.reload(
                    importlib.import_module(
                        "google.cloud.spanner_v1.omni.proto.authentication_pb2_grpc"
                    )
                )
            self.assertIn("The grpc package installed is at version", str(cm.exception))

        # Test ImportError fallback when first_version_is_lower cannot be imported
        import sys

        orig_utilities = sys.modules.get("grpc._utilities")
        try:
            sys.modules["grpc._utilities"] = None
            importlib.reload(
                importlib.import_module(
                    "google.cloud.spanner_v1.omni.proto.login_pb2_grpc"
                )
            )
            importlib.reload(
                importlib.import_module(
                    "google.cloud.spanner_v1.omni.proto.authentication_pb2_grpc"
                )
            )
        finally:
            if orig_utilities is not None:
                sys.modules["grpc._utilities"] = orig_utilities
            else:
                sys.modules.pop("grpc._utilities", None)

        # Restore modules to standard state
        importlib.reload(
            importlib.import_module("google.cloud.spanner_v1.omni.proto.login_pb2_grpc")
        )
        importlib.reload(
            importlib.import_module(
                "google.cloud.spanner_v1.omni.proto.authentication_pb2_grpc"
            )
        )


if __name__ == "__main__":
    unittest.main()
