# Copyright 2020 Google LLC
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

import datetime
from unittest import mock

import pytest  # type: ignore

from google.auth import _helpers, crypt, jwt, transport
from google.oauth2 import _service_account_async as service_account
from tests.oauth2 import test_service_account


class TestCredentials(object):
    SERVICE_ACCOUNT_EMAIL = "service-account@example.com"
    TOKEN_URI = "https://example.com/oauth2/token"

    @classmethod
    def make_credentials(cls):
        return service_account.Credentials(
            test_service_account.SIGNER, cls.SERVICE_ACCOUNT_EMAIL, cls.TOKEN_URI
        )

    def test_from_service_account_info(self):
        credentials = service_account.Credentials.from_service_account_info(
            test_service_account.SERVICE_ACCOUNT_INFO
        )

        assert (
            credentials._signer.key_id
            == test_service_account.SERVICE_ACCOUNT_INFO["private_key_id"]
        )
        assert (
            credentials.service_account_email
            == test_service_account.SERVICE_ACCOUNT_INFO["client_email"]
        )
        assert (
            credentials._token_uri
            == test_service_account.SERVICE_ACCOUNT_INFO["token_uri"]
        )

    def test_from_service_account_info_args(self):
        info = test_service_account.SERVICE_ACCOUNT_INFO.copy()
        scopes = ["email", "profile"]
        subject = "subject"
        additional_claims = {"meta": "data"}

        credentials = service_account.Credentials.from_service_account_info(
            info, scopes=scopes, subject=subject, additional_claims=additional_claims
        )

        assert credentials.service_account_email == info["client_email"]
        assert credentials.project_id == info["project_id"]
        assert credentials._signer.key_id == info["private_key_id"]
        assert credentials._token_uri == info["token_uri"]
        assert credentials._scopes == scopes
        assert credentials._subject == subject
        assert credentials._additional_claims == additional_claims

    def test_from_service_account_file(self):
        info = test_service_account.SERVICE_ACCOUNT_INFO.copy()

        credentials = service_account.Credentials.from_service_account_file(
            test_service_account.SERVICE_ACCOUNT_JSON_FILE
        )

        assert credentials.service_account_email == info["client_email"]
        assert credentials.project_id == info["project_id"]
        assert credentials._signer.key_id == info["private_key_id"]
        assert credentials._token_uri == info["token_uri"]

    def test_from_service_account_file_args(self):
        info = test_service_account.SERVICE_ACCOUNT_INFO.copy()
        scopes = ["email", "profile"]
        subject = "subject"
        additional_claims = {"meta": "data"}

        credentials = service_account.Credentials.from_service_account_file(
            test_service_account.SERVICE_ACCOUNT_JSON_FILE,
            subject=subject,
            scopes=scopes,
            additional_claims=additional_claims,
        )

        assert credentials.service_account_email == info["client_email"]
        assert credentials.project_id == info["project_id"]
        assert credentials._signer.key_id == info["private_key_id"]
        assert credentials._token_uri == info["token_uri"]
        assert credentials._scopes == scopes
        assert credentials._subject == subject
        assert credentials._additional_claims == additional_claims

    def test_default_state(self):
        credentials = self.make_credentials()
        assert not credentials.valid
        # Expiration hasn't been set yet
        assert not credentials.expired
        # Scopes haven't been specified yet
        assert credentials.requires_scopes

    def test_sign_bytes(self):
        credentials = self.make_credentials()
        to_sign = b"123"
        signature = credentials.sign_bytes(to_sign)
        assert crypt.verify_signature(
            to_sign, signature, test_service_account.PUBLIC_CERT_BYTES
        )

    def test_signer(self):
        credentials = self.make_credentials()
        assert isinstance(credentials.signer, crypt.Signer)

    def test_signer_email(self):
        credentials = self.make_credentials()
        assert credentials.signer_email == self.SERVICE_ACCOUNT_EMAIL

    def test_create_scoped(self):
        credentials = self.make_credentials()
        scopes = ["email", "profile"]
        credentials = credentials.with_scopes(scopes)
        assert credentials._scopes == scopes

    def test_with_claims(self):
        credentials = self.make_credentials()
        new_credentials = credentials.with_claims({"meep": "moop"})
        assert new_credentials._additional_claims == {"meep": "moop"}

    @pytest.mark.asyncio
    async def test_with_quota_project(self):
        credentials = self.make_credentials()
        new_credentials = credentials.with_quota_project("new-project-456")
        assert new_credentials.quota_project_id == "new-project-456"
        request = mock.create_autospec(transport.Request, instance=True)
        hdrs = {}
        new_credentials.token = "tok"
        await new_credentials.before_request(
            request, "GET", "https://example.com", hdrs
        )
        assert hdrs.get("x-goog-user-project") == "new-project-456"

    def test__make_authorization_grant_assertion(self):
        credentials = self.make_credentials()
        token = credentials._make_authorization_grant_assertion()
        payload = jwt.decode(token, test_service_account.PUBLIC_CERT_BYTES)
        assert payload["iss"] == self.SERVICE_ACCOUNT_EMAIL
        assert (
            payload["aud"]
            == service_account.service_account._GOOGLE_OAUTH2_TOKEN_ENDPOINT
        )

    def test__make_authorization_grant_assertion_scoped(self):
        credentials = self.make_credentials()
        scopes = ["email", "profile"]
        credentials = credentials.with_scopes(scopes)
        token = credentials._make_authorization_grant_assertion()
        payload = jwt.decode(token, test_service_account.PUBLIC_CERT_BYTES)
        assert payload["scope"] == "email profile"

    def test__make_authorization_grant_assertion_subject(self):
        credentials = self.make_credentials()
        subject = "user@example.com"
        credentials = credentials.with_subject(subject)
        token = credentials._make_authorization_grant_assertion()
        payload = jwt.decode(token, test_service_account.PUBLIC_CERT_BYTES)
        assert payload["sub"] == subject

    @mock.patch("google.oauth2._client_async.jwt_grant", autospec=True)
    @pytest.mark.asyncio
    async def test_refresh_success(self, jwt_grant):
        credentials = self.make_credentials()
        token = "token"
        jwt_grant.return_value = (
            token,
            _helpers.utcnow() + datetime.timedelta(seconds=500),
            {},
        )
        request = mock.create_autospec(transport.Request, instance=True)

        # Refresh credentials
        await credentials.refresh(request)

        # Check jwt grant call.
        assert jwt_grant.called

        called_request, token_uri, assertion = jwt_grant.call_args[0]
        assert called_request == request
        assert token_uri == credentials._token_uri
        assert jwt.decode(assertion, test_service_account.PUBLIC_CERT_BYTES)
        # No further assertion done on the token, as there are separate tests
        # for checking the authorization grant assertion.

        # Check that the credentials have the token.
        assert credentials.token == token

        # Check that the credentials are valid (have a token and are not
        # expired)
        assert credentials.valid

    @mock.patch("google.oauth2._client_async.jwt_grant", autospec=True)
    @pytest.mark.asyncio
    async def test_before_request_refreshes(self, jwt_grant):
        credentials = self.make_credentials()
        token = "token"
        jwt_grant.return_value = (
            token,
            _helpers.utcnow() + datetime.timedelta(seconds=500),
            None,
        )
        request = mock.create_autospec(transport.Request, instance=True)

        # Credentials should start as invalid
        assert not credentials.valid

        # before_request should cause a refresh
        await credentials.before_request(request, "GET", "http://example.com?a=1#3", {})

        # The refresh endpoint should've been called.
        assert jwt_grant.called

        # Credentials should now be valid.
        assert credentials.valid

    @pytest.mark.asyncio
    async def test_before_request_triggers_rab_refresh(self):
        credentials = self.make_credentials()
        credentials.token = "tok"

        request = mock.AsyncMock(spec=["transport.Request"])
        headers1 = {}

        with (
            mock.patch.object(
                credentials,
                "_lookup_regional_access_boundary",
                new_callable=mock.AsyncMock,
            ) as mock_lookup,
            mock.patch.object(
                credentials,
                "_is_regional_access_boundary_lookup_required",
                return_value=True,
            ),
        ):
            mock_lookup.return_value = {
                "locations": ["us-central1", "europe-west1"],
                "encodedLocations": "0xA30",
            }

            # The first request triggers a background refresh and returns immediately.
            await credentials.before_request(
                request, "GET", "https://storage.googleapis.com/bucket", headers1
            )
            assert "x-allowed-locations" not in headers1

            # Wait for the background task to finish and update the cache.
            await credentials._rab_manager.refresh_manager._worker_task
            mock_lookup.assert_called_once_with(request)

            # The second request retrieves the locations from the cache.
            headers2 = {}
            await credentials.before_request(
                request, "GET", "https://storage.googleapis.com/bucket", headers2
            )
            assert headers2["x-allowed-locations"] == "0xA30"

    @pytest.mark.asyncio
    async def test_before_request_rab_refresh_failure_ignored(self):
        credentials = self.make_credentials()
        credentials.token = "tok"

        request = mock.AsyncMock(spec=["transport.Request"])
        headers = {}

        with (
            mock.patch.object(
                credentials,
                "_lookup_regional_access_boundary",
                new_callable=mock.AsyncMock,
                side_effect=Exception("Transport failed"),
            ) as mock_lookup,
            mock.patch.object(
                credentials,
                "_is_regional_access_boundary_lookup_required",
                return_value=True,
            ),
        ):
            # Any transport/lookup failure must be caught gracefully during refresh.
            await credentials.before_request(
                request, "GET", "https://storage.googleapis.com/bucket", headers
            )

            # Wait for the background task to finish.
            await credentials._rab_manager.refresh_manager._worker_task

            mock_lookup.assert_called_once_with(request)
            assert "x-allowed-locations" not in headers

    @pytest.mark.asyncio
    async def test_before_request_triggers_blocking_rab_refresh(self):
        credentials = self.make_credentials()
        credentials.token = "tok"
        credentials._set_blocking_regional_access_boundary_lookup()

        request = mock.AsyncMock(spec=["transport.Request"])
        headers = {}

        with (
            mock.patch.object(
                credentials,
                "_lookup_regional_access_boundary",
                new_callable=mock.AsyncMock,
            ) as mock_lookup,
            mock.patch.object(
                credentials,
                "_is_regional_access_boundary_lookup_required",
                return_value=True,
            ),
        ):
            mock_lookup.return_value = {
                "locations": ["us-central1", "europe-west1"],
                "encodedLocations": "0xA30",
            }

            # When blocking lookup is enabled, the first request awaits the lookup sequentially.
            await credentials.before_request(
                request, "GET", "https://storage.googleapis.com/bucket", headers
            )

            mock_lookup.assert_called_once_with(request, fail_fast=True)
            assert headers["x-allowed-locations"] == "0xA30"

    @pytest.mark.asyncio
    async def test_maybe_start_regional_access_boundary_refresh_async_invalid_url(self):
        credentials = self.make_credentials()
        request = mock.create_autospec(transport.Request)

        # Verifies that passing invalid/non-string URLs asynchronously fails safe without crashing.
        await credentials._maybe_start_regional_access_boundary_refresh_async(
            request, url=None
        )
        await credentials._maybe_start_regional_access_boundary_refresh_async(
            request, url=123
        )
        await credentials._maybe_start_regional_access_boundary_refresh_async(
            request, url=object()
        )

    def test_unpickle_old_credentials_without_rab(self):
        from google.auth import _regional_access_boundary_utils

        credentials = self.make_credentials()
        old_state = credentials.__dict__.copy()
        if "_rab_manager" in old_state:
            del old_state["_rab_manager"]
        if "_use_non_blocking_refresh" in old_state:
            del old_state["_use_non_blocking_refresh"]
        if "_refresh_worker" in old_state:
            del old_state["_refresh_worker"]

        new_instance = type(credentials).__new__(type(credentials))
        new_instance.__setstate__(old_state)

        # Verify the manager was correctly restored with the async refresh manager!
        assert hasattr(new_instance, "_rab_manager")
        assert isinstance(
            new_instance._rab_manager.refresh_manager,
            _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager,
        )


