# Copyright 2016 Google LLC
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

from google.auth import _helpers, credentials


class CredentialsImpl(credentials.CredentialsWithRegionalAccessBoundary):
    def __init__(self, universe_domain=None):
        super(CredentialsImpl, self).__init__()
        if universe_domain:
            self._universe_domain = universe_domain

    def _perform_refresh_token(self, request):
        self.token = "refreshed-token"
        self.expiry = (
            datetime.datetime.utcnow()
            + _helpers.REFRESH_THRESHOLD
            + datetime.timedelta(seconds=5)
        )

    def with_quota_project(self, quota_project_id):
        raise NotImplementedError()

    def _build_regional_access_boundary_lookup_url(self, request=None):
        # Using self.token here to make the URL dynamic for testing purposes
        return "http://mock.url/lookup_for_{}".format(self.token)

    def _make_copy(self):
        new_credentials = self.__class__()
        self._copy_regional_access_boundary_manager(new_credentials)
        return new_credentials


class CredentialsImplWithMetrics(credentials.Credentials):
    def refresh(self, request):
        self.token = request

    def _metric_header_for_usage(self):
        return "foo"


def test_credentials_constructor():
    credentials = CredentialsImpl()
    assert not credentials.token
    assert not credentials.expiry
    assert not credentials.expired
    assert not credentials.valid
    assert credentials.universe_domain == "googleapis.com"
    assert not credentials._use_non_blocking_refresh


def test_credentials_get_cred_info():
    credentials = CredentialsImpl()
    assert not credentials.get_cred_info()


def test_with_non_blocking_refresh():
    c = CredentialsImpl()
    c.with_non_blocking_refresh()
    assert c._use_non_blocking_refresh


def test_expired_and_valid():
    credentials = CredentialsImpl()
    credentials.token = "token"

    assert credentials.valid
    assert not credentials.expired

    # Set the expiration to one second more than now plus the clock skew
    # accomodation. These credentials should be valid.
    credentials.expiry = (
        _helpers.utcnow() + _helpers.REFRESH_THRESHOLD + datetime.timedelta(seconds=1)
    )

    assert credentials.valid
    assert not credentials.expired

    # Set the credentials expiration to now. Because of the clock skew
    # accomodation, these credentials should report as expired.
    credentials.expiry = _helpers.utcnow()

    assert not credentials.valid
    assert credentials.expired


def test_before_request():
    credentials = CredentialsImpl()
    request = mock.Mock()
    headers = {}

    # First call should call refresh, setting the token.
    credentials.before_request(request, "GET", "http://example.com", headers)
    assert credentials.valid
    assert credentials.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert "x-allowed-locations" not in headers

    request = mock.Mock()
    headers = {}

    # Second call shouldn't call refresh.
    credentials.before_request(request, "GET", "http://example.com", headers)
    assert credentials.valid
    assert credentials.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert "x-allowed-locations" not in headers


def test_before_request_with_regional_access_boundary():
    DUMMY_BOUNDARY = "0xA30"
    creds = CredentialsImpl()
    creds._rab_manager._data = credentials._regional_access_boundary_utils._RegionalAccessBoundaryData(
        encoded_locations=DUMMY_BOUNDARY,
        expiry=_helpers.utcnow() + datetime.timedelta(hours=1),
        cooldown_expiry=None,
        cooldown_duration=credentials._regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
    )
    request = mock.Mock()
    headers = {}

    # First call should call refresh, setting the token.
    creds.before_request(request, "GET", "http://example.com", headers)
    assert creds.valid
    assert creds.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert headers["x-allowed-locations"] == DUMMY_BOUNDARY

    request = mock.Mock()
    headers = {}

    # Second call shouldn't call refresh.
    creds.before_request(request, "GET", "http://example.com", headers)
    assert creds.valid
    assert creds.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert headers["x-allowed-locations"] == DUMMY_BOUNDARY


def test_copy_regional_access_boundary_manager_state_and_config():
    creds = CredentialsImpl()
    creds._rab_manager._data = mock.sentinel.rab_data
    creds._rab_manager._use_blocking_regional_access_boundary_lookup = True

    new_creds = creds._make_copy()

    # Verify references to immutable boundary data are shared
    assert new_creds._rab_manager._data == mock.sentinel.rab_data
    # Verify blocking config flag is preserved
    assert new_creds._rab_manager._use_blocking_regional_access_boundary_lookup is True
    # Verify target manager object is isolated (kept from constructor, not replaced)
    assert new_creds._rab_manager is not creds._rab_manager


