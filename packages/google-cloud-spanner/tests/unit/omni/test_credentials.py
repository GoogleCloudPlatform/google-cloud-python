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

import base64
import datetime
import unittest
from collections import namedtuple
from unittest import mock

import google.auth.exceptions
import grpc
from google.protobuf import timestamp_pb2

from google.cloud.spanner_v1.omni.credentials import SpannerOmniCredentials
from google.cloud.spanner_v1.omni.proto import login_pb2


class TestSpannerOmniCredentials(unittest.TestCase):
    def test_init_validation(self):
        with self.assertRaises(ValueError):
            SpannerOmniCredentials("", "password", "localhost:9010")
        with self.assertRaises(ValueError):
            SpannerOmniCredentials("user", "", "localhost:9010")
        with self.assertRaises(ValueError):
            SpannerOmniCredentials("user", "password", "")

    def test_target_scheme_parsing(self):
        creds_http = SpannerOmniCredentials("user", "pass", "http://localhost:9010")
        self.assertEqual(creds_http.target, "localhost:9010")
        self.assertTrue(creds_http.use_plain_text)

        creds_https = SpannerOmniCredentials("user", "pass", "https://localhost:9010")
        self.assertEqual(creds_https.target, "localhost:9010")
        self.assertFalse(creds_https.use_plain_text)

        creds_raw = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", use_plain_text=True
        )
        self.assertEqual(creds_raw.target, "localhost:9010")
        self.assertTrue(creds_raw.use_plain_text)

    def test_refresh_success(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", ca_certificate="/dummy/ca.pem"
        )

        mock_token_proto = login_pb2.AccessToken(
            username="user",
            expiration_time=timestamp_pb2.Timestamp(seconds=1700000000, nanos=0),
            signature=b"test_sig",
            key_id=42,
        )

        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_ca")),
            mock.patch("grpc.secure_channel") as mock_sec_channel,
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.refresh()

            self.assertIsNotNone(creds.token)
            # Verify base64 token decodes back to proto
            decoded_bytes = base64.b64decode(creds.token)
            parsed_token = login_pb2.AccessToken.FromString(decoded_bytes)
            self.assertEqual(parsed_token.username, "user")
            self.assertEqual(parsed_token.signature, b"test_sig")
            self.assertEqual(parsed_token.key_id, 42)
            self.assertEqual(
                creds.expiry,
                datetime.datetime.fromtimestamp(
                    1700000000, tz=datetime.timezone.utc
                ).replace(tzinfo=None),
            )
            mock_sec_channel.return_value.close.assert_called_once()

    def test_refresh_plaintext_channel(self):
        creds = SpannerOmniCredentials("user", "pass", "http://localhost:9010")
        mock_token_proto = login_pb2.AccessToken(username="user")

        with (
            mock.patch("grpc.insecure_channel") as mock_insec_channel,
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.refresh()

            mock_insec_channel.assert_called_once_with("localhost:9010")
            mock_insec_channel.return_value.close.assert_called_once()
            self.assertIsNotNone(creds.token)

    def test_refresh_missing_ca_certificate_raises(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        with self.assertRaises(google.auth.exceptions.RefreshError) as cm:
            creds.refresh()
        self.assertIn("requires ca_certificate to be set", str(cm.exception))

    def test_refresh_mtls_success(self):
        creds = SpannerOmniCredentials(
            "user",
            "pass",
            "localhost:9010",
            ca_certificate="/dummy/ca.pem",
            client_certificate="/dummy/cert.pem",
            client_key="/dummy/key.pem",
        )
        mock_token_proto = login_pb2.AccessToken(username="user")

        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_data")),
            mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds,
            mock.patch("grpc.secure_channel") as mock_sec_channel,
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.refresh()

            mock_ssl_creds.assert_called_once_with(
                root_certificates=b"dummy_data",
                private_key=b"dummy_data",
                certificate_chain=b"dummy_data",
            )
            mock_sec_channel.assert_called_once_with(
                "localhost:9010", mock_ssl_creds.return_value
            )
            self.assertIsNotNone(creds.token)

    def test_refresh_zero_expiration_time_falls_back_to_default_ttl(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", use_plain_text=True
        )
        mock_token_proto = login_pb2.AccessToken(username="user")
        mock_token_proto.expiration_time.seconds = 0
        mock_token_proto.expiration_time.nanos = 0

        with (
            mock.patch("grpc.insecure_channel"),
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.refresh()

            self.assertIsNotNone(creds.token)
            self.assertTrue(creds.valid)
            now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
            self.assertGreater(creds.expiry, now + datetime.timedelta(minutes=50))

    def test_refresh_nanos_only_expiration_time(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", use_plain_text=True
        )
        now_ts = datetime.datetime.now(datetime.timezone.utc).timestamp()
        mock_token_proto = login_pb2.AccessToken(username="user")
        mock_token_proto.expiration_time.seconds = int(now_ts) + 300
        mock_token_proto.expiration_time.nanos = 500000

        with (
            mock.patch("grpc.insecure_channel"),
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.refresh()

            self.assertIsNotNone(creds.token)
            self.assertTrue(creds.valid)
            now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
            self.assertGreater(creds.expiry, now + datetime.timedelta(minutes=4))

    def test_refresh_mtls_missing_key_raises(self):
        creds = SpannerOmniCredentials(
            "user",
            "pass",
            "localhost:9010",
            ca_certificate="/dummy/ca.pem",
            client_certificate="/dummy/cert.pem",
        )
        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_data")),
            self.assertRaises(google.auth.exceptions.RefreshError) as cm,
        ):
            creds.refresh()
        self.assertIn(
            "Both client_certificate and client_key must be provided",
            str(cm.exception),
        )

    def test_refresh_failure_wraps_in_refresh_error(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", ca_certificate="/dummy/ca.pem"
        )

        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_data")),
            mock.patch("grpc.secure_channel"),
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.side_effect = ValueError("Handshake failed")

            with self.assertRaises(google.auth.exceptions.RefreshError):
                creds.refresh()

    def test_refresh_grpc_error_is_reraised(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", ca_certificate="/dummy/ca.pem"
        )

        class CustomRpcError(grpc.RpcError):
            pass

        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_data")),
            mock.patch("grpc.secure_channel"),
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.side_effect = CustomRpcError("Service Unavailable")

            with self.assertRaises(CustomRpcError):
                creds.refresh()

    def test_refresh_skips_when_valid_inside_lock(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        creds.token = "existing_valid_token"
        creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
            tzinfo=None
        ) + datetime.timedelta(hours=1)

        with mock.patch(
            "google.cloud.spanner_v1.omni.credentials.LoginClient"
        ) as mock_login_client_cls:
            creds.refresh()
            mock_login_client_cls.assert_not_called()

    def test_apply_and_before_request(self):
        creds = SpannerOmniCredentials(
            "user", "pass", "localhost:9010", ca_certificate="/dummy/ca.pem"
        )
        headers = {}

        mock_token_proto = login_pb2.AccessToken(username="user")
        with (
            mock.patch("builtins.open", mock.mock_open(read_data=b"dummy_data")),
            mock.patch("grpc.secure_channel"),
            mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls,
        ):
            mock_client = mock_login_client_cls.return_value
            mock_client.login.return_value = mock_token_proto

            creds.before_request(None, "POST", "http://localhost", headers)

            self.assertIn("authorization", headers)
            self.assertTrue(headers["authorization"].startswith("Bearer "))

    def test_interceptor(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        creds.token = "sample_test_token"
        creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
            tzinfo=None
        ) + datetime.timedelta(hours=1)

        interceptor = creds.create_auth_interceptor()

        DummyCallDetails = namedtuple(
            "DummyCallDetails",
            ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
        )
        call_details = DummyCallDetails(
            method="/google.spanner.v1.Spanner/ExecuteSql",
            timeout=30.0,
            metadata=[("custom-header", "custom-val")],
            credentials=None,
            wait_for_ready=None,
        )

        def dummy_continuation(details, req):
            return details

        # Unary-Unary
        res = interceptor.intercept_unary_unary(dummy_continuation, call_details, "req")
        self.assertIn(("authorization", "Bearer sample_test_token"), res.metadata)
        self.assertIn(("custom-header", "custom-val"), res.metadata)

        # Unary-Stream
        res_us = interceptor.intercept_unary_stream(
            dummy_continuation, call_details, "req"
        )
        self.assertIn(("authorization", "Bearer sample_test_token"), res_us.metadata)

        # Stream-Unary
        res_su = interceptor.intercept_stream_unary(
            dummy_continuation, call_details, ["req"]
        )
        self.assertIn(("authorization", "Bearer sample_test_token"), res_su.metadata)

        # Stream-Stream
        res_ss = interceptor.intercept_stream_stream(
            dummy_continuation, call_details, ["req"]
        )
        self.assertIn(("authorization", "Bearer sample_test_token"), res_ss.metadata)

    def test_async_interceptor_attaches_bearer_token(self):
        import asyncio

        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        creds.token = "async_test_token"
        creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
            tzinfo=None
        ) + datetime.timedelta(hours=1)

        interceptors = creds.create_async_auth_interceptors()
        self.assertEqual(len(interceptors), 4)

        DummyCallDetails = namedtuple(
            "DummyCallDetails",
            ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
        )
        call_details = DummyCallDetails(
            method="/google.spanner.v1.Spanner/StreamingRead",
            timeout=30.0,
            metadata=[("custom-header", "custom-val")],
            credentials=None,
            wait_for_ready=None,
        )

        async def dummy_async_continuation(details, req):
            return details

        async def run_async_tests():
            # Unary-Unary
            res_uu = await interceptors[0].intercept_unary_unary(
                dummy_async_continuation, call_details, "req"
            )
            self.assertIn(("authorization", "Bearer async_test_token"), res_uu.metadata)
            self.assertIn(("custom-header", "custom-val"), res_uu.metadata)

            # Unary-Stream
            res_us = await interceptors[1].intercept_unary_stream(
                dummy_async_continuation, call_details, "req"
            )
            self.assertIn(("authorization", "Bearer async_test_token"), res_us.metadata)

            # Stream-Unary
            res_su = await interceptors[2].intercept_stream_unary(
                dummy_async_continuation, call_details, ["req"]
            )
            self.assertIn(("authorization", "Bearer async_test_token"), res_su.metadata)

            # Stream-Stream
            res_ss = await interceptors[3].intercept_stream_stream(
                dummy_async_continuation, call_details, ["req"]
            )
            self.assertIn(("authorization", "Bearer async_test_token"), res_ss.metadata)

        asyncio.run(run_async_tests())

    def test_async_interceptor_triggers_refresh_when_invalid(self):
        import asyncio

        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        interceptors = creds.create_async_auth_interceptors()

        DummyCallDetails = namedtuple(
            "DummyCallDetails",
            ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
        )
        call_details = DummyCallDetails(
            method="/google.spanner.v1.Spanner/ExecuteSql",
            timeout=30.0,
            metadata=[],
            credentials=None,
            wait_for_ready=None,
        )

        async def dummy_async_continuation(details, req):
            return details

        async def run_test():
            with mock.patch.object(creds, "refresh") as mock_refresh:

                def do_refresh():
                    creds.token = "refreshed_async_token"
                    creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
                        tzinfo=None
                    ) + datetime.timedelta(hours=1)

                mock_refresh.side_effect = do_refresh

                res = await interceptors[0].intercept_unary_unary(
                    dummy_async_continuation, call_details, "req"
                )
                mock_refresh.assert_called_once()
                self.assertIn(
                    ("authorization", "Bearer refreshed_async_token"), res.metadata
                )

        asyncio.run(run_test())

    def test_init_channel(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        mock_ssl = mock.Mock(spec=grpc.ChannelCredentials)
        creds.init_channel(
            use_plain_text=True,
            ca_certificate="ca.pem",
            client_certificate="client.pem",
            client_key="key.pem",
            ssl_credentials=mock_ssl,
        )
        self.assertTrue(creds.use_plain_text)
        self.assertEqual(creds.ca_certificate, "ca.pem")
        self.assertEqual(creds.client_certificate, "client.pem")
        self.assertEqual(creds.client_key, "key.pem")
        self.assertIs(creds.ssl_credentials, mock_ssl)

        # Also test with use_plain_text=False
        creds.init_channel(use_plain_text=False)
        self.assertFalse(creds.use_plain_text)

    def test_create_auth_interceptor_async_dispatch(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        interceptors = creds.create_auth_interceptor(is_async=True)
        self.assertIsInstance(interceptors, list)
        self.assertEqual(len(interceptors), 4)

        interceptors_alias = creds.create_async_auth_interceptor()
        self.assertIsInstance(interceptors_alias, list)
        self.assertEqual(len(interceptors_alias), 4)

    def test_sync_interceptor_triggers_refresh_when_invalid(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        interceptor = creds.create_auth_interceptor()

        DummyCallDetails = namedtuple(
            "DummyCallDetails",
            ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
        )
        call_details = DummyCallDetails(
            method="/google.spanner.v1.Spanner/ExecuteSql",
            timeout=30.0,
            metadata=[],
            credentials=None,
            wait_for_ready=None,
        )

        def dummy_continuation(details, req):
            return details

        with mock.patch.object(creds, "refresh") as mock_refresh:

            def do_refresh():
                creds.token = "refreshed_sync_token"
                creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
                    tzinfo=None
                ) + datetime.timedelta(hours=1)

            mock_refresh.side_effect = do_refresh

            res = interceptor.intercept_unary_unary(
                dummy_continuation, call_details, "req"
            )
            mock_refresh.assert_called_once()
            self.assertIn(
                ("authorization", "Bearer refreshed_sync_token"), res.metadata
            )

    def test_perform_refresh_token_with_ssl_credentials(self):
        mock_ssl = mock.Mock(spec=grpc.ChannelCredentials)
        creds = SpannerOmniCredentials(
            "user",
            "pass",
            "localhost:9010",
            ssl_credentials=mock_ssl,
        )
        with mock.patch("grpc.secure_channel") as mock_secure_channel:
            mock_channel = mock.MagicMock()
            mock_secure_channel.return_value = mock_channel
            with mock.patch(
                "google.cloud.spanner_v1.omni.credentials.LoginClient"
            ) as mock_login_client_cls:
                mock_client = mock.MagicMock()
                mock_login_client_cls.return_value = mock_client
                proto_token = login_pb2.AccessToken(
                    username="user", signature=b"secure_token"
                )
                mock_client.login.return_value = proto_token

                creds.refresh()

                mock_secure_channel.assert_called_once_with("localhost:9010", mock_ssl)
                self.assertTrue(creds.valid)
                self.assertIsNotNone(creds.token)
                mock_channel.close.assert_called_once()

    def test_before_request(self):
        creds = SpannerOmniCredentials("user", "pass", "localhost:9010")
        headers = {}

        with mock.patch.object(creds, "refresh") as mock_refresh:

            def do_refresh(request=None):
                creds.token = "refreshed_token"
                creds.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
                    tzinfo=None
                ) + datetime.timedelta(hours=1)

            mock_refresh.side_effect = do_refresh

            creds.before_request(None, "GET", "http://example.com", headers)
            mock_refresh.assert_called_once()
            self.assertEqual(headers["authorization"], "Bearer refreshed_token")

            # Call again when valid - refresh should not be called again
            mock_refresh.reset_mock()
            headers_2 = {}
            creds.before_request(None, "GET", "http://example.com", headers_2)
            mock_refresh.assert_not_called()
            self.assertEqual(headers_2["authorization"], "Bearer refreshed_token")


if __name__ == "__main__":
    unittest.main()
