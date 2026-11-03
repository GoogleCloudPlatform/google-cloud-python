# Copyright 2014 Google LLC
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

import mock
import pytest

from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
)

GCCL_INVOCATION_TEST_CONST = "gccl-invocation-id/test-invocation-123"


class Test__get_storage_emulator_override(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.storage._helpers import _get_storage_emulator_override

        return _get_storage_emulator_override()

    def test_wo_env_var(self):
        with mock.patch("os.environ", {}):
            override = self._call_fut()

        self.assertIsNone(override)

    def test_w_env_var(self):
        from google.cloud.storage._helpers import STORAGE_EMULATOR_ENV_VAR

        HOST = "https://api.example.com"

        with mock.patch("os.environ", {STORAGE_EMULATOR_ENV_VAR: HOST}):
            emu = self._call_fut()

        self.assertEqual(emu, HOST)


class Test__get_api_endpoint_override(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.storage._helpers import _get_api_endpoint_override

        return _get_api_endpoint_override()

    def test_wo_env_var(self):
        from google.cloud.storage._helpers import (
            _DEFAULT_SCHEME,
            _TRUE_DEFAULT_STORAGE_HOST,
        )

        with mock.patch("os.environ", {}):
            override = self._call_fut()

        self.assertIsNone(override, _DEFAULT_SCHEME + _TRUE_DEFAULT_STORAGE_HOST)

    def test_w_env_var(self):
        from google.cloud.storage._helpers import _API_ENDPOINT_OVERRIDE_ENV_VAR

        BASE_URL = "https://api.example.com"

        with mock.patch("os.environ", {_API_ENDPOINT_OVERRIDE_ENV_VAR: BASE_URL}):
            override = self._call_fut()

        self.assertEqual(override, BASE_URL)


class Test__get_environ_project(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.storage._helpers import _get_environ_project

        return _get_environ_project()

    def test_wo_env_var(self):
        with mock.patch("os.environ", {}):
            project = self._call_fut()

        self.assertEqual(project, None)

    def test_w_env_var(self):
        from google.auth import environment_vars

        PROJECT = "environ-project"

        with mock.patch("os.environ", {environment_vars.PROJECT: PROJECT}):
            project = self._call_fut()
        self.assertEqual(project, PROJECT)

        with mock.patch("os.environ", {environment_vars.LEGACY_PROJECT: PROJECT}):
            project = self._call_fut()

        self.assertEqual(project, PROJECT)


class Test_PropertyMixin(unittest.TestCase):
    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    @staticmethod
    def _get_target_class():
        from google.cloud.storage._helpers import _PropertyMixin

        return _PropertyMixin

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _derivedClass(self, path=None, user_project=None):
        class Derived(self._get_target_class()):
            client = None
            _actual_encryption_headers = None

            @property
            def path(self):
                return path

            @property
            def user_project(self):
                return user_project

            def _encryption_headers(self):
                return self._actual_encryption_headers or {}

        return Derived

    def test_path_is_abstract(self):
        mixin = self._make_one()
        with self.assertRaises(NotImplementedError):
            mixin.path

    def test_client_is_abstract(self):
        mixin = self._make_one()
        with self.assertRaises(NotImplementedError):
            mixin.client

    def test_user_project_is_abstract(self):
        mixin = self._make_one()
        with self.assertRaises(NotImplementedError):
            mixin.user_project

    def test__encryption_headers(self):
        mixin = self._make_one()
        self.assertEqual(mixin._encryption_headers(), {})

    def test__query_params_wo_user_project(self):
        derived = self._derivedClass("/path", None)()
        self.assertEqual(derived._query_params, {})

    def test__query_params_w_user_project(self):
        user_project = "user-project-123"
        derived = self._derivedClass("/path", user_project)()
        self.assertEqual(derived._query_params, {"userProject": user_project})

    def test_reload_w_defaults(self):
        path = "/path"
        response = {"foo": "Foo"}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = response
        derived = self._derivedClass(path)()
        # Make sure changes is not a set instance before calling reload
        # (which will clear / replace it with an empty set), checked below.
        derived._changes = object()
        derived.client = client

        derived.reload()

        self.assertEqual(derived._properties, response)
        self.assertEqual(derived._changes, set())

        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}  # no encryption headers by default
        client._get_resource.assert_called_once_with(
            path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test_reload_w_etag_match(self):
        etag = "kittens"
        path = "/path"
        response = {"foo": "Foo"}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = response
        derived = self._derivedClass(path)()
        # Make sure changes is not a set instance before calling reload
        # (which will clear / replace it with an empty set), checked below.
        derived._changes = object()
        derived.client = client

        derived.reload(
            if_etag_match=etag,
        )

        self.assertEqual(derived._properties, response)
        self.assertEqual(derived._changes, set())

        expected_query_params = {
            "projection": "noAcl",
        }
        # no encryption headers by default
        expected_headers = {
            "If-Match": etag,
        }
        client._get_resource.assert_called_once_with(
            path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test_reload_w_generation_match_w_timeout(self):
        generation_number = 9
        metageneration_number = 6
        path = "/path"
        timeout = 42
        response = {"foo": "Foo"}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = response
        derived = self._derivedClass(path)()
        # Make sure changes is not a set instance before calling reload
        # (which will clear / replace it with an empty set), checked below.
        derived._changes = object()
        derived.client = client

        derived.reload(
            if_generation_match=generation_number,
            if_metageneration_match=metageneration_number,
            timeout=timeout,
        )

        self.assertEqual(derived._properties, response)
        self.assertEqual(derived._changes, set())

        expected_query_params = {
            "projection": "noAcl",
            "ifGenerationMatch": generation_number,
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}  # no encryption headers by default
        client._get_resource.assert_called_once_with(
            path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test_reload_w_user_project_w_retry(self):
        user_project = "user-project-123"
        path = "/path"
        retry = mock.Mock(spec=[])
        response = {"foo": "Foo"}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = response
        derived = self._derivedClass(path, user_project)()
        # Make sure changes is not a set instance before calling reload
        # (which will clear / replace it with an empty set), checked below.
        derived._changes = object()
        derived.client = client

        derived.reload(retry=retry)

        self.assertEqual(derived._properties, response)
        self.assertEqual(derived._changes, set())

        expected_query_params = {
            "projection": "noAcl",
            "userProject": user_project,
        }
        expected_headers = {}  # no encryption headers by default
        client._get_resource.assert_called_once_with(
            path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=derived,
        )

    def test_reload_w_projection_w_explicit_client_w_enc_header(self):
        path = "/path"
        response = {"foo": "Foo"}
        encryption_headers = {"bar": "Bar"}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = response
        derived = self._derivedClass(path)()
        # Make sure changes is not a set instance before calling reload
        # (which will clear / replace it with an empty set), checked below.
        derived._changes = object()
        derived._actual_encryption_headers = encryption_headers

        derived.reload(projection="full", client=client)

        self.assertEqual(derived._properties, response)
        self.assertEqual(derived._changes, set())

        expected_query_params = {"projection": "full"}
        client._get_resource.assert_called_once_with(
            path,
            query_params=expected_query_params,
            headers=encryption_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test__set_properties(self):
        mixin = self._make_one()
        self.assertEqual(mixin._properties, {})
        VALUE = object()
        mixin._set_properties(VALUE)
        self.assertEqual(mixin._properties, VALUE)

    def test__patch_property(self):
        derived = self._derivedClass()()
        derived._patch_property("foo", "Foo")
        self.assertEqual(derived._properties, {"foo": "Foo"})

    def test_patch_w_defaults(self):
        path = "/path"
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Ignore baz.
        client = derived.client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response

        derived.patch()

        self.assertEqual(derived._properties, api_response)
        # Make sure changes get reset by patch().
        self.assertEqual(derived._changes, set())

        expected_data = {"bar": bar}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test_patch_w_metageneration_match_w_timeout_w_retry(self):
        path = "/path"
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Ignore baz.
        client = derived.client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        timeout = 42
        retry = mock.Mock(spec=[])
        generation_number = 9
        metageneration_number = 6
        override_unlocked_retention = True

        derived.patch(
            if_generation_match=generation_number,
            if_metageneration_match=metageneration_number,
            timeout=timeout,
            retry=retry,
            override_unlocked_retention=override_unlocked_retention,
        )

        self.assertEqual(derived._properties, {"foo": "Foo"})
        # Make sure changes get reset by patch().
        self.assertEqual(derived._changes, set())

        expected_data = {"bar": bar}
        expected_query_params = {
            "projection": "full",
            "ifGenerationMatch": generation_number,
            "ifMetagenerationMatch": metageneration_number,
            "overrideUnlockedRetention": override_unlocked_retention,
        }
        client._patch_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
            _target_object=derived,
        )

    def test_patch_w_user_project_w_explicit_client(self):
        path = "/path"
        user_project = "user-project-123"
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path, user_project)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Ignore baz.
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response

        derived.patch(client=client)

        self.assertEqual(derived._properties, {"foo": "Foo"})
        # Make sure changes get reset by patch().
        self.assertEqual(derived._changes, set())

        expected_data = {"bar": bar}
        expected_query_params = {
            "projection": "full",
            "userProject": user_project,
        }
        client._patch_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=derived,
        )

    def test_update_w_defaults(self):
        path = "/path"
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        expected_data = derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Update sends 'baz' anyway.
        client = derived.client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response

        derived.update()

        self.assertEqual(derived._properties, api_response)
        # Make sure changes get reset by update().
        self.assertEqual(derived._changes, set())

        expected_query_params = {"projection": "full"}
        client._put_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
            _target_object=derived,
        )

    def test_update_with_metageneration_not_match_w_timeout_w_retry(self):
        path = "/path"
        generation_number = 6
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        expected_data = derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Update sends 'baz' anyway.
        client = derived.client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        timeout = 42
        override_unlocked_retention = True

        derived.update(
            if_metageneration_not_match=generation_number,
            timeout=timeout,
            override_unlocked_retention=override_unlocked_retention,
        )

        self.assertEqual(derived._properties, {"foo": "Foo"})
        # Make sure changes get reset by patch().
        self.assertEqual(derived._changes, set())

        expected_query_params = {
            "projection": "full",
            "ifMetagenerationNotMatch": generation_number,
            "overrideUnlockedRetention": override_unlocked_retention,
        }
        client._put_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
            _target_object=derived,
        )

    def test_update_w_user_project_w_retry_w_explicit_client(self):
        user_project = "user-project-123"
        path = "/path"
        api_response = {"foo": "Foo"}
        derived = self._derivedClass(path, user_project)()
        # Make sure changes is non-empty, so we can observe a change.
        bar = object()
        baz = object()
        expected_data = derived._properties = {"bar": bar, "baz": baz}
        derived._changes = set(["bar"])  # Update sends 'baz' anyway.
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        retry = mock.Mock(spec=[])

        derived.update(client=client, retry=retry)
        # Make sure changes get reset by patch().
        self.assertEqual(derived._changes, set())

        expected_query_params = {
            "projection": "full",
            "userProject": user_project,
        }
        client._put_resource.assert_called_once_with(
            path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=derived,
        )


class Test__scalar_property(unittest.TestCase):
    def _call_fut(self, fieldName):
        from google.cloud.storage._helpers import _scalar_property

        return _scalar_property(fieldName)

    def test_getter(self):
        class Test(object):
            def __init__(self, **kw):
                self._properties = kw.copy()

            do_re_mi = self._call_fut("solfege")

        test = Test(solfege="Latido")
        self.assertEqual(test.do_re_mi, "Latido")

    def test_setter(self):
        class Test(object):
            def _patch_property(self, name, value):
                self._patched = (name, value)

            do_re_mi = self._call_fut("solfege")

        test = Test()
        test.do_re_mi = "Latido"
        self.assertEqual(test._patched, ("solfege", "Latido"))


class Test__base64_md5hash(unittest.TestCase):
    def _call_fut(self, bytes_to_sign):
        from google.cloud.storage._helpers import _base64_md5hash

        return _base64_md5hash(bytes_to_sign)

    def test_it(self):
        from io import BytesIO

        BYTES_TO_SIGN = b"FOO"
        BUFFER = BytesIO()
        BUFFER.write(BYTES_TO_SIGN)
        BUFFER.seek(0)

        SIGNED_CONTENT = self._call_fut(BUFFER)
        self.assertEqual(SIGNED_CONTENT, b"kBiQqOnIz21aGlQrIp/r/w==")

    def test_it_with_stubs(self):
        import mock

        class _Buffer(object):
            def __init__(self, return_vals):
                self.return_vals = return_vals
                self._block_sizes = []

            def read(self, block_size):
                self._block_sizes.append(block_size)
                return self.return_vals.pop()

        BASE64 = _Base64()
        DIGEST_VAL = object()
        BYTES_TO_SIGN = b"BYTES_TO_SIGN"
        BUFFER = _Buffer([b"", BYTES_TO_SIGN])
        MD5 = _MD5(DIGEST_VAL)

        patch = mock.patch.multiple(
            "google.cloud.storage._helpers", base64=BASE64, md5=MD5
        )
        with patch:
            SIGNED_CONTENT = self._call_fut(BUFFER)

        self.assertEqual(BUFFER._block_sizes, [8192, 8192])
        self.assertIs(SIGNED_CONTENT, DIGEST_VAL)
        self.assertEqual(BASE64._called_b64encode, [DIGEST_VAL])
        self.assertEqual(MD5._called, [None])
        self.assertEqual(MD5.hash_obj.num_digest_calls, 1)
        self.assertEqual(MD5.hash_obj._blocks, [BYTES_TO_SIGN])


class Test__add_etag_match_headers(unittest.TestCase):
    def _call_fut(self, headers, **match_params):
        from google.cloud.storage._helpers import _add_etag_match_headers

        return _add_etag_match_headers(headers, **match_params)

    def test_add_etag_match_parameters_str(self):
        ETAG = "kittens"
        headers = {"foo": "bar"}
        EXPECTED_HEADERS = {
            "foo": "bar",
            "If-Match": ETAG,
        }
        self._call_fut(headers, if_etag_match=ETAG)
        self.assertEqual(headers, EXPECTED_HEADERS)

    def test_add_generation_match_parameters_list(self):
        ETAGS = ["kittens", "fluffy"]
        EXPECTED_HEADERS = {
            "foo": "bar",
            "If-Match": ", ".join(ETAGS),
        }
        headers = {"foo": "bar"}
        self._call_fut(headers, if_etag_match=ETAGS)
        self.assertEqual(headers, EXPECTED_HEADERS)


class Test__add_generation_match_parameters(unittest.TestCase):
    def _call_fut(self, params, **match_params):
        from google.cloud.storage._helpers import _add_generation_match_parameters

        return _add_generation_match_parameters(params, **match_params)

    def test_add_generation_match_parameters_list(self):
        GENERATION_NUMBER = 9
        METAGENERATION_NUMBER = 6
        EXPECTED_PARAMS = [
            ("param1", "value1"),
            ("param2", "value2"),
            ("ifGenerationMatch", GENERATION_NUMBER),
            ("ifMetagenerationMatch", METAGENERATION_NUMBER),
        ]
        params = [("param1", "value1"), ("param2", "value2")]
        self._call_fut(
            params,
            if_generation_match=GENERATION_NUMBER,
            if_metageneration_match=METAGENERATION_NUMBER,
        )
        self.assertEqual(params, EXPECTED_PARAMS)

    def test_add_generation_match_parameters_dict(self):
        GENERATION_NUMBER = 9
        METAGENERATION_NUMBER = 6
        EXPECTED_PARAMS = {
            "param1": "value1",
            "param2": "value2",
            "ifGenerationMatch": GENERATION_NUMBER,
            "ifMetagenerationMatch": METAGENERATION_NUMBER,
        }

        params = {"param1": "value1", "param2": "value2"}
        self._call_fut(
            params,
            if_generation_match=GENERATION_NUMBER,
            if_metageneration_match=METAGENERATION_NUMBER,
        )
        self.assertEqual(params, EXPECTED_PARAMS)

    def test_add_generation_match_parameters_tuple(self):
        GENERATION_NUMBER = 9
        METAGENERATION_NUMBER = 6

        params = (("param1", "value1"), ("param2", "value2"))
        with self.assertRaises(ValueError):
            self._call_fut(
                params,
                if_generation_match=GENERATION_NUMBER,
                if_metageneration_match=METAGENERATION_NUMBER,
            )


class Test__bucket_bound_hostname_url(unittest.TestCase):
    def _call_fut(self, **args):
        from google.cloud.storage._helpers import _bucket_bound_hostname_url

        return _bucket_bound_hostname_url(**args)

    def test_full_hostname(self):
        HOST = "scheme://domain.tcl"
        self.assertEqual(self._call_fut(host=HOST), HOST)

    def test_hostname_and_scheme(self):
        HOST = "domain.tcl"
        SCHEME = "scheme"
        EXPECTED_URL = SCHEME + "://" + HOST

        self.assertEqual(self._call_fut(host=HOST, scheme=SCHEME), EXPECTED_URL)


class Test__parse_bool_env:
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._helpers import _parse_bool_env

        return _parse_bool_env(*args, **kwargs)

    def test_not_set_default_false(self):
        with mock.patch("os.getenv", return_value=None):
            assert not self._call_fut("TEST_VAR")

    def test_not_set_default_true(self):
        with mock.patch("os.getenv", return_value=None):
            assert self._call_fut("TEST_VAR", default=True)

    @pytest.mark.parametrize(
        "val",
        ("true", "True", "TRUE", "1", "yes", "YES", "on", "ON", " true "),
    )
    def test_truthy_values(self, val):
        with mock.patch("os.getenv", return_value=val):
            assert self._call_fut("TEST_VAR")

    @pytest.mark.parametrize(
        "val",
        (
            "false",
            "False",
            "FALSE",
            "0",
            "no",
            "NO",
            "off",
            "OFF",
            " false ",
        ),
    )
    def test_falsy_values(self, val):
        with mock.patch("os.getenv", return_value=val):
            assert not self._call_fut("TEST_VAR")

    @pytest.mark.parametrize("val", ("", "   ", "\t\n"))
    def test_empty_or_whitespace_raises(self, val):
        with mock.patch("os.getenv", return_value=val):
            with pytest.raises(ValueError, match="cannot be empty or whitespace-only"):
                self._call_fut("TEST_VAR")

    @pytest.mark.parametrize("val", ("invalid", "2", "foo", "bar"))
    def test_invalid_value_raises(self, val):
        with mock.patch("os.getenv", return_value=val):
            with pytest.raises(ValueError, match="Invalid value for TEST_VAR"):
                self._call_fut("TEST_VAR")


class _MD5Hash(object):
    def __init__(self, digest_val):
        self.digest_val = digest_val
        self.num_digest_calls = 0
        self._blocks = []

    def update(self, block):
        self._blocks.append(block)

    def digest(self):
        self.num_digest_calls += 1
        return self.digest_val


class _MD5(object):
    def __init__(self, digest_val):
        self.hash_obj = _MD5Hash(digest_val)
        self._called = []

    def __call__(self, data=None, usedforsecurity=True):
        self._called.append(data)
        return self.hash_obj


class _Base64(object):
    def __init__(self):
        self._called_b64encode = []

    def b64encode(self, value):
        self._called_b64encode.append(value)
        return value
