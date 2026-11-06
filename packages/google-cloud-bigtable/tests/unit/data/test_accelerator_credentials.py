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
"""Unit tests for the accelerator credential-safety guardrail: which auth
configuration the client forwards to the daemon vs. falls back to native for.
These exercise pure helpers on the async client without spinning up a full
client or event loop."""

from types import SimpleNamespace

import pytest
from google.api_core.client_options import ClientOptions
from google.auth import (
    compute_engine,
    external_account_authorized_user,
    identity_pool,
    impersonated_credentials,
)
from google.oauth2 import (
    credentials as oauth2_credentials,
)
from google.oauth2 import (
    gdch_credentials,
    service_account,
)

import google.cloud.bigtable
from google.cloud.bigtable.data._async import client as _async_client_mod
from google.cloud.bigtable.data._async.client import (
    _UNSET,
    BigtableDataClientAsync,
    _DataApiTargetAsync,
)
from google.cloud.bigtable.data._sync_autogen import client as _sync_client_mod


def _bare_client(cls=BigtableDataClientAsync, unset=_UNSET):
    """A client instance that skips __init__ (no network / event loop)."""
    c = object.__new__(cls)
    c._cached_principal = unset
    c._cached_cred_type = unset
    return c


class _FakeCreds:
    """Stand-in credential exposing (or not) a service_account_email."""

    def __init__(self, email=None):
        if email is not None:
            self.service_account_email = email


class TestInitAcceleratorConfig:
    def test_no_config_forwards_default_scopes(self):
        c = _bare_client()
        c._init_accelerator_config(explicit_credentials=False, client_options=None)
        assert c._accelerator_blocked_reason is None
        assert "--scopes" in c._accelerator_flags
        assert c._accelerator_env == {}

    def test_explicit_credentials_blocks(self):
        c = _bare_client()
        c._init_accelerator_config(explicit_credentials=True, client_options=None)
        assert c._accelerator_blocked_reason is not None
        assert "credentials" in c._accelerator_blocked_reason

    def test_api_key_blocks(self):
        c = _bare_client()
        c._init_accelerator_config(
            explicit_credentials=False, client_options=ClientOptions(api_key="AIzaKEY")
        )
        assert "api_key" in c._accelerator_blocked_reason

    def test_client_cert_source_blocks(self):
        c = _bare_client()
        c._init_accelerator_config(
            explicit_credentials=False,
            client_options=ClientOptions(client_cert_source=lambda: (b"", b"")),
        )
        assert "client_cert_source" in c._accelerator_blocked_reason

    def test_forwards_non_secret_knobs(self):
        c = _bare_client()
        opts = ClientOptions(
            scopes=["https://www.googleapis.com/auth/custom"],
            quota_project_id="quota-proj",
            api_endpoint="https://custom.example.com:443",
            universe_domain="my-universe.example.com",
        )
        c._init_accelerator_config(explicit_credentials=False, client_options=opts)
        flags = c._accelerator_flags
        assert flags[flags.index("--scopes") + 1] == (
            "https://www.googleapis.com/auth/custom"
        )
        assert flags[flags.index("--quota-project") + 1] == "quota-proj"
        # api_endpoint is normalized to host:port (scheme stripped).
        assert flags[flags.index("--data-endpoint") + 1] == "custom.example.com:443"
        assert flags[flags.index("--universe-domain") + 1] == "my-universe.example.com"
        assert c._accelerator_blocked_reason is None

    def test_default_universe_not_forwarded(self):
        c = _bare_client()
        c._init_accelerator_config(
            explicit_credentials=False,
            client_options=ClientOptions(universe_domain="googleapis.com"),
        )
        assert "--universe-domain" not in c._accelerator_flags

    def test_credentials_file_forwarded_as_env_path(self):
        c = _bare_client()
        c._init_accelerator_config(
            explicit_credentials=False,
            client_options=ClientOptions(credentials_file="/path/to/key.json"),
        )
        assert c._accelerator_env["GOOGLE_APPLICATION_CREDENTIALS"] == (
            "/path/to/key.json"
        )
        # The path is not a "secret" that blocks acceleration.
        assert c._accelerator_blocked_reason is None

    def test_caller_user_agent_forwarded(self):
        c = _bare_client()
        c._init_accelerator_config(explicit_credentials=False, client_options=None)
        flags = c._accelerator_flags
        expected = f"python-v{google.cloud.bigtable.__version__}"
        assert flags[flags.index("--caller-user-agent") + 1] == expected

    def test_caller_user_agent_not_built_when_blocked(self):
        # Blocked means the daemon never starts, so no flag list is ever
        # consumed; building one would be dead work.
        c = _bare_client()
        c._init_accelerator_config(explicit_credentials=True, client_options=None)
        assert c._accelerator_blocked_reason is not None
        assert c._accelerator_flags == []


