# Copyright 2015 Google LLC
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

import io
import json
import unittest
from unittest import mock

from google.cloud.client import HAS_GOOGLE_AUTH_API_KEY


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.CredentialsWithQuotaProject)


class Test_ClientFactoryMixin(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.client import _ClientFactoryMixin

        return _ClientFactoryMixin

    def test_virtual(self):
        klass = self._get_target_class()
        self.assertFalse("__init__" in klass.__dict__)


class TestClient(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_unpickleable(self):
        import pickle

        credentials = _make_credentials()
        HTTP = object()

        client_obj = self._make_one(credentials=credentials, _http=HTTP)
        with self.assertRaises(pickle.PicklingError):
            pickle.dumps(client_obj)

    def test_ctor_defaults(self):
        credentials = _make_credentials()

        patch = mock.patch("google.auth.default", return_value=(credentials, None))
        with patch as default:
            client_obj = self._make_one()

        self.assertIs(client_obj._credentials, credentials)
        self.assertIsNone(client_obj._http_internal)
        default.assert_called_once_with(scopes=None)

    def test_ctor_explicit(self):
        credentials = _make_credentials()
        http = mock.sentinel.http
        client_obj = self._make_one(credentials=credentials, _http=http)

        self.assertIs(client_obj._credentials, credentials)
        self.assertIs(client_obj._http_internal, http)

    @unittest.skipIf(
        not HAS_GOOGLE_AUTH_API_KEY, "Auth library version does not support API keys"
    )
    def test_ctor_client_options_w_api_key(self):
        from google.auth.api_key import Credentials

        API_KEY = "my_api_key"

        client_options = {"api_key": API_KEY}
        client_obj = self._make_one(client_options=client_options)

        self.assertIsInstance(client_obj._credentials, Credentials)

    def test_ctor_client_options_w_conflicting_creds(self):
        from google.api_core.exceptions import DuplicateCredentialArgs

        credentials = _make_credentials()
        client_options = {"credentials_file": "/path/to/creds.json"}
        with self.assertRaises(DuplicateCredentialArgs):
            self._make_one(credentials=credentials, client_options=client_options)

    @unittest.skipIf(
        not HAS_GOOGLE_AUTH_API_KEY, "Auth library version does not support API keys"
    )
    def test_ctor_client_options_w_api_key_and_conflicting_creds(self):
        from google.api_core.exceptions import DuplicateCredentialArgs

        API_KEY = "my_api_key"

        credentials = _make_credentials()
        client_options = {"api_key": API_KEY}
        with self.assertRaises(DuplicateCredentialArgs):
            self._make_one(credentials=credentials, client_options=client_options)

    def test_ctor_bad_credentials(self):
        credentials = mock.sentinel.credentials

        with self.assertRaises(ValueError):
            self._make_one(credentials=credentials)

    def test_ctor_client_options_w_creds_file_scopes(self):
        credentials = _make_credentials()
        credentials_file = "/path/to/creds.json"
        scopes = ["SCOPE1", "SCOPE2"]
        client_options = {"credentials_file": credentials_file, "scopes": scopes}

        patch = mock.patch(
            "google.auth.load_credentials_from_file", return_value=(credentials, None)
        )
        with patch as load_credentials_from_file:
            client_obj = self._make_one(client_options=client_options)

        self.assertIs(client_obj._credentials, credentials)
        self.assertIsNone(client_obj._http_internal)
        load_credentials_from_file.assert_called_once_with(
            credentials_file, scopes=scopes
        )

    def test_ctor_client_options_w_quota_project(self):
        credentials = _make_credentials()
        quota_project_id = "quota-project-123"
        client_options = {"quota_project_id": quota_project_id}

        client_obj = self._make_one(
            credentials=credentials, client_options=client_options
        )

        self.assertIs(
            client_obj._credentials, credentials.with_quota_project.return_value
        )
        credentials.with_quota_project.assert_called_once_with(quota_project_id)

    def test_ctor__http_property_existing(self):
        credentials = _make_credentials()
        http = object()
        client = self._make_one(credentials=credentials, _http=http)
        self.assertIs(client._http_internal, http)
        self.assertIs(client._http, http)

    def test_ctor__http_property_new(self):
        from google.cloud.client import _CREDENTIALS_REFRESH_TIMEOUT

        credentials = _make_credentials()
        mock_client_cert_source = mock.Mock()
        client_options = {"client_cert_source": mock_client_cert_source}
        client = self._make_one(credentials=credentials, client_options=client_options)
        self.assertIsNone(client._http_internal)

        with mock.patch(
            "google.auth.transport.requests.AuthorizedSession"
        ) as AuthorizedSession:
            session = mock.Mock()
            session.configure_mtls_channel = mock.Mock()
            AuthorizedSession.return_value = session
            self.assertIs(client._http, session)
            # Check the mock.
            AuthorizedSession.assert_called_once_with(
                credentials, refresh_timeout=_CREDENTIALS_REFRESH_TIMEOUT
            )
            session.configure_mtls_channel.assert_called_once_with(
                mock_client_cert_source
            )
            # Make sure the cached value is used on subsequent access.
            self.assertIs(client._http_internal, session)
            self.assertIs(client._http, session)
            self.assertEqual(AuthorizedSession.call_count, 1)

    def test_from_service_account_info(self):
        klass = self._get_target_class()

        info = {"dummy": "value", "valid": "json"}
        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials.from_service_account_info",
            return_value=_make_credentials(),
        )

        with constructor_patch as constructor:
            client_obj = klass.from_service_account_info(info)

        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        constructor.assert_called_once_with(info)

    def test_from_service_account_info_w_explicit_credentials(self):
        KLASS = self._get_target_class()

        info = {"dummy": "value", "valid": "json"}

        with self.assertRaises(TypeError):
            KLASS.from_service_account_info(info, credentials=mock.sentinel.credentials)

    def test_from_service_account_json(self):
        from google.cloud import _helpers

        klass = self._get_target_class()

        info = {"dummy": "value", "valid": "json"}
        json_file = io.StringIO(_helpers._bytes_to_unicode(json.dumps(info)))

        file_open_patch = mock.patch("io.open", return_value=json_file)
        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials." "from_service_account_info",
            return_value=_make_credentials(),
        )

        with file_open_patch as file_open:
            with constructor_patch as constructor:
                client_obj = klass.from_service_account_json(mock.sentinel.filename)

        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        # Check that mocks were called as expected.
        file_open.assert_called_once_with(mock.sentinel.filename, "r", encoding="utf-8")
        constructor.assert_called_once_with(info)

    def test_close_w__http_internal_none(self):
        credentials = _make_credentials()
        client_obj = self._make_one(credentials=credentials, _http=None)

        client_obj.close()  # noraise

    def test_close_w__http_internal_set(self):
        credentials = _make_credentials()
        http = mock.Mock(spec=["close"])
        client_obj = self._make_one(credentials=credentials, _http=http)

        client_obj.close()

        http.close.assert_called_once_with()


