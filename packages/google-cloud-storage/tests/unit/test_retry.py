# Copyright 2020 Google LLC
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

from google.cloud.storage import _helpers
from google.cloud.storage.exceptions import InvalidResponse


class Test_should_retry(unittest.TestCase):
    def _call_fut(self, exc):
        from google.cloud.storage import retry

        return retry._should_retry(exc)

    def test_w_retryable_transport_error(self):
        from google.auth.exceptions import TransportError as eTransportError
        from requests import ConnectionError as rConnectionError

        from google.cloud.storage import retry

        caught_exc = rConnectionError("Remote end closed connection unexpected")
        exc = eTransportError(caught_exc)
        self.assertTrue(retry._should_retry(exc))

    def test_w_retryable_types(self):
        from google.cloud.storage import retry

        for exc_type in retry._RETRYABLE_TYPES:
            # Some of the types need one positional argument, some two.
            # The easiest way to accommodate both is just to use a try/except.
            try:
                exc = exc_type("testing")
            except TypeError:
                exc = exc_type("testing", "testing")
            self.assertTrue(self._call_fut(exc))

    def test_w_google_api_call_error_hit(self):
        from google.api_core import exceptions

        exc = exceptions.GoogleAPICallError("testing")
        exc.code = 408
        self.assertTrue(self._call_fut(exc))

    def test_w_google_api_call_error_miss(self):
        from google.api_core import exceptions

        exc = exceptions.GoogleAPICallError("testing")
        exc.code = 999
        self.assertFalse(self._call_fut(exc))

    def test_w_InvalidResponse_hit(self):
        response = mock.Mock()
        response.status_code = 408
        exc = InvalidResponse(response, "testing")
        self.assertTrue(self._call_fut(exc))

    def test_w_InvalidResponse_miss(self):
        response = mock.Mock()
        response.status_code = 999
        exc = InvalidResponse(response, "testing")
        self.assertFalse(self._call_fut(exc))

    def test_w_stdlib_error_miss(self):
        exc = ValueError("testing")
        self.assertFalse(self._call_fut(exc))


class TestConditionalRetryPolicy(unittest.TestCase):
    def _make_one(self, retry_policy, conditional_predicate, required_kwargs):
        from google.cloud.storage import retry

        return retry.ConditionalRetryPolicy(
            retry_policy, conditional_predicate, required_kwargs
        )

    def test_ctor(self):
        retry_policy = mock.Mock()
        conditional_predicate = mock.Mock()
        required_kwargs = ("kwarg",)

        policy = self._make_one(retry_policy, conditional_predicate, required_kwargs)

        self.assertIs(policy.retry_policy, retry_policy)
        self.assertIs(policy.conditional_predicate, conditional_predicate)
        self.assertEqual(policy.required_kwargs, required_kwargs)

    def test_get_retry_policy_if_conditions_met_single_kwarg_hit(self):
        retry_policy = mock.Mock()
        conditional_predicate = mock.Mock(return_value=True)
        required_kwargs = ("foo",)
        policy = self._make_one(retry_policy, conditional_predicate, required_kwargs)

        kwargs = {"foo": 1, "bar": 2, "baz": 3}
        result = policy.get_retry_policy_if_conditions_met(**kwargs)

        self.assertIs(result, retry_policy)

        conditional_predicate.assert_called_once_with(1)

    def test_get_retry_policy_if_conditions_met_multiple_kwargs_miss(self):
        retry_policy = mock.Mock()
        conditional_predicate = mock.Mock(return_value=False)
        required_kwargs = ("foo", "bar")
        policy = self._make_one(retry_policy, conditional_predicate, required_kwargs)

        kwargs = {"foo": 1, "bar": 2, "baz": 3}
        result = policy.get_retry_policy_if_conditions_met(**kwargs)

        self.assertIsNone(result)

        conditional_predicate.assert_called_once_with(1, 2)