class TestResolvePrincipal:
    def test_service_account_email(self):
        c = _bare_client()
        c._credentials = _FakeCreds(email="svc@proj.iam.gserviceaccount.com")
        assert c._resolve_principal() == "svc@proj.iam.gserviceaccount.com"

    def test_no_email_returns_none(self):
        c = _bare_client()
        c._credentials = _FakeCreds()  # e.g. plain gcloud user ADC
        assert c._resolve_principal() is None

    def test_default_email_returns_none(self):
        c = _bare_client()
        c._credentials = _FakeCreds(email="default")
        assert c._resolve_principal() is None

    def test_cached_across_calls(self):
        c = _bare_client()
        c._credentials = _FakeCreds(email="svc@proj.iam.gserviceaccount.com")
        assert c._resolve_principal() == "svc@proj.iam.gserviceaccount.com"
        # A later credential swap does not change the memoized principal.
        c._credentials = _FakeCreds(email="other@proj.iam.gserviceaccount.com")
        assert c._resolve_principal() == "svc@proj.iam.gserviceaccount.com"

    def test_compute_engine_refresh(self):
        # Compute Engine credentials only expose the email after a refresh
        # against the metadata server (email defaults to "default" until then).
        creds = compute_engine.Credentials()
        assert creds.service_account_email == "default"

        def fake_refresh(request):
            creds._service_account_email = "compute-sa@proj.iam.gserviceaccount.com"

        creds.refresh = fake_refresh
        c = _bare_client()
        c._credentials = creds
        assert c._resolve_principal() == "compute-sa@proj.iam.gserviceaccount.com"


# Matching scopes and credential type on both sides by default, so
# principal-focused tests exercise only the principal branch.
_SCOPES = ["https://www.googleapis.com/auth/bigtable.data"]
_CRED_TYPE = "service_account"

_CLIENT_MODS = [
    pytest.param(
        (
            _async_client_mod.BigtableDataClientAsync,
            _async_client_mod._DataApiTargetAsync,
            _async_client_mod._AcceleratorIdentityError,
            _async_client_mod._UNSET,
        ),
        id="async",
    ),
    pytest.param(
        (
            _sync_client_mod.BigtableDataClient,
            _sync_client_mod._DataApiTarget,
            _sync_client_mod._AcceleratorIdentityError,
            _sync_client_mod._UNSET,
        ),
        id="sync",
    ),
]


@pytest.mark.parametrize("client_mod", _CLIENT_MODS)
class TestResolveCredentialType:
    @pytest.mark.parametrize(
        ("cred_cls", "expected_type"),
        [
            (service_account.Credentials, "service_account"),
            (impersonated_credentials.Credentials, "impersonated_service_account"),
            (identity_pool.Credentials, "external_account"),
            (oauth2_credentials.Credentials, "authorized_user"),
            (
                external_account_authorized_user.Credentials,
                "external_account_authorized_user",
            ),
            (gdch_credentials.ServiceAccountCredentials, "gdch_service_account"),
            (compute_engine.Credentials, "gce_metadata"),
        ],
    )
    def test_known_credential_types(self, client_mod, cred_cls, expected_type):
        client_cls, _, _, unset = client_mod
        c = _bare_client(client_cls, unset)
        c._credentials = object.__new__(cred_cls)
        assert c._resolve_credential_type() == expected_type

    def test_none_and_unknown_credentials_return_none(self, client_mod):
        client_cls, _, _, unset = client_mod
        c = _bare_client(client_cls, unset)
        c._credentials = None
        assert c._resolve_credential_type() is None

        c2 = _bare_client(client_cls, unset)
        c2._credentials = _FakeCreds(email="svc@proj.iam.gserviceaccount.com")
        assert c2._resolve_credential_type() is None

    def test_cached_across_calls(self, client_mod):
        client_cls, _, _, unset = client_mod
        c = _bare_client(client_cls, unset)
        c._credentials = object.__new__(service_account.Credentials)
        assert c._resolve_credential_type() == "service_account"
        c._credentials = object.__new__(compute_engine.Credentials)
        assert c._resolve_credential_type() == "service_account"


class _FakeServer:
    _OMIT = object()

    def __init__(
        self,
        principal,
        cred_type=_CRED_TYPE,
        scopes=_SCOPES,
        missing=False,
        read_raises=None,
        raw_identity=_OMIT,
    ):
        self._principal = principal
        self._cred_type = cred_type
        self._scopes = scopes
        self._missing = missing
        self._read_raises = read_raises
        self._raw_identity = raw_identity

    def read_identity(self):
        if self._read_raises is not None:
            raise self._read_raises
        if self._raw_identity is not self._OMIT:
            return self._raw_identity
        if self._missing:
            return {}
        doc = {"principal": self._principal, "scopes": self._scopes}
        if self._cred_type is not self._OMIT:
            doc["type"] = self._cred_type
        return doc