class Test_ClientProjectMixin(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.client import _ClientProjectMixin

        return _ClientProjectMixin

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults_wo_envvar(self):
        environ = {}
        patch_env = mock.patch("os.environ", new=environ)
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=None,
        )
        with patch_env:
            with patch_default as patched:
                with self.assertRaises(EnvironmentError):
                    self._make_one()

        patched.assert_called_once_with(None)

    def test_ctor_defaults_w_envvar(self):
        from google.auth.environment_vars import PROJECT

        project = "some-project-123"
        environ = {PROJECT: project}
        patch_env = mock.patch("os.environ", new=environ)
        with patch_env:
            client = self._make_one()

        self.assertEqual(client.project, project)

    def test_ctor_defaults_w_legacy_envvar(self):
        from google.auth.environment_vars import LEGACY_PROJECT

        project = "some-project-123"
        environ = {LEGACY_PROJECT: project}
        patch_env = mock.patch("os.environ", new=environ)
        with patch_env:
            client = self._make_one()

        self.assertEqual(client.project, project)

    def test_ctor_w_explicit_project(self):
        explicit_project = "explicit-project-456"
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=None,
        )
        with patch_default as patched:
            client = self._make_one(project=explicit_project)

        self.assertEqual(client.project, explicit_project)

        patched.assert_not_called()

    def test_ctor_w_explicit_project_bytes(self):
        explicit_project = b"explicit-project-456"
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=None,
        )
        with patch_default as patched:
            client = self._make_one(project=explicit_project)

        self.assertEqual(client.project, explicit_project.decode("utf-8"))

        patched.assert_not_called()

    def test_ctor_w_explicit_project_invalid(self):
        explicit_project = object()
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=None,
        )
        with patch_default as patched:
            with self.assertRaises(ValueError):
                self._make_one(project=explicit_project)

        patched.assert_not_called()

    @staticmethod
    def _make_credentials(**kw):
        from google.auth.credentials import Credentials

        class _Credentials(Credentials):
            def __init__(self, **kw):
                self.__dict__.update(kw)

            def refresh(self):  # pragma: NO COVER
                pass

        return _Credentials(**kw)

    def test_ctor_w_explicit_credentials_wo_project(self):
        default_project = "default-project-123"
        credentials = self._make_credentials()
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=default_project,
        )
        with patch_default as patched:
            client = self._make_one(credentials=credentials)

        self.assertEqual(client.project, default_project)

        patched.assert_called_once_with(None)

    def test_ctor_w_explicit_credentials_w_project(self):
        project = "credentials-project-456"
        credentials = self._make_credentials(project_id=project)
        patch_default = mock.patch(
            "google.cloud.client._determine_default_project",
            return_value=None,
        )
        with patch_default as patched:
            client = self._make_one(credentials=credentials)

        self.assertEqual(client.project, project)

        patched.assert_not_called()


