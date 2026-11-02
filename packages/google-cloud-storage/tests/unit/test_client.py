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

import base64
import http.client
import io
import json
import re
import unittest
import urllib
from unittest.mock import patch

import mock
import pytest
import requests
from google.api_core import exceptions
from google.auth.credentials import AnonymousCredentials
from google.oauth2.service_account import Credentials

from google.cloud.storage import _helpers
from google.cloud.storage._helpers import (
    _API_ENDPOINT_OVERRIDE_ENV_VAR,
    _DEFAULT_UNIVERSE_DOMAIN,
    _NOW,
    _UTC,
    STORAGE_EMULATOR_ENV_VAR,
    _get_default_headers,
)
from google.cloud.storage._http import Connection
from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
)
from tests.unit.test__helpers import GCCL_INVOCATION_TEST_CONST

from . import _read_local_json

_SERVICE_ACCOUNT_JSON = _read_local_json("url_signer_v4_test_account.json")
_CONFORMANCE_TESTS = _read_local_json("url_signer_v4_test_data.json")[
    "postPolicyV4Tests"
]
_POST_POLICY_TESTS = [test for test in _CONFORMANCE_TESTS if "policyInput" in test]
_FAKE_CREDENTIALS = Credentials.from_service_account_info(_SERVICE_ACCOUNT_JSON)


def _make_credentials(project=None, universe_domain=_DEFAULT_UNIVERSE_DOMAIN):
    import google.auth.credentials

    if project is not None:
        return mock.Mock(
            spec=google.auth.credentials.Credentials,
            project_id=project,
            universe_domain=universe_domain,
        )

    return mock.Mock(
        spec=google.auth.credentials.Credentials, universe_domain=universe_domain
    )


def _create_signing_credentials():
    import google.auth.credentials

    class _SigningCredentials(
        google.auth.credentials.Credentials, google.auth.credentials.Signing
    ):
        pass

    credentials = mock.Mock(
        spec=_SigningCredentials, universe_domain=_DEFAULT_UNIVERSE_DOMAIN
    )
    credentials.sign_bytes = mock.Mock(return_value=b"Signature_bytes")
    credentials.signer_email = "test@mail.com"
    return credentials


def _make_connection(*responses):
    from google.cloud.exceptions import NotFound

    import google.cloud.storage._http

    mock_conn = mock.create_autospec(google.cloud.storage._http.Connection)
    mock_conn.user_agent = "testing 1.2.3"
    mock_conn.api_request.side_effect = list(responses) + [NotFound("miss")]
    return mock_conn


def _make_response(status=http.client.OK, content=b"", headers={}):
    response = requests.Response()
    response.status_code = status
    response._content = content
    response.headers = headers
    response.request = requests.Request()
    return response


def _make_json_response(data, status=http.client.OK, headers=None):
    headers = headers or {}
    headers["Content-Type"] = "application/json"
    return _make_response(
        status=status, content=json.dumps(data).encode("utf-8"), headers=headers
    )


def _make_requests_session(responses):
    session = mock.create_autospec(requests.Session, instance=True)
    session.request.side_effect = responses
    session.is_mtls = False
    return session