def _verify(
    client_principal,
    daemon_principal,
    missing=False,
    client_type=_CRED_TYPE,
    daemon_type=_CRED_TYPE,
    client_scopes=_SCOPES,
    daemon_scopes=_SCOPES,
    raw_identity=_FakeServer._OMIT,
    target_cls=_DataApiTargetAsync,
):
    """Invoke the Table's verify helper against fake client/server doubles."""
    table = SimpleNamespace(
        client=SimpleNamespace(
            _resolve_principal=lambda: client_principal,
            _resolve_credential_type=lambda: client_type,
            _accelerator_scopes=client_scopes,
        )
    )
    server = _FakeServer(
        daemon_principal,
        cred_type=daemon_type,
        scopes=daemon_scopes,
        missing=missing,
        raw_identity=raw_identity,
    )
    target_cls._verify_daemon_identity(table, server)


@pytest.mark.parametrize("client_mod", _CLIENT_MODS)
class TestVerifyDaemonIdentity:
    def test_match_proceeds(self, client_mod):
        _, target_cls, _, _ = client_mod
        _verify(
            "svc@proj.iam.gserviceaccount.com",
            "svc@proj.iam.gserviceaccount.com",
            target_cls=target_cls,
        )

    def test_read_identity_error_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        table = SimpleNamespace(
            client=SimpleNamespace(
                _resolve_principal=lambda: "svc@proj.iam.gserviceaccount.com",
                _resolve_credential_type=lambda: _CRED_TYPE,
                _accelerator_scopes=_SCOPES,
            )
        )
        for exc in (RuntimeError("no identity.json"), ValueError("bad json")):
            server = _FakeServer(None, read_raises=exc)
            with pytest.raises(err_cls):
                target_cls._verify_daemon_identity(table, server)

    def test_non_dict_identity_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        for bad in (None, ["not", "a", "dict"], "string", 123):
            with pytest.raises(err_cls, match="expected a JSON object"):
                _verify(
                    "svc@proj.iam.gserviceaccount.com",
                    "svc@proj.iam.gserviceaccount.com",
                    raw_identity=bad,
                    target_cls=target_cls,
                )

    def test_mismatch_raises(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls, match="identity mismatch"):
            _verify(
                "svc-a@proj.iam.gserviceaccount.com",
                "svc-b@proj.iam.gserviceaccount.com",
                target_cls=target_cls,
            )

    def test_credential_type_mismatch_same_principal_raises(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls, match="credential type"):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                client_type="gce_metadata",
                daemon_type="service_account",
                target_cls=target_cls,
            )

    def test_daemon_missing_credential_type_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls, match="credential type is unknown on the daemon"):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                daemon_type=_FakeServer._OMIT,
                target_cls=target_cls,
            )

    def test_client_unknown_credential_type_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls, match="credential type is unknown on this client"):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                client_type=None,
                target_cls=target_cls,
            )

    def test_client_unknown_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls):
            _verify(None, "svc@proj.iam.gserviceaccount.com", target_cls=target_cls)

    def test_daemon_unknown_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls):
            _verify("svc@proj.iam.gserviceaccount.com", None, target_cls=target_cls)

    def test_daemon_missing_principal_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                None,
                missing=True,
                target_cls=target_cls,
            )

    def test_scope_match_ignores_order_and_dupes(self, client_mod):
        _, target_cls, _, _ = client_mod
        _verify(
            "svc@proj.iam.gserviceaccount.com",
            "svc@proj.iam.gserviceaccount.com",
            client_scopes=["scope-a", "scope-b"],
            daemon_scopes=["scope-b", "scope-a", "scope-a"],
            target_cls=target_cls,
        )

    def test_scope_string_and_non_iterable_handled(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        _verify(
            "svc@proj.iam.gserviceaccount.com",
            "svc@proj.iam.gserviceaccount.com",
            client_scopes="scope-a, scope-b",
            daemon_scopes="scope-b scope-a",
            target_cls=target_cls,
        )
        with pytest.raises(err_cls, match="effective scopes are unknown"):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                daemon_scopes=123,
                target_cls=target_cls,
            )

    def test_scope_mismatch_raises(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls, match="scope mismatch"):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                client_scopes=["https://www.googleapis.com/auth/bigtable.data"],
                daemon_scopes=["https://www.googleapis.com/auth/cloud-platform"],
                target_cls=target_cls,
            )

    def test_daemon_missing_scopes_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                daemon_scopes=[],
                target_cls=target_cls,
            )

    def test_client_missing_scopes_falls_back(self, client_mod):
        _, target_cls, err_cls, _ = client_mod
        with pytest.raises(err_cls):
            _verify(
                "svc@proj.iam.gserviceaccount.com",
                "svc@proj.iam.gserviceaccount.com",
                client_scopes=[],
                target_cls=target_cls,
            )