class TestClientWithProject(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.client import ClientWithProject

        return ClientWithProject

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor_defaults(self):
        credentials = _make_credentials()
        patch1 = mock.patch("google.auth.default", return_value=(credentials, None))

        project = "prahj-ekt"
        patch2 = mock.patch(
            "google.cloud.client._determine_default_project", return_value=project
        )

        with patch1 as default:
            with patch2 as _determine_default_project:
                client_obj = self._make_one()

        self.assertEqual(client_obj.project, project)
        self.assertIs(client_obj._credentials, credentials)
        self.assertIsNone(client_obj._http_internal)
        default.assert_called_once_with(scopes=None)
        _determine_default_project.assert_called_once_with(None)

    def test_constructor_missing_project(self):
        from google.cloud._testing import _Monkey
        from google.cloud import client

        FUNC_CALLS = []

        def mock_determine_proj(project):
            FUNC_CALLS.append((project, "_determine_default_project"))
            return None

        with _Monkey(client, _determine_default_project=mock_determine_proj):
            self.assertRaises(EnvironmentError, self._make_one)

        self.assertEqual(FUNC_CALLS, [(None, "_determine_default_project")])

    def test_constructor_w_invalid_project(self):
        CREDENTIALS = _make_credentials()
        HTTP = object()
        with self.assertRaises(ValueError):
            self._make_one(project=object(), credentials=CREDENTIALS, _http=HTTP)

    def _explicit_ctor_helper(self, project):
        CREDENTIALS = _make_credentials()
        HTTP = object()

        client_obj = self._make_one(
            project=project, credentials=CREDENTIALS, _http=HTTP
        )

        if isinstance(project, bytes):
            self.assertEqual(client_obj.project, project.decode("utf-8"))
        else:
            self.assertEqual(client_obj.project, project)
        self.assertIs(client_obj._credentials, CREDENTIALS)
        self.assertIs(client_obj._http_internal, HTTP)

    def test_constructor_explicit_bytes(self):
        PROJECT = b"PROJECT"
        self._explicit_ctor_helper(PROJECT)

    def test_constructor_explicit_text(self):
        PROJECT = "PROJECT"
        self._explicit_ctor_helper(PROJECT)

    def _from_service_account_info_helper(self, project=None):
        klass = self._get_target_class()

        default_project = "eye-d-of-project"
        info = {"dummy": "value", "valid": "json", "project_id": default_project}
        kwargs = {}

        if project is None:
            expected_project = default_project
        else:
            expected_project = project
            kwargs["project"] = project

        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials.from_service_account_info",
            return_value=_make_credentials(),
        )

        with constructor_patch as constructor:
            client_obj = klass.from_service_account_info(info, **kwargs)

        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(client_obj.project, expected_project)

        constructor.assert_called_once_with(info)

    def test_from_service_account_info(self):
        self._from_service_account_info_helper()

    def test_from_service_account_info_with_project(self):
        self._from_service_account_info_helper(project="prah-jekt")

    def test_from_service_account_info_with_posarg(self):
        class Derived(self._get_target_class()):
            def __init__(self, required, **kwargs):
                super(Derived, self).__init__(**kwargs)
                self.required = required

        project = "eye-d-of-project"
        info = {"dummy": "value", "valid": "json", "project_id": project}

        # Mock both the file opening and the credentials constructor.
        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials.from_service_account_info",
            return_value=_make_credentials(),
        )

        with constructor_patch as constructor:
            client_obj = Derived.from_service_account_info(info, "REQUIRED")

        self.assertIsInstance(client_obj, Derived)
        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(client_obj.project, project)
        self.assertEqual(client_obj.required, "REQUIRED")

        # Check that mocks were called as expected.
        constructor.assert_called_once_with(info)

    def _from_service_account_json_helper(self, project=None):
        from google.cloud import _helpers

        klass = self._get_target_class()

        default_project = "eye-d-of-project"
        info = {"dummy": "value", "valid": "json", "project_id": default_project}
        if project is None:
            expected_project = "eye-d-of-project"
        else:
            expected_project = project

        # Mock both the file opening and the credentials constructor.
        json_fi = io.StringIO(_helpers._bytes_to_unicode(json.dumps(info)))
        file_open_patch = mock.patch("io.open", return_value=json_fi)
        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials." "from_service_account_info",
            return_value=_make_credentials(),
        )

        with file_open_patch as file_open:
            with constructor_patch as constructor:
                kwargs = {}
                if project is not None:
                    kwargs["project"] = project
                client_obj = klass.from_service_account_json(
                    mock.sentinel.filename, **kwargs
                )

        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(client_obj.project, expected_project)
        # Check that mocks were called as expected.
        file_open.assert_called_once_with(mock.sentinel.filename, "r", encoding="utf-8")
        constructor.assert_called_once_with(info)

    def test_from_service_account_json(self):
        self._from_service_account_json_helper()

    def test_from_service_account_json_project_set(self):
        self._from_service_account_json_helper(project="prah-jekt")

    def test_from_service_account_json_with_posarg(self):
        from google.cloud import _helpers

        class Derived(self._get_target_class()):
            def __init__(self, required, **kwargs):
                super(Derived, self).__init__(**kwargs)
                self.required = required

        project = "eye-d-of-project"
        info = {"dummy": "value", "valid": "json", "project_id": project}

        # Mock both the file opening and the credentials constructor.
        json_fi = io.StringIO(_helpers._bytes_to_unicode(json.dumps(info)))
        file_open_patch = mock.patch("io.open", return_value=json_fi)
        constructor_patch = mock.patch(
            "google.oauth2.service_account.Credentials.from_service_account_info",
            return_value=_make_credentials(),
        )

        with file_open_patch as file_open:
            with constructor_patch as constructor:
                client_obj = Derived.from_service_account_json(
                    mock.sentinel.filename, "REQUIRED"
                )

        self.assertIsInstance(client_obj, Derived)
        self.assertIs(client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(client_obj.project, project)
        self.assertEqual(client_obj.required, "REQUIRED")

        # Check that mocks were called as expected.
        file_open.assert_called_once_with(mock.sentinel.filename, "r", encoding="utf-8")
        constructor.assert_called_once_with(info)