class TestClient(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.client import Client

        return Client

    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_connection_type(self):
        from google.cloud._http import ClientInfo

        PROJECT = "PROJECT"
        credentials = _make_credentials()

        client = self._make_one(project=PROJECT, credentials=credentials)

        self.assertEqual(client.project, PROJECT)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, credentials)
        self.assertIsNone(client.current_batch)
        self.assertEqual(list(client._batch_stack), [])
        self.assertIsInstance(client._connection._client_info, ClientInfo)
        self.assertEqual(
            client._connection.API_BASE_URL, Connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_empty_client_options(self):
        from google.api_core.client_options import ClientOptions

        PROJECT = "PROJECT"
        credentials = _make_credentials()
        client_options = ClientOptions()

        client = self._make_one(
            project=PROJECT, credentials=credentials, client_options=client_options
        )

        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_client_options_dict(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials()
        api_endpoint = "https://www.foo-googleapis.com"
        client_options = {"api_endpoint": api_endpoint}

        client = self._make_one(
            project=PROJECT, credentials=credentials, client_options=client_options
        )

        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)
        self.assertEqual(client.api_endpoint, api_endpoint)

    def test_ctor_w_client_options_object(self):
        from google.api_core.client_options import ClientOptions

        PROJECT = "PROJECT"
        credentials = _make_credentials()
        api_endpoint = "https://www.foo-googleapis.com"
        client_options = ClientOptions(api_endpoint=api_endpoint)

        client = self._make_one(
            project=PROJECT, credentials=credentials, client_options=client_options
        )

        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)
        self.assertEqual(client.api_endpoint, api_endpoint)

    def test_ctor_w_api_key(self):
        from google.auth.api_key import Credentials

        PROJECT = "PROJECT"
        api_key = "my_api_key"

        client = self._make_one(project=PROJECT, api_key=api_key)

        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )
        self.assertIsInstance(client._credentials, Credentials)
        self.assertEqual(client._credentials.token, api_key)

    def test_ctor_w_api_key_and_client_options(self):
        from google.api_core.client_options import ClientOptions
        from google.auth.api_key import Credentials

        PROJECT = "PROJECT"
        api_key = "my_api_key"
        api_endpoint = "https://www.foo-googleapis.com"
        client_options = ClientOptions(api_endpoint=api_endpoint)

        client = self._make_one(
            project=PROJECT, client_options=client_options, api_key=api_key
        )

        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)
        self.assertIsInstance(client._credentials, Credentials)
        self.assertEqual(client._credentials.token, api_key)

    def test_ctor_w_api_key_and_client_dict(self):
        from google.auth.api_key import Credentials

        PROJECT = "PROJECT"
        api_key = "my_api_key"
        api_endpoint = "https://www.foo-googleapis.com"
        client_options = {"api_endpoint": api_endpoint}

        client = self._make_one(
            project=PROJECT, client_options=client_options, api_key=api_key
        )

        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)
        self.assertIsInstance(client._credentials, Credentials)
        self.assertEqual(client._credentials.token, api_key)

    def test_ctor_w_universe_domain_and_matched_credentials(self):
        PROJECT = "PROJECT"
        universe_domain = "example.com"
        expected_api_endpoint = f"https://storage.{universe_domain}"
        credentials = _make_credentials(universe_domain=universe_domain)
        client_options = {"universe_domain": universe_domain}

        client = self._make_one(
            project=PROJECT, credentials=credentials, client_options=client_options
        )

        self.assertEqual(client._connection.API_BASE_URL, expected_api_endpoint)
        self.assertEqual(client.api_endpoint, expected_api_endpoint)
        self.assertEqual(client.universe_domain, universe_domain)

    def test_ctor_w_enable_metrics(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(
            project=PROJECT, credentials=credentials, enable_metrics=True
        )
        self.assertTrue(client._enable_metrics)

    def test_ctor_w_enable_debug_metrics(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(
            project=PROJECT, credentials=credentials, enable_debug_metrics=True
        )
        self.assertTrue(client._enable_debug_metrics)

    def test_ctor_w_invalid_enable_metrics_raises_type_error(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials()
        with self.assertRaises(TypeError):
            self._make_one(
                project=PROJECT, credentials=credentials, enable_metrics="true"
            )
        with self.assertRaises(TypeError):
            self._make_one(
                project=PROJECT,
                credentials=credentials,
                enable_debug_metrics="true",
            )

    def test_client_metrics_enabled_property(self):
        from google.cloud.storage import _opentelemetry_metrics

        PROJECT = "PROJECT"
        credentials = _make_credentials()

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            client = self._make_one(
                project=PROJECT, credentials=credentials, enable_metrics=True
            )
            self.assertTrue(client.metrics_enabled)

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=False,
        ):
            client = self._make_one(
                project=PROJECT, credentials=credentials, enable_metrics=True
            )
            self.assertFalse(client.metrics_enabled)

    def test_client_debug_metrics_enabled_property(self):
        from google.cloud.storage import _opentelemetry_metrics

        PROJECT = "PROJECT"
        credentials = _make_credentials()

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            client = self._make_one(
                project=PROJECT,
                credentials=credentials,
                enable_metrics=True,
                enable_debug_metrics=True,
            )
            self.assertTrue(client.debug_metrics_enabled)

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=False,
        ):
            client = self._make_one(
                project=PROJECT,
                credentials=credentials,
                enable_metrics=True,
                enable_debug_metrics=True,
            )
            self.assertFalse(client.debug_metrics_enabled)

        # Verify that debug metrics are independent when base metrics are disabled
        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            client_disabled_base = self._make_one(
                project=PROJECT,
                credentials=credentials,
                enable_metrics=False,
                enable_debug_metrics=True,
            )
            self.assertFalse(client_disabled_base.metrics_enabled)
            self.assertTrue(client_disabled_base.debug_metrics_enabled)

    def test_ctor_metrics_defaults_and_env_fallback(self):
        from google.cloud.storage import _opentelemetry_metrics

        PROJECT = "PROJECT"
        credentials = _make_credentials()

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            with mock.patch.dict("os.environ", {}, clear=True):
                client = self._make_one(project=PROJECT, credentials=credentials)
                self.assertIsNone(client._enable_metrics)
                self.assertIsNone(client._enable_debug_metrics)
                self.assertFalse(client.metrics_enabled)
                self.assertFalse(client.debug_metrics_enabled)

            with mock.patch.dict(
                "os.environ",
                {
                    "GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS": "true",
                    "GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS": "true",
                },
                clear=True,
            ):
                client = self._make_one(project=PROJECT, credentials=credentials)
                self.assertTrue(client.metrics_enabled)
                self.assertTrue(client.debug_metrics_enabled)

    def test_ctor_w_universe_domain_and_mismatched_credentials(self):
        PROJECT = "PROJECT"
        universe_domain = "example.com"
        credentials = _make_credentials()  # default universe domain
        client_options = {"universe_domain": universe_domain}

        with self.assertRaises(ValueError):
            self._make_one(
                project=PROJECT, credentials=credentials, client_options=client_options
            )

    def test_ctor_w_universe_domain_and_mtls(self):
        PROJECT = "PROJECT"
        universe_domain = "example.com"
        client_options = {"universe_domain": universe_domain}

        credentials = _make_credentials(
            project=PROJECT, universe_domain=universe_domain
        )

        environ = {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}
        with mock.patch("os.environ", environ):
            with self.assertRaises(ValueError):
                self._make_one(credentials=credentials, client_options=client_options)

    def test_ctor_w_custom_headers(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials()
        custom_headers = {"x-goog-custom-audit-foo": "bar"}
        client = self._make_one(
            project=PROJECT, credentials=credentials, extra_headers=custom_headers
        )
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )
        self.assertEqual(client._connection.extra_headers, custom_headers)

    def test_ctor_wo_project(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials(project=PROJECT)

        with mock.patch.dict("os.environ", {}, clear=True):
            client = self._make_one(credentials=credentials)

        self.assertEqual(client.project, PROJECT)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, credentials)
        self.assertIsNone(client.current_batch)
        self.assertEqual(list(client._batch_stack), [])

    def test_ctor_w_project_explicit_none(self):
        credentials = _make_credentials()

        client = self._make_one(project=None, credentials=credentials)

        self.assertIsNone(client.project)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, credentials)
        self.assertIsNone(client.current_batch)
        self.assertEqual(list(client._batch_stack), [])

    def test_ctor_w_client_info(self):
        from google.cloud._http import ClientInfo

        credentials = _make_credentials()
        client_info = ClientInfo()

        client = self._make_one(
            project=None, credentials=credentials, client_info=client_info
        )

        self.assertIsNone(client.project)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, credentials)
        self.assertIsNone(client.current_batch)
        self.assertEqual(list(client._batch_stack), [])
        self.assertIs(client._connection._client_info, client_info)

    def test_ctor_mtls(self):
        PROJECT = "PROJECT"
        credentials = _make_credentials(project=PROJECT)

        client = self._make_one(credentials=credentials)
        self.assertEqual(client._connection.ALLOW_AUTO_SWITCH_TO_MTLS_URL, True)
        self.assertEqual(
            client._connection.API_BASE_URL, "https://storage.googleapis.com"
        )

        client = self._make_one(
            credentials=credentials, client_options={"api_endpoint": "http://foo"}
        )
        self.assertEqual(client._connection.ALLOW_AUTO_SWITCH_TO_MTLS_URL, False)
        self.assertEqual(client._connection.API_BASE_URL, "http://foo")

    def test_ctor_w_custom_endpoint_use_auth(self):
        custom_endpoint = "storage-example.p.googleapis.com"
        credentials = _make_credentials()
        client = self._make_one(
            project="project",
            credentials=credentials,
            client_options={"api_endpoint": custom_endpoint},
        )
        self.assertEqual(client._connection.API_BASE_URL, custom_endpoint)
        self.assertIsNotNone(client.project)
        self.assertIsInstance(client._connection, Connection)
        self.assertIsNotNone(client._connection.credentials)
        self.assertNotIsInstance(client._connection.credentials, AnonymousCredentials)

    def test_ctor_w_custom_endpoint_bypass_auth(self):
        custom_endpoint = "storage-example.p.googleapis.com"
        with mock.patch.dict("os.environ", {}, clear=True):
            client = self._make_one(
                client_options={"api_endpoint": custom_endpoint},
                use_auth_w_custom_endpoint=False,
            )
        self.assertEqual(client._connection.API_BASE_URL, custom_endpoint)
        self.assertEqual(client.project, None)
        self.assertIsInstance(client._connection, Connection)
        self.assertIsInstance(client._connection.credentials, AnonymousCredentials)

    def test_ctor_w_custom_endpoint_w_credentials(self):
        PROJECT = "PROJECT"
        custom_endpoint = "storage-example.p.googleapis.com"
        credentials = _make_credentials(project=PROJECT)
        with mock.patch.dict("os.environ", {}, clear=True):
            client = self._make_one(
                credentials=credentials,
                client_options={"api_endpoint": custom_endpoint},
            )
        self.assertEqual(client._connection.API_BASE_URL, custom_endpoint)
        self.assertEqual(client.project, PROJECT)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, credentials)

    def test_ctor_w_emulator_wo_project(self):
        # bypasses authentication if STORAGE_EMULATOR_ENV_VAR is set
        host = "http://localhost:8080"
        environ = {STORAGE_EMULATOR_ENV_VAR: host}
        with mock.patch("os.environ", environ):
            client = self._make_one()

        self.assertIsNone(client.project)
        self.assertEqual(client._connection.API_BASE_URL, host)
        self.assertIsInstance(client._connection.credentials, AnonymousCredentials)

    def test_ctor_w_emulator_w_environ_project(self):
        # bypasses authentication and infers the project from the environment
        host = "http://localhost:8080"
        environ_project = "environ-project"
        environ = {
            STORAGE_EMULATOR_ENV_VAR: host,
            "GOOGLE_CLOUD_PROJECT": environ_project,
        }
        with mock.patch("os.environ", environ):
            client = self._make_one()

        self.assertEqual(client.project, environ_project)
        self.assertEqual(client._connection.API_BASE_URL, host)
        self.assertIsInstance(client._connection.credentials, AnonymousCredentials)

    def test_ctor_w_emulator_w_project_arg(self):
        # project argument overrides project set in the enviroment
        host = "http://localhost:8080"
        environ_project = "environ-project"
        project = "my-test-project"
        environ = {
            STORAGE_EMULATOR_ENV_VAR: host,
            "GOOGLE_CLOUD_PROJECT": environ_project,
        }
        with mock.patch("os.environ", environ):
            client = self._make_one(project=project)

        self.assertEqual(client.project, project)
        self.assertEqual(client._connection.API_BASE_URL, host)
        self.assertIsInstance(client._connection.credentials, AnonymousCredentials)

    def test_ctor_w_emulator_w_credentials(self):
        host = "http://localhost:8080"
        environ = {STORAGE_EMULATOR_ENV_VAR: host}
        credentials = _make_credentials()
        with mock.patch("os.environ", environ):
            client = self._make_one(credentials=credentials)

        self.assertEqual(client._connection.API_BASE_URL, host)
        self.assertIs(client._connection.credentials, credentials)

    def test_ctor_w_api_endpoint_override(self):
        host = "http://localhost:8080"
        environ = {_API_ENDPOINT_OVERRIDE_ENV_VAR: host}
        project = "my-test-project"
        credentials = _make_credentials()
        with mock.patch("os.environ", environ):
            client = self._make_one(project=project, credentials=credentials)

        self.assertEqual(client.project, project)
        self.assertEqual(client._connection.API_BASE_URL, host)

    def test_create_anonymous_client(self):
        klass = self._get_target_class()
        client = klass.create_anonymous_client()

        self.assertIsNone(client.project)
        self.assertIsInstance(client._connection, Connection)
        self.assertIsInstance(client._connection.credentials, AnonymousCredentials)

    def test__push_batch_and__pop_batch(self):
        from google.cloud.storage.batch import Batch

        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        batch1 = Batch(client)
        batch2 = Batch(client)
        client._push_batch(batch1)
        self.assertEqual(list(client._batch_stack), [batch1])
        self.assertIs(client.current_batch, batch1)
        client._push_batch(batch2)
        self.assertIs(client.current_batch, batch2)
        # list(_LocalStack) returns in reverse order.
        self.assertEqual(list(client._batch_stack), [batch2, batch1])
        self.assertIs(client._pop_batch(), batch2)
        self.assertEqual(list(client._batch_stack), [batch1])
        self.assertIs(client._pop_batch(), batch1)
        self.assertEqual(list(client._batch_stack), [])

    def test__connection_setter(self):
        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        client._base_connection = None  # Unset the value from the constructor
        client._connection = connection = object()
        self.assertIs(client._base_connection, connection)

    def test__connection_setter_when_set(self):
        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        self.assertRaises(ValueError, setattr, client, "_connection", None)

    def test__connection_getter_no_batch(self):
        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        self.assertIs(client._connection, client._base_connection)
        self.assertIsNone(client.current_batch)

    def test__connection_getter_with_batch(self):
        from google.cloud.storage.batch import Batch

        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        batch = Batch(client)
        client._push_batch(batch)
        self.assertIsNot(client._connection, client._base_connection)
        self.assertIs(client._connection, batch)
        self.assertIs(client.current_batch, batch)

    def test_get_service_account_email_wo_project(self):
        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        EMAIL = "storage-user-123@example.com"
        RESOURCE = {"kind": "storage#serviceAccount", "email_address": EMAIL}

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        http = _make_requests_session([_make_json_response(RESOURCE)])
        client._http_internal = http

        service_account_email = client.get_service_account_email(timeout=42)

        self.assertEqual(service_account_email, EMAIL)
        http.request.assert_called_once_with(
            method="GET", url=mock.ANY, data=None, headers=mock.ANY, timeout=42
        )
        _, kwargs = http.request.call_args
        scheme, netloc, path, qs, _ = urllib.parse.urlsplit(kwargs.get("url"))
        self.assertEqual(f"{scheme}://{netloc}", client._connection.API_BASE_URL)
        self.assertEqual(
            path,
            "/".join(
                [
                    "",
                    "storage",
                    client._connection.API_VERSION,
                    "projects",
                    PROJECT,
                    "serviceAccount",
                ]
            ),
        )

    def test_get_service_account_email_w_project(self):
        PROJECT = "PROJECT"
        OTHER_PROJECT = "OTHER_PROJECT"
        CREDENTIALS = _make_credentials()
        EMAIL = "storage-user-123@example.com"
        RESOURCE = {"kind": "storage#serviceAccount", "email_address": EMAIL}

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        http = _make_requests_session([_make_json_response(RESOURCE)])
        client._http_internal = http

        service_account_email = client.get_service_account_email(project=OTHER_PROJECT)

        self.assertEqual(service_account_email, EMAIL)
        http.request.assert_called_once_with(
            method="GET",
            url=mock.ANY,
            data=None,
            headers=mock.ANY,
            timeout=self._get_default_timeout(),
        )
        _, kwargs = http.request.call_args
        scheme, netloc, path, qs, _ = urllib.parse.urlsplit(kwargs.get("url"))
        self.assertEqual(f"{scheme}://{netloc}", client._connection.API_BASE_URL)
        self.assertEqual(
            path,
            "/".join(
                [
                    "",
                    "storage",
                    client._connection.API_VERSION,
                    "projects",
                    OTHER_PROJECT,
                    "serviceAccount",
                ]
            ),
        )

    def test_bucket(self):
        from google.cloud.storage.bucket import Bucket

        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()
        BUCKET_NAME = "BUCKET_NAME"
        GENERATION = 12345

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        bucket = client.bucket(BUCKET_NAME, generation=GENERATION)
        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, client)
        self.assertEqual(bucket.name, BUCKET_NAME)
        self.assertIsNone(bucket.user_project)
        self.assertEqual(bucket.generation, GENERATION)

    def test_bucket_w_user_project(self):
        from google.cloud.storage.bucket import Bucket

        PROJECT = "PROJECT"
        USER_PROJECT = "USER_PROJECT"
        CREDENTIALS = _make_credentials()
        BUCKET_NAME = "BUCKET_NAME"

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        bucket = client.bucket(BUCKET_NAME, user_project=USER_PROJECT)
        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, client)
        self.assertEqual(bucket.name, BUCKET_NAME)
        self.assertEqual(bucket.user_project, USER_PROJECT)

    def test_batch(self):
        from google.cloud.storage.batch import Batch

        PROJECT = "PROJECT"
        CREDENTIALS = _make_credentials()

        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)
        batch = client.batch()
        self.assertIsInstance(batch, Batch)
        self.assertIs(batch._client, client)

    def test__get_resource_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "PROJECT"
        path = "/path/to/something"
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()

        with self.assertRaises(NotFound):
            client._get_resource(path)

        connection.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params=None,
            headers=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test__get_resource_hit_w_explicit(self):
        project = "PROJECT"
        path = "/path/to/something"
        query_params = {"foo": "Foo"}
        headers = {"bar": "Bar"}
        timeout = 100
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        expected = mock.Mock(spec={})
        connection = client._base_connection = _make_connection(expected)
        target = mock.Mock(spec={})

        found = client._get_resource(
            path,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

        self.assertIs(found, expected)

        connection.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

    def test__list_resource_w_defaults(self):
        import functools

        from google.api_core.page_iterator import HTTPIterator, _do_nothing_page_start

        project = "PROJECT"
        path = "/path/to/list/resource"
        item_to_value = mock.Mock(spec=[])
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()
        connection.build_api_url = mock.Mock(return_value="http://example.com" + path)

        iterator = client._list_resource(
            path=path,
            item_to_value=item_to_value,
        )

        self.assertIsInstance(iterator, HTTPIterator)
        self.assertIs(iterator.client, client)
        self.assertIsInstance(iterator.api_request, functools.partial)
        self.assertIs(iterator.api_request.func, connection.api_request)
        self.assertEqual(iterator.api_request.args, ())
        expected_keywords = {
            "timeout": self._get_default_timeout(),
            "retry": DEFAULT_RETRY,
        }
        self.assertEqual(iterator.api_request.keywords, expected_keywords)
        self.assertEqual(iterator.path, path)
        self.assertEqual(iterator.next_page_token, None)
        self.assertEqual(iterator.max_results, None)
        self.assertIs(iterator._page_start, _do_nothing_page_start)

    def test__list_resource_w_explicit(self):
        import functools

        from google.api_core.page_iterator import HTTPIterator

        project = "PROJECT"
        path = "/path/to/list/resource"
        item_to_value = mock.Mock(spec=[])
        page_token = "PAGE-TOKEN"
        max_results = 47
        extra_params = {"foo": "Foo"}
        page_start = mock.Mock(spec=[])
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()
        connection.build_api_url = mock.Mock(return_value="http://example.com" + path)

        iterator = client._list_resource(
            path=path,
            item_to_value=item_to_value,
            page_token=page_token,
            max_results=max_results,
            extra_params=extra_params,
            page_start=page_start,
        )

        self.assertIsInstance(iterator, HTTPIterator)
        self.assertIs(iterator.client, client)
        self.assertIsInstance(iterator.api_request, functools.partial)
        self.assertIs(iterator.api_request.func, connection.api_request)
        self.assertEqual(iterator.api_request.args, ())
        expected_keywords = {
            "timeout": self._get_default_timeout(),
            "retry": DEFAULT_RETRY,
        }
        self.assertEqual(iterator.api_request.keywords, expected_keywords)
        self.assertEqual(iterator.path, path)
        self.assertEqual(iterator.next_page_token, page_token)
        self.assertEqual(iterator.max_results, max_results)
        self.assertIs(iterator._page_start, page_start)

    def test__patch_resource_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "PROJECT"
        path = "/path/to/something"
        credentials = _make_credentials()
        data = {"baz": "Baz"}

        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()

        with self.assertRaises(NotFound):
            client._patch_resource(path, data)

        connection.api_request.assert_called_once_with(
            method="PATCH",
            path=path,
            data=data,
            query_params=None,
            headers=None,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test__patch_resource_hit_w_explicit(self):
        project = "PROJECT"
        path = "/path/to/something"
        data = {"baz": "Baz"}
        query_params = {"foo": "Foo"}
        headers = {"bar": "Bar"}
        timeout = 100
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        expected = mock.Mock(spec={})
        connection = client._base_connection = _make_connection(expected)
        target = mock.Mock(spec={})

        found = client._patch_resource(
            path,
            data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

        self.assertIs(found, expected)

        connection.api_request.assert_called_once_with(
            method="PATCH",
            path=path,
            data=data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

    def test__put_resource_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "PROJECT"
        path = "/path/to/something"
        credentials = _make_credentials()
        data = {"baz": "Baz"}

        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()

        with self.assertRaises(NotFound):
            client._put_resource(path, data)

        connection.api_request.assert_called_once_with(
            method="PUT",
            path=path,
            data=data,
            query_params=None,
            headers=None,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test__put_resource_hit_w_explicit(self):
        project = "PROJECT"
        path = "/path/to/something"
        data = {"baz": "Baz"}
        query_params = {"foo": "Foo"}
        headers = {"bar": "Bar"}
        timeout = 100
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        expected = mock.Mock(spec={})
        connection = client._base_connection = _make_connection(expected)
        target = mock.Mock(spec={})

        found = client._put_resource(
            path,
            data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

        self.assertIs(found, expected)

        connection.api_request.assert_called_once_with(
            method="PUT",
            path=path,
            data=data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

    def test__post_resource_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "PROJECT"
        path = "/path/to/something"
        credentials = _make_credentials()
        data = {"baz": "Baz"}

        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()

        with self.assertRaises(NotFound):
            client._post_resource(path, data)

        connection.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data=data,
            query_params=None,
            headers=None,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test__post_resource_hit_w_explicit(self):
        project = "PROJECT"
        path = "/path/to/something"
        data = {"baz": "Baz"}
        query_params = {"foo": "Foo"}
        headers = {"bar": "Bar"}
        timeout = 100
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        expected = mock.Mock(spec={})
        connection = client._base_connection = _make_connection(expected)
        target = mock.Mock(spec={})

        found = client._post_resource(
            path,
            data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

        self.assertIs(found, expected)

        connection.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data=data,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

    def test__delete_resource_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "PROJECT"
        path = "/path/to/something"
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        connection = client._base_connection = _make_connection()

        with self.assertRaises(NotFound):
            client._delete_resource(path)

        connection.api_request.assert_called_once_with(
            method="DELETE",
            path=path,
            query_params=None,
            headers=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test__delete_resource_hit_w_explicit(self):
        project = "PROJECT"
        path = "/path/to/something"
        query_params = {"foo": "Foo"}
        headers = {"bar": "Bar"}
        timeout = 100
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()

        client = self._make_one(project=project, credentials=credentials)
        expected = mock.Mock(spec={})
        connection = client._base_connection = _make_connection(expected)
        target = mock.Mock(spec={})

        found = client._delete_resource(
            path,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

        self.assertIs(found, expected)

        connection.api_request.assert_called_once_with(
            method="DELETE",
            path=path,
            query_params=query_params,
            headers=headers,
            timeout=timeout,
            retry=retry,
            _target_object=target,
        )

    def test__bucket_arg_to_bucket_w_bucket_w_client(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        other_client = mock.Mock(spec=[])
        bucket_name = "w_client"

        bucket = Bucket(other_client, name=bucket_name)

        found = client._bucket_arg_to_bucket(bucket)

        self.assertIs(found, bucket)
        self.assertIs(found.client, other_client)

    def test__bucket_arg_to_bucket_raises_on_generation(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        other_client = mock.Mock(spec=[])
        bucket_name = "w_client"

        bucket = Bucket(other_client, name=bucket_name)

        with self.assertRaises(ValueError):
            client._bucket_arg_to_bucket(bucket, generation=12345)

    def test__bucket_arg_to_bucket_w_bucket_wo_client(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        bucket_name = "wo_client"

        bucket = Bucket(client=None, name=bucket_name)

        found = client._bucket_arg_to_bucket(bucket)

        self.assertIs(found, bucket)
        self.assertIs(found.client, client)

    def test__bucket_arg_to_bucket_w_bucket_name(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        generation = 12345
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        bucket_name = "string-name"

        found = client._bucket_arg_to_bucket(bucket_name, generation)

        self.assertIsInstance(found, Bucket)
        self.assertEqual(found.name, bucket_name)
        self.assertEqual(found.generation, generation)
        self.assertIs(found.client, client)

    def test_get_bucket_miss_w_string_w_defaults(self):
        from google.cloud.exceptions import NotFound

        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock()
        client._get_resource.side_effect = NotFound("testing")
        bucket_name = "nonesuch"

        with self.assertRaises(NotFound):
            client.get_bucket(bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

        target = client._get_resource.call_args[1]["_target_object"]
        self.assertIsInstance(target, Bucket)
        self.assertEqual(target.name, bucket_name)

    def test_get_bucket_forbidden_sync_cache_fallback(self):
        from google.api_core.exceptions import Forbidden

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock()
        client._get_resource.side_effect = Forbidden("forbidden")
        bucket_name = "forbidden-bucket"

        # Ensure cache is clear
        client._bucket_metadata_cache.clear()

        with self.assertRaises(Forbidden):
            client.get_bucket(bucket_name)

        # Assert cache was synchronously populated with fallback
        cached = client._bucket_metadata_cache.get(bucket_name)
        self.assertIsNotNone(cached)
        dest_id, loc = cached
        self.assertEqual(
            dest_id, f"//storage.googleapis.com/projects/_/buckets/{bucket_name}"
        )
        self.assertEqual(loc, "global")

    def test_get_bucket_hit_w_string_w_timeout(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        timeout = 42
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)

        bucket = client.get_bucket(bucket_name, timeout=timeout)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_get_bucket_hit_w_string_w_soft_deleted(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        generation = 12345
        api_response = {"name": bucket_name, "generation": generation}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)

        bucket = client.get_bucket(
            bucket_name, generation=generation, soft_deleted=True
        )

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)
        self.assertEqual(bucket.generation, generation)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {
            "generation": generation,
            "projection": "noAcl",
            "softDeleted": True,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=60,
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_get_bucket_hit_w_string_w_metageneration_match(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        metageneration_number = 6
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)

        bucket = client.get_bucket(
            bucket_name, if_metageneration_match=metageneration_number
        )

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {
            "projection": "noAcl",
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_get_bucket_miss_w_object_w_retry(self):
        from google.cloud.exceptions import NotFound

        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "nonesuch"
        retry = mock.Mock(spec=[])
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(side_effect=NotFound("testing"))
        bucket_obj = Bucket(client, bucket_name)

        with self.assertRaises(NotFound):
            client.get_bucket(bucket_obj, retry=retry)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=mock.ANY,
        )

        target = client._get_resource.call_args[1]["_target_object"]
        self.assertIsInstance(target, Bucket)
        self.assertEqual(target.name, bucket_name)

    def test_get_bucket_hit_w_object_defaults(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)
        bucket_obj = Bucket(client, bucket_name)

        bucket = client.get_bucket(bucket_obj)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_get_bucket_hit_w_object_w_retry_none(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)
        bucket_obj = Bucket(client, bucket_name)

        bucket = client.get_bucket(bucket_obj, retry=None)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=bucket,
        )

    def test_lookup_bucket_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "nonesuch"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(side_effect=NotFound("testing"))

        bucket = client.lookup_bucket(bucket_name)

        self.assertIsNone(bucket)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

        target = client._get_resource.call_args[1]["_target_object"]
        self.assertIsInstance(target, Bucket)
        self.assertEqual(target.name, bucket_name)

    def test_lookup_bucket_forbidden_sync_cache_fallback(self):
        from google.api_core.exceptions import Forbidden

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(side_effect=Forbidden("forbidden"))
        bucket_name = "forbidden-bucket"

        # Ensure cache is clear
        client._bucket_metadata_cache.clear()

        with self.assertRaises(Forbidden):
            client.lookup_bucket(bucket_name)

        # Assert cache was synchronously populated with fallback
        cached = client._bucket_metadata_cache.get(bucket_name)
        self.assertIsNotNone(cached)
        dest_id, loc = cached
        self.assertEqual(
            dest_id, f"//storage.googleapis.com/projects/_/buckets/{bucket_name}"
        )
        self.assertEqual(loc, "global")

    def test_lookup_bucket_hit_w_timeout(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        timeout = 42
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)

        bucket = client.lookup_bucket(bucket_name, timeout=timeout)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_lookup_bucket_hit_w_metageneration_match(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        metageneration_number = 6
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)

        bucket = client.lookup_bucket(
            bucket_name, if_metageneration_match=metageneration_number
        )

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {
            "projection": "noAcl",
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_lookup_bucket_hit_w_retry(self):
        from google.cloud.storage.bucket import Bucket

        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._get_resource = mock.Mock(return_value=api_response)
        bucket_obj = Bucket(client, bucket_name)

        bucket = client.lookup_bucket(bucket_obj, retry=None)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)

        expected_path = f"/b/{bucket_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=bucket,
        )

    def test_create_bucket_w_missing_client_project(self):
        from google.cloud.exceptions import BadRequest

        credentials = _make_credentials()
        client = self._make_one(project=None, credentials=credentials)

        client._post_resource = mock.Mock()
        client._post_resource.side_effect = BadRequest("Required parameter: project")

        bucket_name = "bucket-name"

        with self.assertRaises(BadRequest):
            client.create_bucket(bucket_name)

        expected_path = "/b"
        expected_data = {"name": bucket_name}
        # no required parameter: project
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

    def test_create_bucket_w_missing_client_project_w_emulator(self):
        # mock STORAGE_EMULATOR_ENV_VAR is set
        host = "http://localhost:8080"
        environ = {STORAGE_EMULATOR_ENV_VAR: host}
        with mock.patch("os.environ", environ):
            client = self._make_one()

        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        # mock STORAGE_EMULATOR_ENV_VAR is set
        with mock.patch("os.environ", environ):
            bucket = client.create_bucket(bucket_name)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {"project": "<none>"}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_environ_project_w_emulator(self):
        # mock STORAGE_EMULATOR_ENV_VAR is set
        host = "http://localhost:8080"
        environ_project = "environ-project"
        environ = {
            STORAGE_EMULATOR_ENV_VAR: host,
            "GOOGLE_CLOUD_PROJECT": environ_project,
        }
        with mock.patch("os.environ", environ):
            client = self._make_one()

        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        # mock STORAGE_EMULATOR_ENV_VAR is set
        with mock.patch("os.environ", environ):
            bucket = client.create_bucket(bucket_name)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {"project": environ_project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_custom_endpoint(self):
        custom_endpoint = "storage-example.p.googleapis.com"
        credentials = _make_credentials()
        client = self._make_one(
            project="project",
            credentials=credentials,
            client_options={"api_endpoint": custom_endpoint},
        )
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = client.create_bucket(bucket_name)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {"project": client.project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_conflict_w_user_project(self):
        from google.cloud.exceptions import Conflict

        project = "PROJECT"
        user_project = "USER_PROJECT"
        other_project = "OTHER_PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.side_effect = Conflict("testing")

        bucket_name = "bucket-name"

        with self.assertRaises(Conflict):
            client.create_bucket(
                bucket_name, project=other_project, user_project=user_project
            )

        expected_path = "/b"
        expected_data = {"name": bucket_name}
        expected_query_params = {
            "project": other_project,
            "userProject": user_project,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

    def test_update_user_agent_when_default_clientinfo_provided(self):
        from google.cloud._http import ClientInfo

        client_info = ClientInfo()

        credentials = _make_credentials()
        client = self._make_one(
            project=None, credentials=credentials, client_info=client_info
        )
        self.assertGreater(len(client._connection.user_agent), 0)

        client.update_user_agent("my-test-agent/1.0")
        self.assertIn("my-test-agent/1.0", client._connection.user_agent)

    def test_update_user_agent_when_none_clientinfo_provided(self):
        credentials = _make_credentials()
        client = self._make_one(project=None, credentials=credentials)
        client.update_user_agent("my-test-agent/1.0")

        self.assertIn("my-test-agent/1.0", client._connection.user_agent)

    def test_update_user_agent_with_existing_user_agent(self):
        from google.cloud._http import ClientInfo

        client_info = ClientInfo(user_agent="existing-agent/2.0")
        credentials = _make_credentials()
        client = self._make_one(
            project=None, credentials=credentials, client_info=client_info
        )
        client.update_user_agent("my-test-agent/1.0")

        self.assertIn(
            "my-test-agent/1.0 existing-agent/2.0", client._connection.user_agent
        )

    @mock.patch("warnings.warn")
    def test_create_bucket_w_requester_pays_deprecated(self, mock_warn):
        from google.cloud.storage.bucket import Bucket

        bucket_name = "bucket-name"
        project = "PROJECT"
        credentials = _make_credentials()
        api_respone = {"name": bucket_name, "billing": {"requesterPays": True}}
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_respone

        bucket = client.create_bucket(bucket_name, requester_pays=True)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, bucket_name)
        self.assertTrue(bucket.requester_pays)

        expected_path = "/b"
        expected_data = api_respone
        expected_query_params = {"project": project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

        mock_warn.assert_called_with(
            "requester_pays arg is deprecated. Use Bucket().requester_pays instead.",
            PendingDeprecationWarning,
            stacklevel=1,
        )

    def test_create_bucket_w_predefined_acl_invalid(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()

        with self.assertRaises(ValueError):
            client.create_bucket(bucket_name, predefined_acl="bogus")

        client._post_resource.assert_not_called()

    def test_create_bucket_w_predefined_acl_valid_w_timeout(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response
        timeout = 42

        bucket = client.create_bucket(
            bucket_name,
            predefined_acl="publicRead",
            timeout=timeout,
        )

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {
            "project": project,
            "predefinedAcl": "publicRead",
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_predefined_default_object_acl_invalid(self):
        project = "PROJECT"
        bucket_name = "bucket-name"

        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()

        with self.assertRaises(ValueError):
            client.create_bucket(bucket_name, predefined_default_object_acl="bogus")

        client._post_resource.assert_not_called()

    def test_create_bucket_w_predefined_default_object_acl_valid_w_retry(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response
        retry = mock.Mock(spec=[])

        bucket = client.create_bucket(
            bucket_name,
            predefined_default_object_acl="publicRead",
            retry=retry,
        )

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {
            "project": project,
            "predefinedDefaultObjectAcl": "publicRead",
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=bucket,
        )

    def test_create_bucket_w_explicit_location(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        location = "us-central1"
        api_response = {"location": location, "name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = client.create_bucket(bucket_name, location=location)

        self.assertEqual(bucket.location, location)

        expected_path = "/b"
        expected_data = {"location": location, "name": bucket_name}
        expected_query_params = {"project": project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_custom_dual_region(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        location = "US"
        data_locations = ["US-EAST1", "US-WEST1"]
        api_response = {
            "location": location,
            "customPlacementConfig": {"dataLocations": data_locations},
            "name": bucket_name,
        }
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = client.create_bucket(
            bucket_name, location=location, data_locations=data_locations
        )

        self.assertEqual(bucket.location, location)
        self.assertEqual(bucket.data_locations, data_locations)

        expected_path = "/b"
        expected_data = {
            "location": location,
            "customPlacementConfig": {"dataLocations": data_locations},
            "name": bucket_name,
        }
        expected_query_params = {"project": project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_explicit_project(self):
        project = "PROJECT"
        other_project = "other-project-123"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = client.create_bucket(bucket_name, project=other_project)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {"project": other_project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_extra_properties(self):
        from google.cloud.storage.bucket import Bucket

        bucket_name = "bucket-name"
        project = "PROJECT"
        cors = [
            {
                "maxAgeSeconds": 60,
                "methods": ["*"],
                "origin": ["https://example.com/frontend"],
                "responseHeader": ["X-Custom-Header"],
            }
        ]
        lifecycle_rules = [{"action": {"type": "Delete"}, "condition": {"age": 365}}]
        location = "eu"
        labels = {"color": "red", "flavor": "cherry"}
        storage_class = "NEARLINE"
        api_response = {
            "name": bucket_name,
            "cors": cors,
            "lifecycle": {"rule": lifecycle_rules},
            "location": location,
            "storageClass": storage_class,
            "versioning": {"enabled": True},
            "billing": {"requesterPays": True},
            "labels": labels,
        }
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = Bucket(client=client, name=bucket_name)
        bucket.cors = cors
        bucket.lifecycle_rules = lifecycle_rules
        bucket.storage_class = storage_class
        bucket.versioning_enabled = True
        bucket.requester_pays = True
        bucket.labels = labels

        client.create_bucket(bucket, location=location, enable_object_retention=True)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {
            "project": project,
            "enableObjectRetention": True,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_create_bucket_w_name_only(self):
        project = "PROJECT"
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        bucket = client.create_bucket(bucket_name)

        expected_path = "/b"
        expected_data = api_response
        expected_query_params = {"project": project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    @staticmethod
    def _make_blob(*args, **kw):
        from google.cloud.storage.blob import Blob

        blob = Blob(*args, **kw)

        return blob

    def test_download_blob_to_file_with_failure(self):
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT
        from google.cloud.storage.exceptions import InvalidResponse

        project = "PROJECT"
        raw_response = requests.Response()
        raw_response.status_code = http.client.NOT_FOUND
        raw_request = requests.Request("GET", "http://example.com")
        raw_response.request = raw_request.prepare()
        grmp_response = InvalidResponse(raw_response)
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)
        blob = self._make_blob(name="blob_name", bucket=None)
        blob._encryption_key = None
        blob._get_download_url = mock.Mock()
        blob._do_download = mock.Mock()
        blob._do_download.side_effect = grmp_response

        file_obj = io.BytesIO()
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            with self.assertRaises(exceptions.NotFound):
                client.download_blob_to_file(blob, file_obj)

            self.assertEqual(file_obj.tell(), 0)
            headers = {
                **_get_default_headers(client._connection.user_agent),
                "accept-encoding": "gzip",
            }
        blob._do_download.assert_called_once_with(
            client._http,
            file_obj,
            blob._get_download_url(),
            headers,
            None,
            None,
            False,
            checksum="auto",
            timeout=_DEFAULT_TIMEOUT,
            retry=DEFAULT_RETRY,
            single_shot_download=False,
        )

    def test_download_blob_to_file_with_uri(self):
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(project=project, credentials=credentials)
        blob = self._make_blob(name="blob_name", bucket=None)
        file_obj = io.BytesIO()
        blob._encryption_key = None
        blob._get_download_url = mock.Mock()
        blob._do_download = mock.Mock()

        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            with mock.patch(
                "google.cloud.storage.client.Blob.from_uri", return_value=blob
            ):
                client.download_blob_to_file(
                    "gs://bucket_name/path/to/object", file_obj
                )

            headers = {
                **_get_default_headers(client._connection.user_agent),
                "accept-encoding": "gzip",
            }
        blob._do_download.assert_called_once_with(
            client._http,
            file_obj,
            blob._get_download_url(),
            headers,
            None,
            None,
            False,
            checksum="auto",
            timeout=_DEFAULT_TIMEOUT,
            retry=DEFAULT_RETRY,
            single_shot_download=False,
        )

    def test_download_blob_to_file_with_invalid_uri(self):
        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        file_obj = io.BytesIO()

        with pytest.raises(ValueError):
            client.download_blob_to_file("http://bucket_name/path/to/object", file_obj)

    def test_download_blob_to_file_w_no_retry(self):
        self._download_blob_to_file_helper(
            use_chunks=True, raw_download=True, retry=None
        )

    def test_download_blob_to_file_w_conditional_etag_match_string(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=None,
            if_etag_match="kittens",
        )

    def test_download_blob_to_file_w_conditional_etag_match_list(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=None,
            if_etag_match=["kittens", "fluffy"],
        )

    def test_download_blob_to_file_w_conditional_etag_not_match_string(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=None,
            if_etag_not_match="kittens",
        )

    def test_download_blob_to_file_w_conditional_etag_not_match_list(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=None,
            if_etag_not_match=["kittens", "fluffy"],
        )

    def test_download_blob_to_file_w_conditional_retry_pass(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            if_generation_match=1,
        )

    def test_download_blob_to_file_w_conditional_retry_fail(self):
        self._download_blob_to_file_helper(
            use_chunks=True,
            raw_download=True,
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            expect_condition_fail=True,
        )

    def _download_blob_to_file_helper(
        self, use_chunks, raw_download, expect_condition_fail=False, **extra_kwargs
    ):
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)
        blob = self._make_blob(name="blob_name", bucket=None)
        blob._encryption_key = None
        blob._get_download_url = mock.Mock()
        if use_chunks:
            blob._CHUNK_SIZE_MULTIPLE = 1
            blob.chunk_size = 3
        blob._do_download = mock.Mock()
        file_obj = io.BytesIO()
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            if raw_download:
                client.download_blob_to_file(
                    blob, file_obj, raw_download=True, **extra_kwargs
                )
            else:
                client.download_blob_to_file(blob, file_obj, **extra_kwargs)

        expected_retry = extra_kwargs.get("retry", DEFAULT_RETRY)
        if (
            expected_retry is DEFAULT_RETRY_IF_GENERATION_SPECIFIED
            and not expect_condition_fail
        ):
            expected_retry = DEFAULT_RETRY
        elif expect_condition_fail:
            expected_retry = None

        headers = {"accept-encoding": "gzip"}
        if_etag_match = extra_kwargs.get("if_etag_match")
        if if_etag_match is not None:
            if isinstance(if_etag_match, str):
                if_etag_match = [if_etag_match]
            headers["If-Match"] = ", ".join(if_etag_match)
        if_etag_not_match = extra_kwargs.get("if_etag_not_match")
        if if_etag_not_match is not None:
            if isinstance(if_etag_not_match, str):
                if_etag_not_match = [if_etag_not_match]
            headers["If-None-Match"] = ", ".join(if_etag_not_match)

        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            headers = {**_get_default_headers(client._connection.user_agent), **headers}

        blob._do_download.assert_called_once_with(
            client._http,
            file_obj,
            blob._get_download_url(),
            headers,
            None,
            None,
            raw_download,
            checksum="auto",
            timeout=_DEFAULT_TIMEOUT,
            retry=expected_retry,
            single_shot_download=False,
        )

    def test_download_blob_to_file_wo_chunks_wo_raw(self):
        self._download_blob_to_file_helper(use_chunks=False, raw_download=False)

    def test_download_blob_to_file_w_chunks_wo_raw(self):
        self._download_blob_to_file_helper(use_chunks=True, raw_download=False)

    def test_download_blob_to_file_wo_chunks_w_raw(self):
        self._download_blob_to_file_helper(use_chunks=False, raw_download=True)

    def test_download_blob_to_file_w_chunks_w_raw(self):
        self._download_blob_to_file_helper(use_chunks=True, raw_download=True)

    def test_download_blob_have_different_uuid(self):
        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)
        blob = self._make_blob(name="blob_name", bucket=None)
        blob._encryption_key = None
        blob._do_download = mock.Mock()
        blob._get_download_url = mock.Mock()
        file_obj = io.BytesIO()
        client.download_blob_to_file(blob, file_obj)
        client.download_blob_to_file(blob, file_obj)

        self.assertNotEqual(
            blob._do_download.call_args_list[0][0][3]["x-goog-api-client"],
            blob._do_download.call_args_list[1][0][3]["x-goog-api-client"],
        )

    def test_list_blobs_w_defaults_w_bucket_obj(self):
        from google.cloud.storage.bucket import Bucket, _blobs_page_start, _item_to_blob

        project = "PROJECT"
        bucket_name = "bucket-name"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])
        bucket = Bucket(client, bucket_name)

        iterator = client.list_blobs(bucket)

        self.assertIs(iterator, client._list_resource.return_value)
        self.assertIs(iterator.bucket, bucket)
        self.assertEqual(iterator.prefixes, set())

        expected_path = f"/b/{bucket_name}/o"
        expected_item_to_value = _item_to_blob
        expected_page_token = None
        expected_max_results = None
        expected_extra_params = {"projection": "noAcl"}
        expected_page_start = _blobs_page_start
        expected_page_size = None
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_start=expected_page_start,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_list_blobs_w_explicit_w_user_project(self):
        from google.cloud.storage.bucket import _blobs_page_start, _item_to_blob

        project = "PROJECT"
        user_project = "user-project-123"
        bucket_name = "name"
        max_results = 10
        page_token = "ABCD"
        prefix = "subfolder"
        delimiter = "/"
        match_glob = "**txt"
        start_offset = "c"
        end_offset = "g"
        include_trailing_delimiter = True
        include_folders_as_prefixes = True
        soft_deleted = False
        versions = True
        projection = "full"
        page_size = 2
        fields = "items/contentLanguage,nextPageToken"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])
        client._bucket_arg_to_bucket = mock.Mock(spec=[])
        bucket = client._bucket_arg_to_bucket.return_value = mock.Mock(
            spec=["path", "user_project"],
        )
        bucket.path = f"/b/{bucket_name}"
        bucket.user_project = user_project
        timeout = 42
        retry = mock.Mock(spec=[])

        iterator = client.list_blobs(
            bucket_or_name=bucket_name,
            max_results=max_results,
            page_token=page_token,
            prefix=prefix,
            delimiter=delimiter,
            start_offset=start_offset,
            end_offset=end_offset,
            include_trailing_delimiter=include_trailing_delimiter,
            versions=versions,
            projection=projection,
            fields=fields,
            page_size=page_size,
            timeout=timeout,
            retry=retry,
            match_glob=match_glob,
            include_folders_as_prefixes=include_folders_as_prefixes,
            soft_deleted=soft_deleted,
        )

        self.assertIs(iterator, client._list_resource.return_value)
        self.assertIs(iterator.bucket, bucket)
        self.assertEqual(iterator.prefixes, set())

        expected_path = f"/b/{bucket_name}/o"
        expected_item_to_value = _item_to_blob
        expected_page_token = page_token
        expected_max_results = max_results
        expected_extra_params = {
            "projection": projection,
            "prefix": prefix,
            "delimiter": delimiter,
            "matchGlob": match_glob,
            "startOffset": start_offset,
            "endOffset": end_offset,
            "includeTrailingDelimiter": include_trailing_delimiter,
            "versions": versions,
            "fields": fields,
            "userProject": user_project,
            "includeFoldersAsPrefixes": include_folders_as_prefixes,
            "softDeleted": soft_deleted,
        }
        expected_page_start = _blobs_page_start
        expected_page_size = 2
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_start=expected_page_start,
            page_size=expected_page_size,
            timeout=timeout,
            retry=retry,
        )

    def test_list_blobs_w_filter(self):
        from google.cloud.storage.bucket import _blobs_page_start, _item_to_blob

        project = "PROJECT"
        bucket_name = "name"
        filter_ = 'contexts."foo"="bar"'
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])
        client._bucket_arg_to_bucket = mock.Mock(spec=[])
        bucket = client._bucket_arg_to_bucket.return_value = mock.Mock(
            spec=["path", "user_project"],
        )
        bucket.path = f"/b/{bucket_name}"
        bucket.user_project = None

        iterator = client.list_blobs(bucket_or_name=bucket_name, filter_=filter_)

        self.assertIs(iterator, client._list_resource.return_value)
        self.assertIs(iterator.bucket, bucket)
        self.assertEqual(iterator.prefixes, set())

        expected_path = f"/b/{bucket_name}/o"
        expected_item_to_value = _item_to_blob
        expected_page_token = None
        expected_max_results = None
        expected_extra_params = {
            "projection": "noAcl",
            "filter": filter_,
        }
        expected_page_start = _blobs_page_start
        expected_page_size = None
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_start=expected_page_start,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_list_buckets_wo_project(self):
        from google.cloud.exceptions import BadRequest

        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        credentials = _make_credentials()
        client = self._make_one(project=None, credentials=credentials)

        client._list_resource = mock.Mock()
        client._list_resource.side_effect = BadRequest("Required parameter: project")

        with self.assertRaises(BadRequest):
            client.list_buckets()

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        # no required parameter: project
        expected_extra_params = {
            "projection": "noAcl",
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_wo_project_w_emulator(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        # mock STORAGE_EMULATOR_ENV_VAR is set
        host = "http://localhost:8080"
        environ = {STORAGE_EMULATOR_ENV_VAR: host}
        with mock.patch("os.environ", environ):
            client = self._make_one()

        client._list_resource = mock.Mock(spec=[])

        # mock STORAGE_EMULATOR_ENV_VAR is set
        with mock.patch("os.environ", environ):
            client.list_buckets()

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        expected_extra_params = {
            "project": "<none>",
            "projection": "noAcl",
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_w_environ_project_w_emulator(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        # mock STORAGE_EMULATOR_ENV_VAR is set
        host = "http://localhost:8080"
        environ_project = "environ-project"
        environ = {
            STORAGE_EMULATOR_ENV_VAR: host,
            "GOOGLE_CLOUD_PROJECT": environ_project,
        }
        with mock.patch("os.environ", environ):
            client = self._make_one()

        client._list_resource = mock.Mock(spec=[])

        # mock STORAGE_EMULATOR_ENV_VAR is set
        with mock.patch("os.environ", environ):
            client.list_buckets()

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        expected_extra_params = {
            "project": environ_project,
            "projection": "noAcl",
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_w_custom_endpoint(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        custom_endpoint = "storage-example.p.googleapis.com"
        credentials = _make_credentials()
        client = self._make_one(
            project="project",
            credentials=credentials,
            client_options={"api_endpoint": custom_endpoint},
        )
        client._list_resource = mock.Mock(spec=[])

        iterator = client.list_buckets()

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        expected_extra_params = {
            "project": client.project,
            "projection": "noAcl",
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_w_defaults(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])

        iterator = client.list_buckets()

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        expected_extra_params = {
            "project": project,
            "projection": "noAcl",
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_w_soft_deleted(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])

        iterator = client.list_buckets(soft_deleted=True)

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = None
        expected_max_results = None
        expected_page_size = None
        expected_extra_params = {
            "project": project,
            "projection": "noAcl",
            "softDeleted": True,
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )

    def test_list_buckets_w_explicit(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        project = "foo-bar"
        other_project = "OTHER_PROJECT"
        max_results = 10
        page_token = "ABCD"
        prefix = "subfolder"
        projection = "full"
        fields = "items/id,nextPageToken"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])
        page_size = 2
        timeout = 42
        retry = mock.Mock(spec=[])

        iterator = client.list_buckets(
            project=other_project,
            max_results=max_results,
            page_token=page_token,
            prefix=prefix,
            projection=projection,
            fields=fields,
            page_size=page_size,
            timeout=timeout,
            retry=retry,
        )

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_page_token = page_token
        expected_max_results = max_results
        expected_extra_params = {
            "project": other_project,
            "prefix": prefix,
            "projection": projection,
            "fields": fields,
        }
        expected_page_size = 2
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=expected_page_token,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            page_size=expected_page_size,
            timeout=timeout,
            retry=retry,
            page_start=_buckets_page_start,
        )

    def test_restore_bucket(self):
        from google.cloud.storage.bucket import Bucket

        PROJECT = "PROJECT"
        NAME = "my_deleted_bucket"
        GENERATION = 12345

        api_response = {"name": NAME}
        credentials = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=credentials)
        client._post_resource = mock.Mock(return_value=api_response)

        bucket = client.restore_bucket(NAME, GENERATION)

        self.assertIsInstance(bucket, Bucket)
        self.assertEqual(bucket.name, NAME)

        expected_path = f"/b/{NAME}/restore"
        expected_query_params = {"generation": 12345, "projection": "noAcl"}
        client._post_resource.assert_called_once_with(
            expected_path,
            None,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def _create_hmac_key_helper(
        self,
        explicit_project=None,
        user_project=None,
        timeout=None,
        retry=None,
    ):
        from google.cloud.storage.hmac_key import HMACKeyMetadata

        project = "PROJECT"
        access_id = "ACCESS-ID"
        credentials = _make_credentials()
        email = "storage-user-123@example.com"
        secret = "a" * 40
        now = _NOW(_UTC)
        now_stamp = f"{now.isoformat()}Z"

        if explicit_project is not None:
            expected_project = explicit_project
        else:
            expected_project = project

        api_response = {
            "kind": "storage#hmacKey",
            "metadata": {
                "accessId": access_id,
                "etag": "ETAG",
                "id": f"projects/{project}/hmacKeys/{access_id}",
                "project": expected_project,
                "state": "ACTIVE",
                "serviceAccountEmail": email,
                "timeCreated": now_stamp,
                "updated": now_stamp,
            },
            "secret": secret,
        }

        client = self._make_one(project=project, credentials=credentials)
        client._post_resource = mock.Mock()
        client._post_resource.return_value = api_response

        kwargs = {}
        if explicit_project is not None:
            kwargs["project_id"] = explicit_project

        if user_project is not None:
            kwargs["user_project"] = user_project

        if timeout is None:
            expected_timeout = self._get_default_timeout()
        else:
            expected_timeout = kwargs["timeout"] = timeout

        if retry is None:
            expected_retry = None
        else:
            expected_retry = kwargs["retry"] = retry

        metadata, secret = client.create_hmac_key(service_account_email=email, **kwargs)

        self.assertIsInstance(metadata, HMACKeyMetadata)

        self.assertIs(metadata._client, client)
        self.assertEqual(metadata._properties, api_response["metadata"])
        self.assertEqual(secret, api_response["secret"])

        expected_path = f"/projects/{expected_project}/hmacKeys"
        expected_data = None
        expected_query_params = {"serviceAccountEmail": email}

        if user_project is not None:
            expected_query_params["userProject"] = user_project

        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=expected_timeout,
            retry=expected_retry,
        )

    def test_create_hmac_key_defaults(self):
        self._create_hmac_key_helper()

    def test_create_hmac_key_explicit_project(self):
        self._create_hmac_key_helper(explicit_project="other-project-456")

    def test_create_hmac_key_w_user_project(self):
        self._create_hmac_key_helper(user_project="billed-project")

    def test_create_hmac_key_w_timeout(self):
        self._create_hmac_key_helper(timeout=42)

    def test_create_hmac_key_w_retry(self):
        self._create_hmac_key_helper(retry=mock.Mock(spec=[]))

    def test_list_hmac_keys_w_defaults(self):
        from google.cloud.storage.client import _item_to_hmac_key_metadata

        project = "PROJECT"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])

        iterator = client.list_hmac_keys()

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = f"/projects/{project}/hmacKeys"
        expected_item_to_value = _item_to_hmac_key_metadata
        expected_max_results = None
        expected_extra_params = {}
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_list_hmac_keys_w_explicit(self):
        from google.cloud.storage.client import _item_to_hmac_key_metadata

        project = "PROJECT"
        other_project = "other-project-456"
        max_results = 3
        show_deleted_keys = True
        service_account_email = "storage-user-123@example.com"
        user_project = "billed-project"
        credentials = _make_credentials()
        client = self._make_one(project=project, credentials=credentials)
        client._list_resource = mock.Mock(spec=[])
        timeout = 42
        retry = mock.Mock(spec=[])

        iterator = client.list_hmac_keys(
            max_results=max_results,
            service_account_email=service_account_email,
            show_deleted_keys=show_deleted_keys,
            project_id=other_project,
            user_project=user_project,
            timeout=timeout,
            retry=retry,
        )

        self.assertIs(iterator, client._list_resource.return_value)

        expected_path = f"/projects/{other_project}/hmacKeys"
        expected_item_to_value = _item_to_hmac_key_metadata
        expected_max_results = max_results
        expected_extra_params = {
            "serviceAccountEmail": service_account_email,
            "showDeletedKeys": show_deleted_keys,
            "userProject": user_project,
        }
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            max_results=expected_max_results,
            extra_params=expected_extra_params,
            timeout=timeout,
            retry=retry,
        )

    def test_get_hmac_key_metadata_wo_project(self):
        from google.cloud.storage.hmac_key import HMACKeyMetadata

        PROJECT = "PROJECT"
        EMAIL = "storage-user-123@example.com"
        ACCESS_ID = "ACCESS-ID"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)

        resource = {
            "kind": "storage#hmacKeyMetadata",
            "accessId": ACCESS_ID,
            "projectId": PROJECT,
            "serviceAccountEmail": EMAIL,
        }

        http = _make_requests_session([_make_json_response(resource)])
        client._http_internal = http

        metadata = client.get_hmac_key_metadata(ACCESS_ID, timeout=42)

        self.assertIsInstance(metadata, HMACKeyMetadata)
        self.assertIs(metadata._client, client)
        self.assertEqual(metadata.access_id, ACCESS_ID)
        self.assertEqual(metadata.project, PROJECT)

        http.request.assert_called_once_with(
            method="GET", url=mock.ANY, data=None, headers=mock.ANY, timeout=42
        )
        _, kwargs = http.request.call_args
        scheme, netloc, path, qs, _ = urllib.parse.urlsplit(kwargs.get("url"))
        self.assertEqual(f"{scheme}://{netloc}", client._connection.API_BASE_URL)
        self.assertEqual(
            path,
            "/".join(
                [
                    "",
                    "storage",
                    client._connection.API_VERSION,
                    "projects",
                    PROJECT,
                    "hmacKeys",
                    ACCESS_ID,
                ]
            ),
        )

    def test_get_hmac_key_metadata_w_project(self):
        from google.cloud.storage.hmac_key import HMACKeyMetadata

        PROJECT = "PROJECT"
        OTHER_PROJECT = "other-project-456"
        EMAIL = "storage-user-123@example.com"
        ACCESS_ID = "ACCESS-ID"
        USER_PROJECT = "billed-project"
        CREDENTIALS = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=CREDENTIALS)

        resource = {
            "kind": "storage#hmacKeyMetadata",
            "accessId": ACCESS_ID,
            "projectId": OTHER_PROJECT,
            "serviceAccountEmail": EMAIL,
        }

        http = _make_requests_session([_make_json_response(resource)])
        client._http_internal = http

        metadata = client.get_hmac_key_metadata(
            ACCESS_ID, project_id=OTHER_PROJECT, user_project=USER_PROJECT
        )

        self.assertIsInstance(metadata, HMACKeyMetadata)
        self.assertIs(metadata._client, client)
        self.assertEqual(metadata.access_id, ACCESS_ID)
        self.assertEqual(metadata.project, OTHER_PROJECT)

        http.request.assert_called_once_with(
            method="GET",
            url=mock.ANY,
            data=None,
            headers=mock.ANY,
            timeout=self._get_default_timeout(),
        )
        _, kwargs = http.request.call_args
        scheme, netloc, path, qs, _ = urllib.parse.urlsplit(kwargs.get("url"))
        self.assertEqual(f"{scheme}://{netloc}", client._connection.API_BASE_URL)
        self.assertEqual(
            path,
            "/".join(
                [
                    "",
                    "storage",
                    client._connection.API_VERSION,
                    "projects",
                    OTHER_PROJECT,
                    "hmacKeys",
                    ACCESS_ID,
                ]
            ),
        )
        parms = dict(urllib.parse.parse_qsl(qs))
        self.assertEqual(parms["userProject"], USER_PROJECT)

    def test_get_signed_policy_v4(self):
        import datetime

        BUCKET_NAME = "bucket-name"
        BLOB_NAME = "object-name"
        EXPECTED_SIGN = "5369676e61747572655f6279746573"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsiYWNsIjoicHJpdmF0ZSJ9LFsic3RhcnRzLXdpdGgiLCIkQ29udGVudC1UeXBlIiwidGV4dC9wbGFpbiJdLHsiYnVja2V0IjoiYnVja2V0LW5hbWUifSx7ImtleSI6Im9iamVjdC1uYW1lIn0seyJ4LWdvb2ctZGF0ZSI6IjIwMjAwMzEyVDExNDcxNloifSx7IngtZ29vZy1jcmVkZW50aWFsIjoidGVzdEBtYWlsLmNvbS8yMDIwMDMxMi9hdXRvL3N0b3JhZ2UvZ29vZzRfcmVxdWVzdCJ9LHsieC1nb29nLWFsZ29yaXRobSI6IkdPT0c0LVJTQS1TSEEyNTYifV0sImV4cGlyYXRpb24iOiIyMDIwLTAzLTI2VDAwOjAwOjEwWiJ9"

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            policy = client.generate_signed_post_policy_v4(
                BUCKET_NAME,
                BLOB_NAME,
                expiration=datetime.datetime(2020, 3, 12),
                conditions=[
                    {"bucket": BUCKET_NAME},
                    {"acl": "private"},
                    ["starts-with", "$Content-Type", "text/plain"],
                ],
                credentials=_create_signing_credentials(),
            )
        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        fields = policy["fields"]

        self.assertEqual(fields["key"], BLOB_NAME)
        self.assertEqual(fields["x-goog-algorithm"], "GOOG4-RSA-SHA256")
        self.assertEqual(fields["x-goog-date"], "20200312T114716Z")
        self.assertEqual(
            fields["x-goog-credential"],
            "test@mail.com/20200312/auto/storage/goog4_request",
        )
        self.assertEqual(fields["x-goog-signature"], EXPECTED_SIGN)
        self.assertEqual(fields["policy"], EXPECTED_POLICY)

    def test_get_signed_policy_v4_without_credentials(self):
        import datetime

        BUCKET_NAME = "bucket-name"
        BLOB_NAME = "object-name"
        EXPECTED_SIGN = "5369676e61747572655f6279746573"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsiYWNsIjoicHJpdmF0ZSJ9LFsic3RhcnRzLXdpdGgiLCIkQ29udGVudC1UeXBlIiwidGV4dC9wbGFpbiJdLHsiYnVja2V0IjoiYnVja2V0LW5hbWUifSx7ImtleSI6Im9iamVjdC1uYW1lIn0seyJ4LWdvb2ctZGF0ZSI6IjIwMjAwMzEyVDExNDcxNloifSx7IngtZ29vZy1jcmVkZW50aWFsIjoidGVzdEBtYWlsLmNvbS8yMDIwMDMxMi9hdXRvL3N0b3JhZ2UvZ29vZzRfcmVxdWVzdCJ9LHsieC1nb29nLWFsZ29yaXRobSI6IkdPT0c0LVJTQS1TSEEyNTYifV0sImV4cGlyYXRpb24iOiIyMDIwLTAzLTI2VDAwOjAwOjEwWiJ9"

        client = self._make_one(
            project="PROJECT", credentials=_create_signing_credentials()
        )

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            policy = client.generate_signed_post_policy_v4(
                BUCKET_NAME,
                BLOB_NAME,
                expiration=datetime.datetime(2020, 3, 12),
                conditions=[
                    {"bucket": BUCKET_NAME},
                    {"acl": "private"},
                    ["starts-with", "$Content-Type", "text/plain"],
                ],
            )
        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        fields = policy["fields"]

        self.assertEqual(fields["key"], BLOB_NAME)
        self.assertEqual(fields["x-goog-algorithm"], "GOOG4-RSA-SHA256")
        self.assertEqual(fields["x-goog-date"], "20200312T114716Z")
        self.assertEqual(
            fields["x-goog-credential"],
            "test@mail.com/20200312/auto/storage/goog4_request",
        )
        self.assertEqual(fields["x-goog-signature"], EXPECTED_SIGN)
        self.assertEqual(fields["policy"], EXPECTED_POLICY)

    def test_get_signed_policy_v4_with_fields(self):
        import datetime

        BUCKET_NAME = "bucket-name"
        BLOB_NAME = "object-name"
        FIELD1_VALUE = "Value1"
        EXPECTED_SIGN = "5369676e61747572655f6279746573"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsiYWNsIjoicHJpdmF0ZSJ9LFsic3RhcnRzLXdpdGgiLCIkQ29udGVudC1UeXBlIiwidGV4dC9wbGFpbiJdLHsiZmllbGQxIjoiVmFsdWUxIn0seyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsia2V5Ijoib2JqZWN0LW5hbWUifSx7IngtZ29vZy1kYXRlIjoiMjAyMDAzMTJUMTE0NzE2WiJ9LHsieC1nb29nLWNyZWRlbnRpYWwiOiJ0ZXN0QG1haWwuY29tLzIwMjAwMzEyL2F1dG8vc3RvcmFnZS9nb29nNF9yZXF1ZXN0In0seyJ4LWdvb2ctYWxnb3JpdGhtIjoiR09PRzQtUlNBLVNIQTI1NiJ9XSwiZXhwaXJhdGlvbiI6IjIwMjAtMDMtMjZUMDA6MDA6MTBaIn0="

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            policy = client.generate_signed_post_policy_v4(
                BUCKET_NAME,
                BLOB_NAME,
                expiration=datetime.datetime(2020, 3, 12),
                conditions=[
                    {"bucket": BUCKET_NAME},
                    {"acl": "private"},
                    ["starts-with", "$Content-Type", "text/plain"],
                ],
                fields={"field1": FIELD1_VALUE, "x-ignore-field": "Ignored_value"},
                credentials=_create_signing_credentials(),
            )
        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        fields = policy["fields"]

        self.assertEqual(fields["key"], BLOB_NAME)
        self.assertEqual(fields["x-goog-algorithm"], "GOOG4-RSA-SHA256")
        self.assertEqual(fields["x-goog-date"], "20200312T114716Z")
        self.assertEqual(fields["field1"], FIELD1_VALUE)
        self.assertNotIn("x-ignore-field", fields.keys())
        self.assertEqual(
            fields["x-goog-credential"],
            "test@mail.com/20200312/auto/storage/goog4_request",
        )
        self.assertEqual(fields["x-goog-signature"], EXPECTED_SIGN)
        self.assertEqual(fields["policy"], EXPECTED_POLICY)

    def test_get_signed_policy_v4_virtual_hosted_style(self):
        import datetime

        BUCKET_NAME = "bucket-name"

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, _, _ = _time_functions_patches()
        with dtstamps_patch:
            policy = client.generate_signed_post_policy_v4(
                BUCKET_NAME,
                "object-name",
                expiration=datetime.datetime(2020, 3, 12),
                virtual_hosted_style=True,
                credentials=_create_signing_credentials(),
            )
        self.assertEqual(
            policy["url"], f"https://{BUCKET_NAME}.storage.googleapis.com/"
        )

    def test_get_signed_policy_v4_bucket_bound_hostname(self):
        import datetime

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, _, _ = _time_functions_patches()
        with dtstamps_patch:
            policy = client.generate_signed_post_policy_v4(
                "bucket-name",
                "object-name",
                expiration=datetime.datetime(2020, 3, 12),
                bucket_bound_hostname="https://bucket.bound_hostname",
                credentials=_create_signing_credentials(),
            )
        self.assertEqual(policy["url"], "https://bucket.bound_hostname/")

    def test_get_signed_policy_v4_with_conflicting_arguments(self):
        import datetime

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, _, _ = _time_functions_patches()
        with dtstamps_patch:
            with self.assertRaises(ValueError):
                client.generate_signed_post_policy_v4(
                    "bucket-name",
                    "object-name",
                    expiration=datetime.datetime(2020, 3, 12),
                    bucket_bound_hostname="https://bucket.bound_hostname",
                    virtual_hosted_style=True,
                    credentials=_create_signing_credentials(),
                )

    def test_get_signed_policy_v4_bucket_bound_hostname_with_scheme(self):
        import datetime

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, _, _ = _time_functions_patches()
        with dtstamps_patch:
            policy = client.generate_signed_post_policy_v4(
                "bucket-name",
                "object-name",
                expiration=datetime.datetime(2020, 3, 12),
                bucket_bound_hostname="bucket.bound_hostname",
                scheme="http",
                credentials=_create_signing_credentials(),
            )
        self.assertEqual(policy["url"], "http://bucket.bound_hostname/")

    def test_get_signed_policy_v4_no_expiration(self):
        BUCKET_NAME = "bucket-name"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsia2V5Ijoib2JqZWN0LW5hbWUifSx7IngtZ29vZy1kYXRlIjoiMjAyMDAzMTJUMTE0NzE2WiJ9LHsieC1nb29nLWNyZWRlbnRpYWwiOiJ0ZXN0QG1haWwuY29tLzIwMjAwMzEyL2F1dG8vc3RvcmFnZS9nb29nNF9yZXF1ZXN0In0seyJ4LWdvb2ctYWxnb3JpdGhtIjoiR09PRzQtUlNBLVNIQTI1NiJ9XSwiZXhwaXJhdGlvbiI6IjIwMjAtMDMtMjZUMDA6MDA6MTBaIn0="

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            policy = client.generate_signed_post_policy_v4(
                BUCKET_NAME,
                "object-name",
                expiration=None,
                credentials=_create_signing_credentials(),
            )

        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        self.assertEqual(policy["fields"]["policy"], EXPECTED_POLICY)

    def test_get_signed_policy_v4_with_access_token(self):
        import datetime

        BUCKET_NAME = "bucket-name"
        BLOB_NAME = "object-name"
        EXPECTED_SIGN = "0c4003044105"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsiYWNsIjoicHJpdmF0ZSJ9LFsic3RhcnRzLXdpdGgiLCIkQ29udGVudC1UeXBlIiwidGV4dC9wbGFpbiJdLHsiYnVja2V0IjoiYnVja2V0LW5hbWUifSx7ImtleSI6Im9iamVjdC1uYW1lIn0seyJ4LWdvb2ctZGF0ZSI6IjIwMjAwMzEyVDExNDcxNloifSx7IngtZ29vZy1jcmVkZW50aWFsIjoidGVzdEBtYWlsLmNvbS8yMDIwMDMxMi9hdXRvL3N0b3JhZ2UvZ29vZzRfcmVxdWVzdCJ9LHsieC1nb29nLWFsZ29yaXRobSI6IkdPT0c0LVJTQS1TSEEyNTYifV0sImV4cGlyYXRpb24iOiIyMDIwLTAzLTI2VDAwOjAwOjEwWiJ9"

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            with mock.patch(
                "google.cloud.storage.client._sign_message", return_value=b"DEADBEEF"
            ):
                policy = client.generate_signed_post_policy_v4(
                    BUCKET_NAME,
                    BLOB_NAME,
                    expiration=datetime.datetime(2020, 3, 12),
                    conditions=[
                        {"bucket": BUCKET_NAME},
                        {"acl": "private"},
                        ["starts-with", "$Content-Type", "text/plain"],
                    ],
                    credentials=_create_signing_credentials(),
                    service_account_email="test@mail.com",
                    access_token="token",
                )
        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        fields = policy["fields"]

        self.assertEqual(fields["key"], BLOB_NAME)
        self.assertEqual(fields["x-goog-algorithm"], "GOOG4-RSA-SHA256")
        self.assertEqual(fields["x-goog-date"], "20200312T114716Z")
        self.assertEqual(
            fields["x-goog-credential"],
            "test@mail.com/20200312/auto/storage/goog4_request",
        )
        self.assertEqual(fields["x-goog-signature"], EXPECTED_SIGN)
        self.assertEqual(fields["policy"], EXPECTED_POLICY)

    def test_get_signed_policy_v4_with_access_token_sa_email(self):
        import datetime

        BUCKET_NAME = "bucket-name"
        BLOB_NAME = "object-name"
        EXPECTED_SIGN = "0c4003044105"
        EXPECTED_POLICY = "eyJjb25kaXRpb25zIjpbeyJidWNrZXQiOiJidWNrZXQtbmFtZSJ9LHsiYWNsIjoicHJpdmF0ZSJ9LFsic3RhcnRzLXdpdGgiLCIkQ29udGVudC1UeXBlIiwidGV4dC9wbGFpbiJdLHsiYnVja2V0IjoiYnVja2V0LW5hbWUifSx7ImtleSI6Im9iamVjdC1uYW1lIn0seyJ4LWdvb2ctZGF0ZSI6IjIwMjAwMzEyVDExNDcxNloifSx7IngtZ29vZy1jcmVkZW50aWFsIjoidGVzdEBtYWlsLmNvbS8yMDIwMDMxMi9hdXRvL3N0b3JhZ2UvZ29vZzRfcmVxdWVzdCJ9LHsieC1nb29nLWFsZ29yaXRobSI6IkdPT0c0LVJTQS1TSEEyNTYifV0sImV4cGlyYXRpb24iOiIyMDIwLTAzLTI2VDAwOjAwOjEwWiJ9"

        project = "PROJECT"
        credentials = _make_credentials(project=project)
        client = self._make_one(credentials=credentials)

        dtstamps_patch, now_patch, expire_secs_patch = _time_functions_patches()
        with dtstamps_patch, now_patch, expire_secs_patch:
            with mock.patch(
                "google.cloud.storage.client._sign_message", return_value=b"DEADBEEF"
            ):
                policy = client.generate_signed_post_policy_v4(
                    BUCKET_NAME,
                    BLOB_NAME,
                    expiration=datetime.datetime(2020, 3, 12),
                    conditions=[
                        {"bucket": BUCKET_NAME},
                        {"acl": "private"},
                        ["starts-with", "$Content-Type", "text/plain"],
                    ],
                    service_account_email="test@mail.com",
                    access_token="token",
                )
        self.assertEqual(
            policy["url"], "https://storage.googleapis.com/" + BUCKET_NAME + "/"
        )
        fields = policy["fields"]

        self.assertEqual(fields["key"], BLOB_NAME)
        self.assertEqual(fields["x-goog-algorithm"], "GOOG4-RSA-SHA256")
        self.assertEqual(fields["x-goog-date"], "20200312T114716Z")
        self.assertEqual(
            fields["x-goog-credential"],
            "test@mail.com/20200312/auto/storage/goog4_request",
        )
        self.assertEqual(fields["x-goog-signature"], EXPECTED_SIGN)
        self.assertEqual(fields["policy"], EXPECTED_POLICY)

    def test_list_buckets_w_partial_success(self):
        from google.cloud.storage.client import _buckets_page_start, _item_to_bucket

        PROJECT = "project"
        bucket_name = "bucket-name"
        unreachable_bucket = "projects/_/buckets/unreachable-bucket"

        credentials = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=credentials)

        mock_bucket = mock.Mock()
        mock_bucket.name = bucket_name

        mock_page = mock.Mock()
        mock_page.unreachable = [unreachable_bucket]
        mock_page.__iter__ = mock.Mock(return_value=iter([mock_bucket]))

        mock_iterator = mock.Mock()
        mock_iterator.pages = iter([mock_page])

        client._list_resource = mock.Mock(return_value=mock_iterator)

        iterator = client.list_buckets(return_partial_success=True)

        page = next(iterator.pages)

        self.assertEqual(page.unreachable, [unreachable_bucket])

        buckets = list(page)
        self.assertEqual(len(buckets), 1)
        self.assertEqual(buckets[0].name, bucket_name)

        expected_path = "/b"
        expected_item_to_value = _item_to_bucket
        expected_extra_params = {
            "project": PROJECT,
            "projection": "noAcl",
            "returnPartialSuccess": True,
        }

        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            page_token=None,
            max_results=None,
            extra_params=expected_extra_params,
            page_size=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            page_start=_buckets_page_start,
        )


class Test__item_to_bucket(unittest.TestCase):
    def _call_fut(self, iterator, item):
        from google.cloud.storage.client import _item_to_bucket

        return _item_to_bucket(iterator, item)

    def test_w_empty_item(self):
        from google.cloud.storage.bucket import Bucket

        iterator = mock.Mock(spec=["client"])
        item = {}

        bucket = self._call_fut(iterator, item)

        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, iterator.client)
        self.assertIsNone(bucket.name)

    def test_w_name(self):
        from google.cloud.storage.bucket import Bucket

        name = "name"
        iterator = mock.Mock(spec=["client"])
        item = {"name": name}

        bucket = self._call_fut(iterator, item)

        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, iterator.client)
        self.assertEqual(bucket.name, name)


class Test__item_to_hmac_key_metadata(unittest.TestCase):
    def _call_fut(self, iterator, item):
        from google.cloud.storage.client import _item_to_hmac_key_metadata

        return _item_to_hmac_key_metadata(iterator, item)

    def test_it(self):
        from google.cloud.storage.hmac_key import HMACKeyMetadata

        access_id = "ABCDE"
        iterator = mock.Mock(spec=["client"])
        item = {"id": access_id}

        metadata = self._call_fut(iterator, item)

        self.assertIsInstance(metadata, HMACKeyMetadata)
        self.assertIs(metadata._client, iterator.client)
        self.assertEqual(metadata._properties, item)


@pytest.mark.parametrize("test_data", _POST_POLICY_TESTS)
def test_conformance_post_policy(test_data):
    import datetime

    from google.cloud.storage.client import Client

    in_data = test_data["policyInput"]
    timestamp = datetime.datetime.strptime(in_data["timestamp"], "%Y-%m-%dT%H:%M:%SZ")

    client = Client(credentials=_FAKE_CREDENTIALS, project="PROJECT")

    # mocking time functions
    with mock.patch("google.cloud.storage._signing._NOW", return_value=timestamp):
        with mock.patch(
            "google.cloud.storage.client.get_expiration_seconds_v4",
            return_value=in_data["expiration"],
        ):
            with mock.patch("google.cloud.storage.client._NOW", return_value=timestamp):
                policy = client.generate_signed_post_policy_v4(
                    bucket_name=in_data["bucket"],
                    blob_name=in_data["object"],
                    conditions=_prepare_conditions(in_data),
                    fields=in_data.get("fields"),
                    credentials=_FAKE_CREDENTIALS,
                    expiration=in_data["expiration"],
                    virtual_hosted_style=in_data.get("urlStyle")
                    == "VIRTUAL_HOSTED_STYLE",
                    bucket_bound_hostname=in_data.get("bucketBoundHostname"),
                    scheme=in_data.get("scheme"),
                )
    fields = policy["fields"]
    out_data = test_data["policyOutput"]

    decoded_policy = base64.b64decode(fields["policy"]).decode("unicode_escape")
    assert decoded_policy == out_data["expectedDecodedPolicy"]

    for field in (
        "x-goog-algorithm",
        "x-goog-credential",
        "x-goog-date",
        "x-goog-signature",
    ):
        assert fields[field] == test_data["policyOutput"]["fields"][field]

    assert policy["url"] == out_data["url"]


def _prepare_conditions(in_data):
    """Helper for V4 POST policy generation conformance tests.

    Convert conformance test data conditions dict into list.

    Args:
        in_data (dict): conditions arg from conformance test data.

    Returns:
        list: conditions arg to pass into generate_signed_post_policy_v4().
    """
    if "conditions" in in_data:
        conditions = []
        for key, value in in_data["conditions"].items():
            # camel case to snake case with "-" separator
            field = re.sub(r"(?<!^)(?=[A-Z])", "-", key).lower()
            conditions.append([field] + value)

        return conditions


def _time_functions_patches():
    """Helper for POST policy generation - returns all necessary time functions patches."""
    import datetime

    dtstamps_patch = mock.patch(
        "google.cloud.storage.client.get_v4_now_dtstamps",
        return_value=("20200312T114716Z", "20200312"),
    )
    now_patch = mock.patch(
        "google.cloud.storage.client._NOW", return_value=datetime.datetime(2020, 3, 26)
    )
    expire_secs_patch = mock.patch(
        "google.cloud.storage.client.get_expiration_seconds_v4", return_value=10
    )
    return dtstamps_patch, now_patch, expire_secs_patch
