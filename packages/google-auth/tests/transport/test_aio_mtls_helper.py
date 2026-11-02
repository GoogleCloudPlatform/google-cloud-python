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

import os
import ssl
from unittest import mock

import pytest

from google.auth import exceptions
from google.auth.aio.transport import mtls

CERT_DATA = b"client-cert"
KEY_DATA = b"client-key"


class TestMTLS:
    @pytest.mark.asyncio
    async def test_make_client_cert_ssl_context_success(self):
        """Tests successful creation of an SSLContext with client certificates."""
        cert_bytes = b"cert_data"
        key_bytes = b"key_data"
        passphrase = b"password"

        mock_context = mock.Mock(spec=ssl.SSLContext)

        with mock.patch(
            "ssl.create_default_context", return_value=mock_context
        ) as mock_create:
            context = mtls.make_client_cert_ssl_context(
                cert_bytes, key_bytes, passphrase=passphrase
            )

            assert context == mock_context
            mock_create.assert_called_once_with(ssl.Purpose.SERVER_AUTH)

            # Verify load_cert_chain was called
            assert mock_context.load_cert_chain.called
            kwargs = mock_context.load_cert_chain.call_args.kwargs
            assert "certfile" in kwargs
            assert "keyfile" in kwargs
            assert kwargs["password"] == passphrase

            assert not os.path.exists(kwargs["certfile"])
            assert not os.path.exists(kwargs["keyfile"])

    @pytest.mark.asyncio
    async def test_make_client_cert_ssl_context_success_no_passphrase(self):
        """Tests successful creation of an SSLContext with no passphrase."""
        cert_bytes = b"cert_data"
        key_bytes = b"key_data"

        mock_context = mock.Mock(spec=ssl.SSLContext)

        with mock.patch(
            "ssl.create_default_context", return_value=mock_context
        ) as mock_create:
            context = mtls.make_client_cert_ssl_context(
                cert_bytes, key_bytes, passphrase=None
            )

            assert context == mock_context
            mock_create.assert_called_once_with(ssl.Purpose.SERVER_AUTH)
            kwargs = mock_context.load_cert_chain.call_args.kwargs
            assert kwargs["password"] is None

    @pytest.mark.asyncio
    async def test_make_client_cert_ssl_context_error(self):
        """Verifies that TransportError is raised when SSL loading fails."""
        cert_bytes = b"cert_data"
        key_bytes = b"key_data"

        mock_context = mock.Mock(spec=ssl.SSLContext)
        # Mocking an SSLError to trigger the exception handler in make_client_cert_ssl_context
        mock_context.load_cert_chain.side_effect = ssl.SSLError("Mock SSL Error")

        with mock.patch("ssl.create_default_context", return_value=mock_context):
            with pytest.raises(exceptions.TransportError) as exc_info:
                mtls.make_client_cert_ssl_context(cert_bytes, key_bytes)

            assert "Failed to load client certificate" in str(exc_info.value)
            assert isinstance(exc_info.value.__cause__, ssl.SSLError)

    @pytest.mark.asyncio
    @mock.patch(
        "google.auth.transport.mtls.has_default_client_cert_source", return_value=False
    )
    async def test_default_client_cert_source_not_found(self, mock_has_default):
        """Tests that a MutualTLSChannelError is raised if no cert source exists."""
        with pytest.raises(exceptions.MutualTLSChannelError, match="doesn't exist"):
            mtls.default_client_cert_source()

    @pytest.mark.asyncio
    @mock.patch(
        "google.auth.aio.transport.mtls.get_client_cert_and_key",
        new_callable=mock.AsyncMock,
    )
    @mock.patch(
        "google.auth.transport.mtls.has_default_client_cert_source", return_value=True
    )
    async def test_default_client_cert_source_success(
        self, mock_has_default, mock_get_cert_key
    ):
        """Tests the async callback returned by default_client_cert_source."""
        mock_get_cert_key.return_value = (True, CERT_DATA, KEY_DATA)

        # default_client_cert_source is a factory that returns an async callback
        callback = mtls.default_client_cert_source()
        assert callable(callback)

        cert, key = await callback()
        assert cert == CERT_DATA
        assert key == KEY_DATA

    @pytest.mark.asyncio
    @mock.patch(
        "google.auth.aio.transport.mtls.get_client_cert_and_key",
        new_callable=mock.AsyncMock,
    )
    @mock.patch(
        "google.auth.transport.mtls.has_default_client_cert_source", return_value=True
    )
    async def test_default_client_cert_source_callback_wraps_exception(
        self, mock_has, mock_get
    ):
        """Tests that the callback wraps underlying errors into MutualTLSChannelError."""
        mock_get.side_effect = ValueError("Format error")
        callback = mtls.default_client_cert_source()

        with pytest.raises(exceptions.MutualTLSChannelError) as excinfo:
            await callback()
        assert "Format error" in str(excinfo.value)

    @pytest.mark.asyncio
    @mock.patch("google.auth.transport._mtls_helper._get_workload_cert_and_key")
    async def test_get_client_ssl_credentials_success(self, mock_workload):
        """Tests successful retrieval of workload credentials via the executor."""
        mock_workload.return_value = (CERT_DATA, KEY_DATA)

        success, cert, key, passphrase = await mtls.get_client_ssl_credentials()

        assert success is True
        assert cert == CERT_DATA
        assert key == KEY_DATA
        assert passphrase is None

    @pytest.mark.asyncio
    @mock.patch("google.auth.aio.transport.mtls.get_client_ssl_credentials")
    async def test_get_client_cert_and_key_no_credentials_found(self, mock_get_ssl):
        """Tests behavior when no credentials are found at the default location."""
        mock_get_ssl.return_value = (False, None, None, None)

        success, cert, key = await mtls.get_client_cert_and_key(None)

        assert success is False
        assert cert is None
        assert key is None

    @pytest.mark.asyncio
    async def test_get_client_cert_and_key_callback_async(self):
        """Tests that an async callback is correctly awaited."""
        callback = mock.AsyncMock(return_value=(CERT_DATA, KEY_DATA))

        success, cert, key = await mtls.get_client_cert_and_key(callback)

        assert success is True
        assert cert == CERT_DATA
        assert key == KEY_DATA
        callback.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_client_cert_and_key_callback_sync(self):
        """Tests that a sync callback is handled via the TypeError fallback."""
        callback = mock.Mock(return_value=(CERT_DATA, KEY_DATA))

        success, cert, key = await mtls.get_client_cert_and_key(callback)

        assert success is True
        assert cert == CERT_DATA
        # Note: In the source, the first 'await' will call the function.
        # When it fails to await, the exception handler uses the result already obtained.
        assert callback.call_count == 1

    @pytest.mark.asyncio
    @mock.patch("google.auth.transport._mtls_helper._get_workload_cert_and_key")
    async def test_get_client_ssl_credentials_error(self, mock_workload):
        """Tests exception propagation from the workload helper."""
        mock_workload.side_effect = exceptions.ClientCertError(
            "Failed to read metadata"
        )

        with pytest.raises(exceptions.ClientCertError, match="Failed to read metadata"):
            await mtls.get_client_ssl_credentials()

    @pytest.mark.asyncio
    @mock.patch("google.auth.aio.transport.mtls.secure_cert_key_paths")
    async def test_make_client_cert_ssl_context_setup_error(self, mock_secure_paths):
        """Verifies that TransportError is raised when temp file creation fails."""
        cert_bytes = b"cert_data"
        key_bytes = b"key_data"

        mock_secure_paths.side_effect = OSError("Temp file error")

        with pytest.raises(exceptions.TransportError) as exc_info:
            mtls.make_client_cert_ssl_context(cert_bytes, key_bytes)

        assert "Failed to load client certificate" in str(exc_info.value)
        assert isinstance(exc_info.value.__cause__, OSError)