class TestIDTokenCredentials(object):
    SERVICE_ACCOUNT_EMAIL = "service-account@example.com"
    TOKEN_URI = "https://example.com/oauth2/token"
    TARGET_AUDIENCE = "https://example.com"

    @classmethod
    def make_credentials(cls):
        return service_account.IDTokenCredentials(
            test_service_account.SIGNER,
            cls.SERVICE_ACCOUNT_EMAIL,
            cls.TOKEN_URI,
            cls.TARGET_AUDIENCE,
        )

    def test_from_service_account_info(self):
        credentials = service_account.IDTokenCredentials.from_service_account_info(
            test_service_account.SERVICE_ACCOUNT_INFO,
            target_audience=self.TARGET_AUDIENCE,
        )

        assert (
            credentials._signer.key_id
            == test_service_account.SERVICE_ACCOUNT_INFO["private_key_id"]
        )
        assert (
            credentials.service_account_email
            == test_service_account.SERVICE_ACCOUNT_INFO["client_email"]
        )
        assert (
            credentials._token_uri
            == test_service_account.SERVICE_ACCOUNT_INFO["token_uri"]
        )
        assert credentials._target_audience == self.TARGET_AUDIENCE

    def test_from_service_account_file(self):
        info = test_service_account.SERVICE_ACCOUNT_INFO.copy()

        credentials = service_account.IDTokenCredentials.from_service_account_file(
            test_service_account.SERVICE_ACCOUNT_JSON_FILE,
            target_audience=self.TARGET_AUDIENCE,
        )

        assert credentials.service_account_email == info["client_email"]
        assert credentials._signer.key_id == info["private_key_id"]
        assert credentials._token_uri == info["token_uri"]
        assert credentials._target_audience == self.TARGET_AUDIENCE

    def test_default_state(self):
        credentials = self.make_credentials()
        assert not credentials.valid
        # Expiration hasn't been set yet
        assert not credentials.expired

    def test_sign_bytes(self):
        credentials = self.make_credentials()
        to_sign = b"123"
        signature = credentials.sign_bytes(to_sign)
        assert crypt.verify_signature(
            to_sign, signature, test_service_account.PUBLIC_CERT_BYTES
        )

    def test_signer(self):
        credentials = self.make_credentials()
        assert isinstance(credentials.signer, crypt.Signer)

    def test_signer_email(self):
        credentials = self.make_credentials()
        assert credentials.signer_email == self.SERVICE_ACCOUNT_EMAIL

    def test_with_target_audience(self):
        credentials = self.make_credentials()
        new_credentials = credentials.with_target_audience("https://new.example.com")
        assert new_credentials._target_audience == "https://new.example.com"

    def test_with_quota_project(self):
        credentials = self.make_credentials()
        new_credentials = credentials.with_quota_project("project-foo")
        assert new_credentials._quota_project_id == "project-foo"

    def test__make_authorization_grant_assertion(self):
        credentials = self.make_credentials()
        token = credentials._make_authorization_grant_assertion()
        payload = jwt.decode(token, test_service_account.PUBLIC_CERT_BYTES)
        assert payload["iss"] == self.SERVICE_ACCOUNT_EMAIL
        assert (
            payload["aud"]
            == service_account.service_account._GOOGLE_OAUTH2_TOKEN_ENDPOINT
        )
        assert payload["target_audience"] == self.TARGET_AUDIENCE

    @mock.patch("google.oauth2._client_async.id_token_jwt_grant", autospec=True)
    @pytest.mark.asyncio
    async def test_refresh_success(self, id_token_jwt_grant):
        credentials = self.make_credentials()
        token = "token"
        id_token_jwt_grant.return_value = (
            token,
            _helpers.utcnow() + datetime.timedelta(seconds=500),
            {},
        )

        request = mock.AsyncMock(spec=["transport.Request"])

        # Refresh credentials
        await credentials.refresh(request)

        # Check jwt grant call.
        assert id_token_jwt_grant.called

        called_request, token_uri, assertion = id_token_jwt_grant.call_args[0]
        assert called_request == request
        assert token_uri == credentials._token_uri
        assert jwt.decode(assertion, test_service_account.PUBLIC_CERT_BYTES)
        # No further assertion done on the token, as there are separate tests
        # for checking the authorization grant assertion.

        # Check that the credentials have the token.
        assert credentials.token == token

        # Check that the credentials are valid (have a token and are not
        # expired)
        assert credentials.valid

    @mock.patch("google.oauth2._client_async.id_token_jwt_grant", autospec=True)
    @pytest.mark.asyncio
    async def test_before_request_refreshes(self, id_token_jwt_grant):
        credentials = self.make_credentials()
        token = "token"
        id_token_jwt_grant.return_value = (
            token,
            _helpers.utcnow() + datetime.timedelta(seconds=500),
            None,
        )
        request = mock.AsyncMock(spec=["transport.Request"])

        # Credentials should start as invalid
        assert not credentials.valid

        # before_request should cause a refresh
        await credentials.before_request(request, "GET", "http://example.com?a=1#3", {})

        # The refresh endpoint should've been called.
        assert id_token_jwt_grant.called

        # Credentials should now be valid.
        assert credentials.valid