def test_before_request_metrics():
    credentials = CredentialsImplWithMetrics()
    request = "token"
    headers = {}

    credentials.before_request(request, "GET", "http://example.com", headers)
    assert headers["x-goog-api-client"] == "foo"


def test_anonymous_credentials_ctor():
    anon = credentials.AnonymousCredentials()
    assert anon.token is None
    assert anon.expiry is None
    assert not anon.expired
    assert anon.valid


def test_anonymous_credentials_refresh():
    anon = credentials.AnonymousCredentials()
    request = object()
    with pytest.raises(ValueError):
        anon.refresh(request)


def test_anonymous_credentials_apply_default():
    anon = credentials.AnonymousCredentials()
    headers = {}
    anon.apply(headers)
    assert headers == {}
    with pytest.raises(ValueError):
        anon.apply(headers, token="TOKEN")


def test_anonymous_credentials_before_request():
    anon = credentials.AnonymousCredentials()
    request = object()
    method = "GET"
    url = "https://example.com/api/endpoint"
    headers = {}
    anon.before_request(request, method, url, headers)
    assert headers == {}


class ReadOnlyScopedCredentialsImpl(credentials.ReadOnlyScoped, CredentialsImpl):
    @property
    def requires_scopes(self):
        return super(ReadOnlyScopedCredentialsImpl, self).requires_scopes


def test_readonly_scoped_credentials_constructor():
    credentials = ReadOnlyScopedCredentialsImpl()
    assert credentials._scopes is None


def test_readonly_scoped_credentials_scopes():
    credentials = ReadOnlyScopedCredentialsImpl()
    credentials._scopes = ["one", "two"]
    assert credentials.scopes == ["one", "two"]
    assert credentials.has_scopes(["one"])
    assert credentials.has_scopes(["two"])
    assert credentials.has_scopes(["one", "two"])
    assert not credentials.has_scopes(["three"])

    # Test with default scopes
    credentials_with_default = ReadOnlyScopedCredentialsImpl()
    credentials_with_default._default_scopes = ["one", "two"]
    assert credentials_with_default.has_scopes(["one", "two"])
    assert not credentials_with_default.has_scopes(["three"])

    # Test with no scopes
    credentials_no_scopes = ReadOnlyScopedCredentialsImpl()
    assert not credentials_no_scopes.has_scopes(["one"])

    assert credentials_no_scopes.has_scopes([])


def test_readonly_scoped_credentials_requires_scopes():
    credentials = ReadOnlyScopedCredentialsImpl()
    assert not credentials.requires_scopes


class RequiresScopedCredentialsImpl(credentials.Scoped, CredentialsImpl):
    def __init__(self, scopes=None, default_scopes=None):
        super(RequiresScopedCredentialsImpl, self).__init__()
        self._scopes = scopes
        self._default_scopes = default_scopes

    @property
    def requires_scopes(self):
        return not self.scopes

    def with_scopes(self, scopes, default_scopes=None):
        return RequiresScopedCredentialsImpl(
            scopes=scopes, default_scopes=default_scopes
        )


def test_create_scoped_if_required_scoped():
    unscoped_credentials = RequiresScopedCredentialsImpl()
    scoped_credentials = credentials.with_scopes_if_required(
        unscoped_credentials, ["one", "two"]
    )

    assert scoped_credentials is not unscoped_credentials
    assert not scoped_credentials.requires_scopes
    assert scoped_credentials.has_scopes(["one", "two"])


def test_create_scoped_if_required_not_scopes():
    unscoped_credentials = CredentialsImpl()
    scoped_credentials = credentials.with_scopes_if_required(
        unscoped_credentials, ["one", "two"]
    )

    assert scoped_credentials is unscoped_credentials


def test_nonblocking_refresh_fresh_credentials():
    c = CredentialsImpl()

    c._refresh_worker = mock.MagicMock()

    request = mock.Mock()

    c.refresh(request)
    assert c.token_state == credentials.TokenState.FRESH

    c.with_non_blocking_refresh()
    c.before_request(request, "GET", "http://example.com", {})


def test_nonblocking_refresh_invalid_credentials():
    c = CredentialsImpl()
    c.with_non_blocking_refresh()

    request = mock.Mock()
    headers = {}

    assert c.token_state == credentials.TokenState.INVALID

    c.before_request(request, "GET", "http://example.com", headers)
    assert c.token_state == credentials.TokenState.FRESH
    assert c.valid
    assert c.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert "x-identity-trust-boundary" not in headers


