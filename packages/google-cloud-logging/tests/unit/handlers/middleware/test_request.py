# Copyright 2017 Google LLC All Rights Reserved.
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


class DjangoBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from django.conf import settings
        from django.test.utils import setup_test_environment

        if not settings.configured:
            settings.configure()
        setup_test_environment()

    @classmethod
    def tearDownClass(cls):
        from django.test.utils import teardown_test_environment

        teardown_test_environment()


class TestRequestMiddleware(DjangoBase):
    def _get_target_class(self):
        from google.cloud.logging_v2.handlers.middleware import request

        return request.RequestMiddleware

    def _make_one(self, *args, **kw):
        if not args and "get_response" not in kw:
            kw["get_response"] = None

        return self._get_target_class()(*args, **kw)

    def _mock_get_response(self, req):
        return req

    def test_process_request(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        middleware = self._make_one()
        mock_request = RequestFactory().get("/")
        middleware(mock_request)

        django_request = request._get_django_request()
        self.assertEqual(django_request, mock_request)

    def test_can_instantiate_middleware_without_kwargs(self):
        middleware = self._make_one(self._mock_get_response)
        mock_request = "test_req"
        self.assertEqual(middleware(mock_request), mock_request)

    def test_can_instantiate_middleware_with_kwargs(self):
        middleware = self._make_one(get_response=self._mock_get_response)
        mock_request = "test_req"
        self.assertEqual(middleware(mock_request), mock_request)


class Test__get_django_request(DjangoBase):
    @staticmethod
    def _call_fut():
        from google.cloud.logging_v2.handlers.middleware import request

        return request._get_django_request()

    @staticmethod
    def _make_patch(new_locals):
        return mock.patch(
            "google.cloud.logging_v2.handlers.middleware.request._thread_locals",
            new=new_locals,
        )

    def test_with_request(self):
        thread_locals = mock.Mock(spec=["request"])
        with self._make_patch(thread_locals):
            django_request = self._call_fut()

        self.assertIs(django_request, thread_locals.request)

    def test_without_request(self):
        thread_locals = mock.Mock(spec=[])
        with self._make_patch(thread_locals):
            django_request = self._call_fut()

        self.assertIsNone(django_request)
