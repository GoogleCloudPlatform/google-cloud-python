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

from unittest import mock

import pytest

from google.auth import exceptions
from google.auth.aio.transport import mtls

CERT_BYTES = (
    b"-----BEGIN CERTIFICATE-----\nMIID...CERT1...=\n-----END CERTIFICATE-----\n"
)
KEY_BYTES = (
    b"-----BEGIN PRIVATE KEY-----\nMIIE...KEY1...==\n-----END PRIVATE KEY-----\n"
)
NEW_CERT_BYTES = (
    b"-----BEGIN CERTIFICATE-----\nMIID...CERT2...=\n-----END CERTIFICATE-----\n"
)
NEW_KEY_BYTES = (
    b"-----BEGIN PRIVATE KEY-----\nMIIE...KEY2...==\n-----END PRIVATE KEY-----\n"
)


@pytest.mark.asyncio
async def test_check_parameters_no_client_cert():
    """Test when no certificate is discovered (has_cert is False)."""
    with mock.patch.object(
        mtls, "get_client_cert_and_key", return_value=(False, None, None)
    ):
        (
            cert,
            key,
            cached_fp,
            current_fp,
        ) = await mtls.check_parameters_for_unauthorized_response(
            cached_cert=b"stale_cert", client_cert_callback=None
        )

        assert cert is None
        assert key is None
        assert cached_fp is None
        assert current_fp is None


@pytest.mark.asyncio
async def test_check_parameters_cert_matched():
    """Test when newly retrieved certificate matches the cached certificate."""

    def callback():
        return CERT_BYTES, KEY_BYTES

    with (
        mock.patch("google.auth._agent_identity_utils.parse_certificate") as mock_parse,
        mock.patch(
            "google.auth._agent_identity_utils.calculate_certificate_fingerprint",
            return_value="FINGERPRINT_A",
        ),
        mock.patch(
            "google.auth._agent_identity_utils.get_cached_cert_fingerprint",
            return_value="FINGERPRINT_A",
        ) as mock_get_cached,
    ):
        (
            cert,
            key,
            cached_fp,
            current_fp,
        ) = await mtls.check_parameters_for_unauthorized_response(
            cached_cert=CERT_BYTES, client_cert_callback=callback
        )

    assert cert == CERT_BYTES
    assert key == KEY_BYTES
    assert cached_fp == "FINGERPRINT_A"
    assert current_fp == "FINGERPRINT_A"
    assert cached_fp == current_fp

    # These assertions will now work correctly using the bound mocks
    mock_parse.assert_called_once_with(CERT_BYTES)
    mock_get_cached.assert_called_once_with(CERT_BYTES)


@pytest.mark.asyncio
async def test_check_parameters_cert_mismatch_rotation():
    """Test when newly retrieved certificate differs from the cached certificate (rotation occurred)."""

    def callback():
        return NEW_CERT_BYTES, NEW_KEY_BYTES

    with (
        mock.patch("google.auth._agent_identity_utils.parse_certificate") as mock_parse,
        mock.patch(
            "google.auth._agent_identity_utils.calculate_certificate_fingerprint",
            return_value="FINGERPRINT_NEW",
        ),
        mock.patch(
            "google.auth._agent_identity_utils.get_cached_cert_fingerprint",
            return_value="FINGERPRINT_OLD",
        ) as mock_get_cached,
    ):
        (
            cert,
            key,
            cached_fp,
            current_fp,
        ) = await mtls.check_parameters_for_unauthorized_response(
            cached_cert=CERT_BYTES, client_cert_callback=callback
        )

    assert cert == NEW_CERT_BYTES
    assert key == NEW_KEY_BYTES
    assert cached_fp == "FINGERPRINT_OLD"
    assert current_fp == "FINGERPRINT_NEW"
    assert cached_fp != current_fp

    # The fix: mock_parse is called with the NEW cert from the callback
    mock_parse.assert_called_once_with(NEW_CERT_BYTES)
    # mock_get_cached is called with the old cached cert
    mock_get_cached.assert_called_once_with(CERT_BYTES)


@pytest.mark.asyncio
async def test_check_parameters_without_cached_cert():
    """Test when cached_cert is None."""

    def callback():
        return CERT_BYTES, KEY_BYTES

    with (
        mock.patch("google.auth._agent_identity_utils.parse_certificate"),
        mock.patch(
            "google.auth._agent_identity_utils.calculate_certificate_fingerprint",
            return_value="FINGERPRINT_CURRENT",
        ),
        mock.patch(
            "google.auth._agent_identity_utils.get_cached_cert_fingerprint"
        ) as mock_get_cached,
    ):
        (
            cert,
            key,
            cached_fp,
            current_fp,
        ) = await mtls.check_parameters_for_unauthorized_response(
            cached_cert=None, client_cert_callback=callback
        )

        assert cert == CERT_BYTES
        assert key == KEY_BYTES
        assert cached_fp is None
        assert current_fp == "FINGERPRINT_CURRENT"
        assert cached_fp != current_fp
        mock_get_cached.assert_not_called()


@pytest.mark.asyncio
async def test_check_parameters_executor_fingerprint_computation():
    """Test that fingerprint computation is properly offloaded to the executor."""

    def callback():
        return CERT_BYTES, KEY_BYTES

    with (
        mock.patch.object(
            mtls, "_run_in_executor", wraps=mtls._run_in_executor
        ) as mock_run_in_executor,
        mock.patch("google.auth._agent_identity_utils.parse_certificate"),
        mock.patch(
            "google.auth._agent_identity_utils.calculate_certificate_fingerprint",
            return_value="FP_CURRENT",
        ),
        mock.patch(
            "google.auth._agent_identity_utils.get_cached_cert_fingerprint",
            return_value="FP_CACHED",
        ),
    ):
        (
            cert,
            key,
            cached_fp,
            current_fp,
        ) = await mtls.check_parameters_for_unauthorized_response(
            cached_cert=CERT_BYTES, client_cert_callback=callback
        )

        assert mock_run_in_executor.called
        assert cert == CERT_BYTES
        assert cached_fp == "FP_CACHED"
        assert current_fp == "FP_CURRENT"


@pytest.mark.asyncio
async def test_check_parameters_callback_exception_propagation():
    """Test that exceptions raised by client_cert_callback propagate cleanly."""

    def failing_callback():
        raise exceptions.ClientCertError("Client cert provider failed")

    with pytest.raises(exceptions.ClientCertError, match="Client cert provider failed"):
        await mtls.check_parameters_for_unauthorized_response(
            cached_cert=CERT_BYTES, client_cert_callback=failing_callback
        )


@pytest.mark.asyncio
async def test_check_parameters_async_callback_exception_propagation():
    """Test that exceptions raised in an async client_cert_callback propagate cleanly."""

    async def failing_async_callback():
        raise OSError("Disk read error while loading certificates")

    with pytest.raises(OSError, match="Disk read error while loading certificates"):
        await mtls.check_parameters_for_unauthorized_response(
            cached_cert=CERT_BYTES, client_cert_callback=failing_async_callback
        )