def test_nonblocking_refresh_stale_credentials():
    c = CredentialsImpl()
    c.with_non_blocking_refresh()

    request = mock.Mock()
    headers = {}

    # Invalid credentials MUST require a blocking refresh.
    c.before_request(request, "GET", "http://example.com", headers)
    assert c.token_state == credentials.TokenState.FRESH
    assert not c._refresh_worker._worker

    c.expiry = (
        datetime.datetime.utcnow()
        + _helpers.REFRESH_THRESHOLD
        - datetime.timedelta(seconds=1)
    )

    # STALE credentials SHOULD spawn a non-blocking worker
    assert c.token_state == credentials.TokenState.STALE
    c.before_request(request, "GET", "http://example.com", headers)
    assert c._refresh_worker._worker is not None

    assert c.token_state == credentials.TokenState.FRESH
    assert c.valid
    assert c.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert "x-identity-trust-boundary" not in headers


def test_nonblocking_refresh_failed_credentials():
    c = CredentialsImpl()
    c.with_non_blocking_refresh()

    request = mock.Mock()
    headers = {}

    # Invalid credentials MUST require a blocking refresh.
    c.before_request(request, "GET", "http://example.com", headers)
    assert c.token_state == credentials.TokenState.FRESH
    assert not c._refresh_worker._worker

    c.expiry = (
        datetime.datetime.utcnow()
        + _helpers.REFRESH_THRESHOLD
        - datetime.timedelta(seconds=1)
    )

    # STALE credentials SHOULD spawn a non-blocking worker
    assert c.token_state == credentials.TokenState.STALE
    c._refresh_worker._worker = mock.MagicMock()
    c._refresh_worker._worker._error_info = "Some Error"
    c.before_request(request, "GET", "http://example.com", headers)
    assert c._refresh_worker._worker is not None

    assert c.token_state == credentials.TokenState.FRESH
    assert c.valid
    assert c.token == "refreshed-token"
    assert headers["authorization"] == "Bearer refreshed-token"
    assert "x-identity-trust-boundary" not in headers


def test_token_state_no_expiry():
    c = CredentialsImpl()

    request = mock.Mock()
    c.refresh(request)

    c.expiry = None
    assert c.token_state == credentials.TokenState.FRESH

    c.before_request(request, "GET", "http://example.com", {})


def test_credentials_with_trust_boundary_bridge():
    class LegacySubclass(credentials.CredentialsWithTrustBoundary):
        def _perform_refresh_token(self, request):
            pass

        def _build_trust_boundary_lookup_url(self):
            return "http://legacy.url"

    creds = LegacySubclass()

    # Verify that calling the new method delegates to the old method
    with pytest.warns(DeprecationWarning):
        assert creds._build_regional_access_boundary_lookup_url() == "http://legacy.url"


def test_before_request_triggers_rab_refresh():
    with mock.patch("google.oauth2._client._lookup_regional_access_boundary") as lookup:
        lookup.return_value = {"encodedLocations": "0xA30"}

        creds = CredentialsImpl()
        creds = creds._set_blocking_regional_access_boundary_lookup()

        request = mock.Mock()
        headers = {}

        # Initial state: no token
        assert creds.token is None

        # before_request should trigger token refresh and THEN RAB refresh.
        # We verify this by checking that the RAB lookup was called with
        # the URL containing the refreshed token.
        creds.before_request(request, "GET", "http://example.com", headers)

        assert creds.token == "refreshed-token"
        assert headers["authorization"] == "Bearer refreshed-token"
        assert headers["x-allowed-locations"] == "0xA30"

        # Verify lookup was called with the refreshed token's URL
        lookup.assert_called_once()
        args, kwargs = lookup.call_args
        assert args[1] == "http://mock.url/lookup_for_refreshed-token"


def test_maybe_start_regional_access_boundary_refresh_invalid_url():
    credentials_instance = CredentialsImpl()
    request = mock.Mock()

    # Verifies that passing invalid/non-string URLs synchronously fails safe without crashing.
    credentials_instance._maybe_start_regional_access_boundary_refresh(
        request, url=None
    )
    credentials_instance._maybe_start_regional_access_boundary_refresh(request, url=123)
    credentials_instance._maybe_start_regional_access_boundary_refresh(
        request, url=object()
    )
