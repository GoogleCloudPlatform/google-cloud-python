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

import asyncio
import importlib.util
import sys
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor

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
    def setUp(self):
        from google.cloud.logging_v2.handlers.middleware import request

        patch = mock.patch.object(request, "_thread_locals", request.Local())
        patch.start()
        self.addCleanup(patch.stop)

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

    def test_concurrent_async_requests(self):
        from google.cloud.logging_v2.handlers.middleware import request

        middleware = self._make_one()
        requests = [object(), object()]

        async def handle_requests():
            ready = [asyncio.Event(), asyncio.Event()]

            async def handle_request(index):
                middleware(requests[index])
                ready[index].set()
                await ready[1 - index].wait()
                return request._get_django_request()

            return await asyncio.gather(handle_request(0), handle_request(1))

        self.assertEqual(asyncio.run(handle_requests()), requests)
        self.assertIsNone(request._get_django_request())

    def test_async_view(self):
        from asgiref.sync import async_to_sync

        from google.cloud.logging_v2.handlers.middleware import request

        async def get_response(req):
            return request._get_django_request()

        middleware = self._make_one(async_to_sync(get_response))
        mock_request = object()
        self.assertIs(middleware(mock_request), mock_request)

    def test_sync_middleware_in_async_context(self):
        from asgiref.sync import sync_to_async

        from google.cloud.logging_v2.handlers.middleware import request

        middleware = self._make_one()
        mock_request = object()

        async def handle_request():
            await sync_to_async(middleware)(mock_request)
            return request._get_django_request()

        self.assertIs(asyncio.run(handle_request()), mock_request)

    def test_requests_are_thread_local(self):
        from google.cloud.logging_v2.handlers.middleware import request

        middleware = self._make_one()
        main_request = object()
        worker_request = object()
        middleware(main_request)

        def worker():
            self.assertIsNone(request._get_django_request())
            middleware(worker_request)
            self.assertIs(request._get_django_request(), worker_request)

        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(worker).result()

        self.assertIs(request._get_django_request(), main_request)


class TestRequestStorage(unittest.TestCase):
    def test_without_asgiref(self):
        from google.cloud.logging_v2.handlers.middleware import request

        spec = importlib.util.spec_from_file_location("request", request.__file__)
        module = importlib.util.module_from_spec(spec)
        with mock.patch.dict(sys.modules, {"asgiref.local": None}):
            spec.loader.exec_module(module)

        self.assertIsInstance(module._thread_locals, threading.local)
        self.assertIsNone(module._get_django_request())
        mock_request = object()
        middleware = module.RequestMiddleware(None)
        middleware(mock_request)
        self.assertIs(module._get_django_request(), mock_request)


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