class Test_is_generation_specified(unittest.TestCase):
    def _call_fut(self, query_params):
        from google.cloud.storage import retry

        return retry.is_generation_specified(query_params)

    def test_w_empty(self):
        query_params = {}

        self.assertFalse(self._call_fut(query_params))

    def test_w_generation(self):
        query_params = {"generation": 123}

        self.assertTrue(self._call_fut(query_params))

    def test_wo_generation_w_if_generation_match(self):
        query_params = {"ifGenerationMatch": 123}

        self.assertTrue(self._call_fut(query_params))


class Test_is_metageneration_specified(unittest.TestCase):
    def _call_fut(self, query_params):
        from google.cloud.storage import retry

        return retry.is_metageneration_specified(query_params)

    def test_w_empty(self):
        query_params = {}

        self.assertFalse(self._call_fut(query_params))

    def test_w_if_metageneration_match(self):
        query_params = {"ifMetagenerationMatch": 123}

        self.assertTrue(self._call_fut(query_params))


class Test_is_etag_in_data(unittest.TestCase):
    def _call_fut(self, data):
        from google.cloud.storage import retry

        return retry.is_etag_in_data(data)

    def test_w_none(self):
        data = None

        self.assertFalse(self._call_fut(data))

    def test_w_etag_in_data(self):
        data = {"etag": "123"}

        self.assertTrue(self._call_fut(data))

    def test_w_empty_data(self):
        data = {}

        self.assertFalse(self._call_fut(data))


class Test_default_conditional_retry_policies(unittest.TestCase):
    def test_is_generation_specified_match_generation_match(self):
        from google.cloud.storage import retry

        query_dict = {}
        _helpers._add_generation_match_parameters(query_dict, if_generation_match=1)

        conditional_policy = retry.DEFAULT_RETRY_IF_GENERATION_SPECIFIED
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params=query_dict
        )
        self.assertEqual(policy, retry.DEFAULT_RETRY)

    def test_is_generation_specified_match_generation(self):
        from google.cloud.storage import retry

        query_dict = {"generation": 1}

        conditional_policy = retry.DEFAULT_RETRY_IF_GENERATION_SPECIFIED
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params=query_dict
        )
        self.assertEqual(policy, retry.DEFAULT_RETRY)

    def test_is_generation_specified_mismatch(self):
        from google.cloud.storage import retry

        query_dict = {}
        _helpers._add_generation_match_parameters(query_dict, if_metageneration_match=1)

        conditional_policy = retry.DEFAULT_RETRY_IF_GENERATION_SPECIFIED
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params=query_dict
        )
        self.assertEqual(policy, None)

    def test_is_metageneration_specified_match(self):
        from google.cloud.storage import retry

        query_dict = {}
        _helpers._add_generation_match_parameters(query_dict, if_metageneration_match=1)

        conditional_policy = retry.DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params=query_dict
        )
        self.assertEqual(policy, retry.DEFAULT_RETRY)

    def test_is_metageneration_specified_mismatch(self):
        from google.cloud.storage import retry

        query_dict = {}
        _helpers._add_generation_match_parameters(query_dict, if_generation_match=1)

        conditional_policy = retry.DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params=query_dict
        )
        self.assertEqual(policy, None)

    def test_is_etag_in_json_etag_match(self):
        from google.cloud.storage import retry

        conditional_policy = retry.DEFAULT_RETRY_IF_ETAG_IN_JSON
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params={"ifGenerationMatch": 1}, data='{"etag": "12345678"}'
        )
        self.assertEqual(policy, retry.DEFAULT_RETRY)

    def test_is_etag_in_json_mismatch(self):
        from google.cloud.storage import retry

        conditional_policy = retry.DEFAULT_RETRY_IF_ETAG_IN_JSON
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params={"ifGenerationMatch": 1}, data="{}"
        )
        self.assertEqual(policy, None)

    def test_is_meta_or_etag_in_json_invalid(self):
        from google.cloud.storage import retry

        conditional_policy = retry.DEFAULT_RETRY_IF_ETAG_IN_JSON
        policy = conditional_policy.get_retry_policy_if_conditions_met(
            query_params={"ifGenerationMatch": 1}, data="I am invalid JSON!"
        )
        self.assertEqual(policy, None)
