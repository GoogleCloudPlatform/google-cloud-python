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

import asyncio
import http.client as http_client
import json
import os
import ssl
from unittest import mock

import pytest

from google.auth import exceptions
from google.auth.aio import credentials, transport
from google.auth.aio.transport import sessions
from google.auth.exceptions import TimeoutError

# This is the valid "workload" format the library expects
VALID_WORKLOAD_CONFIG = {
    "version": 1,
    "cert_configs": {
        "workload": {
            "cert_path": "/tmp/mock_cert.pem",
            "key_path": "/tmp/mock_key.pem",
        }
    },
}


class TestSessionsMtls:
    @pytest.mark.asyncio
    async def test_configure_mtls_channel(self):
        """
        Tests that the mTLS channel configures correctly when a
        valid workload config is mocked.
        """
        with (
            mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}),
            mock.patch("os.path.exists") as mock_exists,
            mock.patch(
                "builtins.open",
                mock.mock_open(read_data=json.dumps(VALID_WORKLOAD_CONFIG)),
            ),
            mock.patch(
                "google.auth.aio.transport.mtls.get_client_cert_and_key"
            ) as mock_helper,
            mock.patch(
                "google.auth.aio.transport.mtls.make_client_cert_ssl_context"
            ) as mock_make_context,
            mock.patch("aiohttp.TCPConnector") as mock_connector,
            mock.patch("aiohttp.ClientSession") as mock_session,
        ):
            mock_session.return_value.close = mock.AsyncMock()
            mock_exists.return_value = True
            mock_helper.return_value = (True, b"fake_cert_data", b"fake_key_data")

            mock_context = mock.Mock(spec=ssl.SSLContext)
            mock_make_context.return_value = mock_context

            mock_creds = mock.AsyncMock(spec=credentials.Credentials)
            session = sessions.AsyncAuthorizedSession(mock_creds)

            await session.configure_mtls_channel()

            assert session._is_mtls is True
            assert session._cached_cert == b"fake_cert_data"
            mock_make_context.assert_called_once_with(
                b"fake_cert_data", b"fake_key_data"
            )
            mock_connector.assert_called_once_with(ssl=mock_context)
            mock_session.assert_called_once_with(connector=mock_connector.return_value)
            await session.close()

    @pytest.mark.asyncio
    async def test_configure_mtls_channel_disabled(self):
        """
        Tests behavior when the config file does not exist.
        """
        with (
            mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}),
            mock.patch("os.path.exists") as mock_exists,
        ):
            mock_exists.return_value = False
            mock_creds = mock.AsyncMock(spec=credentials.Credentials)
            session = sessions.AsyncAuthorizedSession(mock_creds)
            await session.configure_mtls_channel()
            assert session._is_mtls is False
            await session.close()

    @pytest.mark.asyncio
    async def test_configure_mtls_channel_invalid_format(self):
        """
        Verifies that the MutualTLSChannelError is raised for bad formats.
        """
        with (
            mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}),
            mock.patch("os.path.exists") as mock_exists,
            mock.patch(
                "builtins.open", mock.mock_open(read_data='{"invalid": "format"}')
            ),
        ):
            mock_exists.return_value = True
            mock_creds = mock.AsyncMock(spec=credentials.Credentials)
            session = sessions.AsyncAuthorizedSession(mock_creds)

            with pytest.raises(exceptions.MutualTLSChannelError):
                await session.configure_mtls_channel()
            await session.close()

    @pytest.mark.asyncio
    async def test_configure_mtls_channel_invalid_fields(self):
        """If cert is missing expected keys, it should fail gracefully."""
        bad_config = {"version": 1, "cert_configs": {"workload": {}}}
        with (
            mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}),
            mock.patch("os.path.exists") as mock_exists,
            mock.patch(
                "builtins.open", mock.mock_open(read_data=json.dumps(bad_config))
            ),
        ):
            mock_exists.return_value = True
            mock_creds = mock.AsyncMock(spec=credentials.Credentials)
            session = sessions.AsyncAuthorizedSession(mock_creds)

            with pytest.raises(exceptions.MutualTLSChannelError):
                await session.configure_mtls_channel()
            await session.close()

    @pytest.mark.asyncio
    async def test_configure_mtls_channel_close_exception_does_not_abort(self):
        """Tests that an exception in old_auth_request.close() during eviction does not abort configuration."""
        with (
            mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}),
            mock.patch("os.path.exists", return_value=True),
            mock.patch(
                "builtins.open",
                mock.mock_open(read_data=json.dumps(VALID_WORKLOAD_CONFIG)),
            ),
            mock.patch(
                "google.auth.aio.transport.mtls.get_client_cert_and_key",
                return_value=(True, b"fake_cert_data", b"fake_key_data"),
            ),
            mock.patch(
                "google.auth.aio.transport.mtls.make_client_cert_ssl_context",
                return_value=mock.Mock(spec=ssl.SSLContext),
            ),
            mock.patch("aiohttp.TCPConnector"),
            mock.patch("aiohttp.ClientSession") as mock_session,
        ):
            mock_session.return_value.close = mock.AsyncMock()

            mock_creds = mock.AsyncMock(spec=credentials.Credentials)
            session = sessions.AsyncAuthorizedSession(mock_creds)

            # Pre-populate _old_auth_requests with failing transports to test eviction (maxlen >= 2)
            failing_req_1 = mock.AsyncMock()
            failing_req_1.close.side_effect = Exception("Close failure 1")
            failing_req_2 = mock.AsyncMock()
            failing_req_2.close.side_effect = Exception("Close failure 2")
            session._old_auth_requests.extend([failing_req_1, failing_req_2])

            await session.configure_mtls_channel()

            assert session._is_mtls is True
            assert session._cached_cert == b"fake_cert_data"
            await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_failure_raises_error(self):
        """Verifies that an error in configure_mtls_channel raises MutualTLSChannelError."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_auth_req = mock.AsyncMock()
        mock_resp = mock.Mock()
        mock_resp.status_code = http_client.UNAUTHORIZED
        mock_resp.close = mock.AsyncMock()
        mock_auth_req.return_value = mock_resp

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        new_cert = b"new_cert"
        new_key = b"new_key"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (new_cert, new_key, b"old_fp", b"new_fp")
            mock_conf.side_effect = Exception("Failed to reconfigure")

            with pytest.raises(exceptions.MutualTLSChannelError):
                await session.request("GET", "https://pubsub.mtls.googleapis.com/test")

            mock_check.assert_called_once()
            mock_conf.assert_called_once()
            mock_resp.close.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_check_params_fails(self):
        """Verifies that a failure during parameter checking falls back to credential refresh and retries."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"cached_cert"

        with mock.patch(
            "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
            new_callable=mock.AsyncMock,
            side_effect=exceptions.ClientCertError("check_params failed"),
        ) as mock_check_params:
            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )
            assert resp == mock_resp_200
            mock_check_params.assert_called_once()
            mock_creds.refresh.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_no_cert_rotation_when_cert_matches_and_mtls_enabled(self):
        """Verifies that if the fingerprint has not changed, reconfiguration is skipped and retry succeeds."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (
                b"new_cert",
                b"new_key",
                b"same_fp",
                b"same_fp",
            )

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp_200
            mock_check.assert_called_once()
            mock_conf.assert_not_called()
            mock_creds.refresh.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_success_and_retry(self):
        """Verifies successful cert rotation, channel reconfiguration, and request retry."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        new_cert = b"new_cert"
        new_key = b"new_key"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (new_cert, new_key, b"old_fp", b"new_fp")

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp_200
            mock_conf.assert_called_once()
            cb = (
                mock_conf.call_args.args[0]
                if mock_conf.call_args.args
                else mock_conf.call_args.kwargs["client_cert_callback"]
            )
            assert cb() == (new_cert, new_key)
            mock_creds.refresh.assert_called_once()
            assert mock_auth_req.call_count == 2
            mock_resp_401.close.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_lock_contention(self):
        """Verifies that concurrent requests serialize mTLS check and skip redundant checks."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401_1 = mock.Mock()
        mock_resp_401_1.status_code = http_client.UNAUTHORIZED
        mock_resp_401_1.close = mock.AsyncMock()

        mock_resp_401_2 = mock.Mock()
        mock_resp_401_2.status_code = http_client.UNAUTHORIZED
        mock_resp_401_2.close = mock.AsyncMock()

        mock_resp_200_1 = mock.Mock()
        mock_resp_200_1.status_code = http_client.OK
        mock_resp_200_1.close = mock.AsyncMock()

        mock_resp_200_2 = mock.Mock()
        mock_resp_200_2.status_code = http_client.OK
        mock_resp_200_2.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(
            side_effect=[
                mock_resp_401_1,
                mock_resp_401_2,
                mock_resp_200_1,
                mock_resp_200_2,
            ]
        )

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        async def slow_check(*args, **kwargs):
            await asyncio.sleep(0.05)
            return (b"new", b"new", b"old_fp", b"new_fp")

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                side_effect=slow_check,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            results = await asyncio.gather(
                session.request("GET", "https://pubsub.mtls.googleapis.com/test1"),
                session.request("GET", "https://pubsub.mtls.googleapis.com/test2"),
            )

            assert results == [mock_resp_200_1, mock_resp_200_2]
            assert mock_check.call_count == 1
            assert mock_conf.call_count == 1
            assert mock_creds.refresh.call_count == 1

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_lock_contention_no_cert_change(self):
        """Verifies lock contention when certificates have not changed."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401_1 = mock.Mock()
        mock_resp_401_1.status_code = http_client.UNAUTHORIZED
        mock_resp_401_1.close = mock.AsyncMock()

        mock_resp_401_2 = mock.Mock()
        mock_resp_401_2.status_code = http_client.UNAUTHORIZED
        mock_resp_401_2.close = mock.AsyncMock()

        mock_resp_200_1 = mock.Mock()
        mock_resp_200_1.status_code = http_client.OK
        mock_resp_200_1.close = mock.AsyncMock()

        mock_resp_200_2 = mock.Mock()
        mock_resp_200_2.status_code = http_client.OK
        mock_resp_200_2.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(
            side_effect=[
                mock_resp_401_1,
                mock_resp_401_2,
                mock_resp_200_1,
                mock_resp_200_2,
            ]
        )

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        async def slow_check(*args, **kwargs):
            await asyncio.sleep(0.05)
            return (b"new", b"new", b"same_fp", b"same_fp")

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                side_effect=slow_check,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            results = await asyncio.gather(
                session.request("GET", "https://pubsub.mtls.googleapis.com/test1"),
                session.request("GET", "https://pubsub.mtls.googleapis.com/test2"),
            )

            assert results == [mock_resp_200_1, mock_resp_200_2]
            assert mock_check.call_count == 1
            assert mock_conf.call_count == 0
            assert mock_creds.refresh.call_count == 1

        await session.close()

    @pytest.mark.asyncio
    async def test_psc_endpoint_triggers_cert_rotation(self):
        """Verifies that PSC endpoints (*.p.googleapis.com) are recognized as mTLS endpoints."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        new_cert = b"new_cert"
        new_key = b"new_key"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (new_cert, new_key, b"old_fp", b"new_fp")

            resp = await session.request("GET", "https://pubsub.p.googleapis.com/test")

            assert resp == mock_resp_200
            mock_check.assert_called_once()
            mock_conf.assert_called_once()
            cb = (
                mock_conf.call_args.args[0]
                if mock_conf.call_args.args
                else mock_conf.call_args.kwargs["client_cert_callback"]
            )
            assert cb() == (new_cert, new_key)

        await session.close()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "non_mtls_url",
        [
            "https://pubsub.googleapis.com/test",
            "https://my-service-xyz-uc.a.run.app/test",
        ],
    )
    async def test_non_mtls_url_bypasses_rotation(self, non_mtls_url):
        """Verifies that standard non-mTLS URLs bypass certificate rotation."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            resp = await session.request("GET", non_mtls_url)

            assert resp == mock_resp_200
            mock_check.assert_not_called()
            mock_conf.assert_not_called()
            mock_creds.refresh.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_skips_retry_for_streaming(self):
        """Verifies that streaming requests skip retry on 401 and return the response."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp = mock.Mock()
        mock_resp.status_code = http_client.UNAUTHORIZED
        mock_resp.close = mock.AsyncMock()
        mock_auth_req = mock.AsyncMock(return_value=mock_resp)

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        def data_gen():
            yield b"part1"
            yield b"part2"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (b"new", b"new", b"old_fp", b"new_fp")

            resp = await session.request(
                "POST", "https://pubsub.mtls.googleapis.com/test", data=data_gen()
            )

            assert resp == mock_resp
            mock_check.assert_called_once()
            mock_conf.assert_called_once()
            mock_creds.refresh.assert_called_once()
            assert mock_auth_req.call_count == 1
            mock_resp.close.assert_not_called()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_credential_refresh_fails(self):
        """Covers the except block for RefreshError when credentials fail to refresh."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(
            side_effect=exceptions.RefreshError("Refresh failed")
        )

        mock_resp = mock.Mock()
        mock_resp.status_code = http_client.UNAUTHORIZED
        mock_resp.close = mock.AsyncMock()
        mock_auth_req = mock.AsyncMock(return_value=mock_resp)

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ),
        ):
            mock_check.return_value = (b"new", b"new", b"old_fp", b"new_fp")

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp
            mock_creds.refresh.assert_called_once()
            mock_auth_req.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_max_retries_exceeded(self):
        """Covers the `if _auth_retry_count < 2:` max retry limit."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp = mock.Mock()
        mock_resp.status_code = http_client.UNAUTHORIZED
        mock_resp.close = mock.AsyncMock()
        mock_auth_req = mock.AsyncMock(return_value=mock_resp)

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ),
        ):
            mock_check.return_value = (b"new", b"new", b"old_fp", b"new_fp")

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp
            assert mock_auth_req.call_count == 3
            assert mock_check.call_count == 2
            assert mock_resp.close.call_count == 2

        await session.close()

    @pytest.mark.asyncio
    async def test_session_close_cleans_old_auth_requests(self):
        """Covers the loop in the `close()` method that drains `_old_auth_requests`."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock.AsyncMock()
        )

        mock_old_req_1 = mock.AsyncMock()
        mock_old_req_2 = mock.AsyncMock()
        mock_old_req_3_fails = mock.AsyncMock()
        mock_old_req_3_fails.close.side_effect = Exception("Close error")

        session._old_auth_requests.extend(
            [mock_old_req_1, mock_old_req_2, mock_old_req_3_fails]
        )

        await session.close()

        mock_old_req_1.close.assert_called_once()
        mock_old_req_2.close.assert_called_once()
        mock_old_req_3_fails.close.assert_called_once()
        assert len(session._old_auth_requests) == 0

    @pytest.mark.asyncio
    async def test_request_401_streaming_refreshes_creds_and_returns_open_response(
        self,
    ):
        """Verifies that streaming requests refresh credentials but return the unclosed response."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(return_value=mock_resp_401)
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )

        streaming_data = (chunk for chunk in [b"chunk1", b"chunk2"])
        response = await session.request(
            "POST", "https://example.com", data=streaming_data
        )

        assert response == mock_resp_401
        mock_creds.refresh.assert_awaited_once()
        mock_resp_401.close.assert_not_called()
        await session.close()

    @pytest.mark.asyncio
    async def test_request_401_closes_response_on_timeout_during_recovery(self):
        """Verifies that response is closed when auth_with_timeout times out during _recover_auth_state."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)

        async def slow_refresh(*args, **kwargs):
            await asyncio.sleep(10)

        mock_creds.refresh = mock.AsyncMock(side_effect=slow_refresh)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(return_value=mock_resp_401)
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )

        with pytest.raises(TimeoutError):
            await session.request("GET", "https://example.com", max_allowed_time=0.1)

        mock_resp_401.close.assert_awaited_once()
        await session.close()

    @pytest.mark.asyncio
    async def test_request_401_closes_response_on_cancellation(self):
        """Verifies that response is closed and CancelledError propagated if task is cancelled."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)

        refresh_started = asyncio.Event()

        async def cancel_on_refresh(*args, **kwargs):
            refresh_started.set()
            await asyncio.sleep(10)

        mock_creds.refresh = mock.AsyncMock(side_effect=cancel_on_refresh)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(return_value=mock_resp_401)
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )

        task = asyncio.create_task(session.request("GET", "https://example.com"))
        await refresh_started.wait()
        task.cancel()

        with pytest.raises(asyncio.CancelledError):
            await task

        mock_resp_401.close.assert_awaited_once()
        await session.close()

    @pytest.mark.asyncio
    async def test_request_401_concurrent_refreshes_are_deduplicated(self):
        """Verifies that concurrent 401s execute only one credentials.refresh call."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(
            side_effect=[
                mock_resp_401,
                mock_resp_401,
                mock_resp_200,
                mock_resp_200,
            ]
        )
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )

        refresh_count = 0

        async def slow_refresh(*args, **kwargs):
            nonlocal refresh_count
            refresh_count += 1
            await asyncio.sleep(0.05)

        mock_creds.refresh = mock.AsyncMock(side_effect=slow_refresh)

        results = await asyncio.gather(
            session.request("GET", "https://example.com/1"),
            session.request("GET", "https://example.com/2"),
        )

        assert all(r.status_code == 200 for r in results)
        assert refresh_count == 1
        await session.close()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "mtls_url",
        [
            "https://pubsub.mtls.googleapis.com/test",
            "https://my-service-123456.us-central1.mtls.run.app/test",
        ],
    )
    async def test_cert_rotation_with_completed_mtls_init_task(self, mtls_url):
        """
        Verifies that when _mtls_init_task is already completed, receiving a 401
        with rotated certificates properly resets _mtls_init_task and reconfigures mTLS.
        """
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        # 1. Pre-populate _mtls_init_task with an already completed task
        async def dummy_completed():
            return None

        initial_task = asyncio.create_task(dummy_completed())
        await initial_task
        assert initial_task.done()
        # 2. Mock 401 then 200 responses
        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()
        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()
        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"
        session._mtls_init_task = initial_task  # Pre-populate completed task
        new_cert = b"new_cert"
        new_key = b"new_key"
        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            mock_check.return_value = (new_cert, new_key, b"old_fp", b"new_fp")
            # Must use a hostname matching _mtls_helper.is_mtls_endpoint
            resp = await session.request("GET", mtls_url)
            assert resp == mock_resp_200
            mock_conf.assert_called_once()
            # Verify the previous completed task was cleared during rotation
            assert session._mtls_init_task is not initial_task
            mock_creds.refresh.assert_called_once()
            assert mock_auth_req.call_count == 2
        await session.close()

    @pytest.mark.asyncio
    async def test_401_retry_raises_timeout_before_refresh(self):
        """
        Tests that TimeoutError is raised if max_allowed_time expires before
        credentials.refresh can be executed following a 401 response.
        """
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_auth_request = mock.AsyncMock(spec=transport.Request)
        mock_resp_401 = mock.Mock(spec=transport.Response, status_code=401)
        current_time = 0.0

        # When the 401 request completes, advance time past max_allowed_time
        async def fake_auth_request(*args, **kwargs):
            nonlocal current_time
            current_time = 100.0  # Expire timeout before refresh starts
            return mock_resp_401

        mock_auth_request.side_effect = fake_auth_request
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_request
        )
        with mock.patch("time.monotonic", side_effect=lambda: current_time):
            with pytest.raises(exceptions.TimeoutError):
                await session.request(
                    "GET", "https://example.com", max_allowed_time=1.0
                )
        # Confirm credentials.refresh was never called
        mock_creds.refresh.assert_not_called()
        await session.close()

    @pytest.mark.asyncio
    async def test_401_retry_raises_timeout_before_subsequent_retry(self):
        """
        Tests that TimeoutError is raised if credentials.refresh succeeds on 401,
        but elapsed time exceeds max_allowed_time before the retried request can execute.
        """
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_auth_request = mock.AsyncMock(spec=transport.Request)
        mock_resp_401 = mock.Mock(spec=transport.Response, status_code=401)
        mock_auth_request.return_value = mock_resp_401
        current_time = 0.0

        # Allow initial request to proceed at t=0.0, but expire timeout during refresh
        async def fake_refresh(auth_request):
            nonlocal current_time
            current_time = 100.0  # Expire timeout during refresh before retry
            return None

        mock_creds.refresh = mock.AsyncMock(side_effect=fake_refresh)
        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_request
        )
        with mock.patch("time.monotonic", side_effect=lambda: current_time):
            with pytest.raises(exceptions.TimeoutError):
                await session.request(
                    "GET", "https://example.com", max_allowed_time=1.0
                )
        # Refresh succeeded once, but subsequent retry was stopped by timeout
        assert mock_creds.refresh.call_count == 1
        assert mock_auth_request.call_count == 1
        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_lock_contention_check_params_fails(self):
        """Verifies lock contention when certificate parameter check raises a handled exception."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401_1 = mock.Mock()
        mock_resp_401_1.status_code = http_client.UNAUTHORIZED
        mock_resp_401_1.close = mock.AsyncMock()

        mock_resp_401_2 = mock.Mock()
        mock_resp_401_2.status_code = http_client.UNAUTHORIZED
        mock_resp_401_2.close = mock.AsyncMock()

        mock_resp_200_1 = mock.Mock()
        mock_resp_200_1.status_code = http_client.OK
        mock_resp_200_1.close = mock.AsyncMock()

        mock_resp_200_2 = mock.Mock()
        mock_resp_200_2.status_code = http_client.OK
        mock_resp_200_2.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(
            side_effect=[
                mock_resp_401_1,
                mock_resp_401_2,
                mock_resp_200_1,
                mock_resp_200_2,
            ]
        )

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"cached_cert"

        async def slow_failing_check(*args, **kwargs):
            await asyncio.sleep(0.05)
            raise exceptions.ClientCertError("check_params failed")

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                side_effect=slow_failing_check,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            results = await asyncio.gather(
                session.request("GET", "https://pubsub.mtls.googleapis.com/test1"),
                session.request("GET", "https://pubsub.mtls.googleapis.com/test2"),
            )

            assert results == [mock_resp_200_1, mock_resp_200_2]
            assert mock_check.call_count == 1
            assert session._mtls_check_counter == 1
            assert mock_conf.call_count == 0
            assert mock_creds.refresh.call_count == 1

        await session.close()

    @pytest.mark.asyncio
    async def test_no_cert_rotation_when_client_cert_does_not_exist(self):
        """Verifies that if client certificate does not exist, reconfiguration is skipped with proper logging."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(return_value=None)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
            mock.patch.object(sessions._LOGGER, "info") as mock_logger_info,
        ):
            mock_check.return_value = (None, None, None, None)

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp_200
            mock_check.assert_called_once()
            mock_conf.assert_not_called()
            mock_creds.refresh.assert_called_once()
            mock_logger_info.assert_any_call(
                "Skipping reconfiguration of mTLS channel because the client"
                " certificate does not exist."
            )

        await session.close()

    @pytest.mark.asyncio
    async def test_request_cancellation_propagates_and_leaves_mtls_init_running(self):
        """Verifies that cancelling an in-flight request propagates CancelledError
        to the caller while asyncio.shield preserves self._mtls_init_task running
        in the background.
        """
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        session = sessions.AsyncAuthorizedSession(mock_creds)
        init_started = asyncio.Event()
        init_can_finish = asyncio.Event()

        async def slow_mtls_init():
            init_started.set()
            await init_can_finish.wait()
            session._is_mtls = True

        # Simulate an in-progress mTLS initialization task
        mtls_task = asyncio.create_task(slow_mtls_init())
        session._mtls_init_task = mtls_task
        # Launch an in-flight request that awaits the shielded mTLS task
        req_task = asyncio.create_task(session.request("GET", "https://example.com"))
        # Ensure the mTLS task has started and the request is waiting on it
        await init_started.wait()
        # Yield to event loop to guarantee session.request has reached await asyncio.shield(...)
        await asyncio.sleep(0)
        # Cancel the in-flight request
        req_task.cancel()
        # 1. Verify asyncio.CancelledError is propagated to the request caller
        with pytest.raises(asyncio.CancelledError):
            await req_task
        # 2. Verify self._mtls_init_task was NOT cancelled and is still running
        assert not session._mtls_init_task.cancelled()
        assert not session._mtls_init_task.done()
        # 3. Allow self._mtls_init_task to complete and verify it finishes cleanly
        init_can_finish.set()
        await session._mtls_init_task
        assert session._mtls_init_task.done()
        assert not session._mtls_init_task.cancelled()
        assert session._is_mtls is True
        await session.close()

    @pytest.mark.asyncio
    async def test_cert_rotation_credential_refresh_not_implemented_retries(self):
        """Validate credentials that raise NotImplementedError on refresh()
        still trigger a retry after mTLS reconfiguration, not return the 401."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(side_effect=NotImplementedError)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with mock.patch(
            "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
            new_callable=mock.AsyncMock,
        ) as mock_check:
            with mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf:
                mock_check.return_value = (
                    b"new_cert",
                    b"new_key",
                    b"old_fp",
                    b"new_fp",
                )

                resp = await session.request(
                    "GET", "https://pubsub.mtls.googleapis.com/test"
                )

                # Validate that the handler falls through to `return None`
                # on NotImplementedError in order to signal retry.
                assert resp == mock_resp_200
                mock_conf.assert_called_once()
                cb = (
                    mock_conf.call_args.args[0]
                    if mock_conf.call_args.args
                    else mock_conf.call_args.kwargs["client_cert_callback"]
                )
                assert cb() == (b"new_cert", b"new_key")
                mock_creds.refresh.assert_called_once_with(mock_auth_req)
                assert mock_auth_req.call_count == 2
                mock_resp_401.close.assert_called_once()

        await session.close()

    @pytest.mark.asyncio
    async def test_credential_refresh_not_implemented_no_retry_on_non_mtls(self):
        """Validate credentials raising NotImplementedError on refresh do NOT
        retry when the request is on a non-mTLS endpoint."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(side_effect=NotImplementedError)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(return_value=mock_resp_401)

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )

        resp = await session.request("GET", "https://pubsub.googleapis.com/test")

        assert resp == mock_resp_401
        assert mock_auth_req.call_count == 1
        await session.close()

    @pytest.mark.asyncio
    async def test_credential_refresh_not_implemented_no_retry_when_cert_not_rotated(
        self,
    ):
        """Validate credentials raising NotImplementedError on refresh do NOT
        retry when the mTLS certificate has not rotated."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(side_effect=NotImplementedError)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_auth_req = mock.AsyncMock(return_value=mock_resp_401)

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"current_cert"

        with mock.patch(
            "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
            new_callable=mock.AsyncMock,
        ) as mock_check:
            mock_check.return_value = (
                b"current_cert",
                b"current_key",
                b"same_fp",
                b"same_fp",
            )

            resp = await session.request(
                "GET", "https://pubsub.mtls.googleapis.com/test"
            )

            assert resp == mock_resp_401
            assert mock_auth_req.call_count == 1

        await session.close()

    @pytest.mark.asyncio
    async def test_credential_refresh_not_implemented_concurrent_rotation_retries(
        self,
    ):
        """Validate that concurrent requests hitting 401 during rotation both retry
        and succeed when credentials raise NotImplementedError."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.before_request = mock.AsyncMock(return_value=None)
        mock_creds.refresh = mock.AsyncMock(side_effect=NotImplementedError)

        mock_resp_401_a = mock.Mock(
            status_code=http_client.UNAUTHORIZED, close=mock.AsyncMock()
        )
        mock_resp_401_b = mock.Mock(
            status_code=http_client.UNAUTHORIZED, close=mock.AsyncMock()
        )
        mock_resp_200_a = mock.Mock(status_code=http_client.OK, close=mock.AsyncMock())
        mock_resp_200_b = mock.Mock(status_code=http_client.OK, close=mock.AsyncMock())

        mock_auth_req = mock.AsyncMock(
            side_effect=[
                mock_resp_401_a,
                mock_resp_401_b,
                mock_resp_200_a,
                mock_resp_200_b,
            ]
        )

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        with mock.patch(
            "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
            new_callable=mock.AsyncMock,
        ) as mock_check:
            with mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ):
                mock_check.return_value = (
                    b"new_cert",
                    b"new_key",
                    b"old_fp",
                    b"new_fp",
                )

                resps = await asyncio.gather(
                    session.request("GET", "https://pubsub.mtls.googleapis.com/test"),
                    session.request("GET", "https://pubsub.mtls.googleapis.com/test"),
                )
                assert resps == [mock_resp_200_a, mock_resp_200_b]
                assert mock_auth_req.call_count == 4

        await session.close()

    @pytest.mark.asyncio
    async def test_credential_refresh_not_implemented_no_retry_on_non_mtls_during_concurrent_rotation(
        self,
    ):
        """A non-mTLS request whose credentials raise NotImplementedError on
        refresh() must NOT retry, even when a concurrent mTLS rotation has
        advanced the session-wide reconfig counter. Guards against the race
        where the shared counter alone would signal a spurious retry."""
        mock_creds = mock.AsyncMock(spec=credentials.Credentials)
        mock_creds.refresh = mock.AsyncMock(side_effect=NotImplementedError)

        mock_resp_401 = mock.Mock()
        mock_resp_401.status_code = http_client.UNAUTHORIZED
        mock_resp_401.close = mock.AsyncMock()

        mock_resp_200 = mock.Mock()
        mock_resp_200.status_code = http_client.OK
        mock_resp_200.close = mock.AsyncMock()

        # If a retry were (incorrectly) triggered, the 200 would be returned.
        mock_auth_req = mock.AsyncMock(side_effect=[mock_resp_401, mock_resp_200])

        session = sessions.AsyncAuthorizedSession(
            mock_creds, auth_request=mock_auth_req
        )
        session._is_mtls = True
        session._cached_cert = b"old_cert"

        # Advance the session-wide counter after this request snapshots it (the
        # snapshot happens before before_request), simulating a concurrent mTLS
        # request that reconfigured mTLS while this one was in flight.
        async def advance_counter(*args, **kwargs):
            session._mtls_reconfig_counter += 1

        mock_creds.before_request = mock.AsyncMock(side_effect=advance_counter)

        with (
            mock.patch(
                "google.auth.aio.transport.mtls.check_parameters_for_unauthorized_response",
                new_callable=mock.AsyncMock,
            ) as mock_check,
            mock.patch.object(
                session, "configure_mtls_channel", new_callable=mock.AsyncMock
            ) as mock_conf,
        ):
            resp = await session.request("GET", "https://pubsub.googleapis.com/test")

            # The 401 is returned as-is; no retry, no cert-rotation machinery
            # for a non-mTLS endpoint.
            assert resp == mock_resp_401
            mock_check.assert_not_called()
            mock_conf.assert_not_called()
            mock_creds.refresh.assert_called_once_with(mock_auth_req)
            assert mock_auth_req.call_count == 1

        await session.close()
