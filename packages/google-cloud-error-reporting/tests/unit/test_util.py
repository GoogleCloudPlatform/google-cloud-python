# Copyright 2016 Google LLC All Rights Reserved.
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


class Test_build_flask_context(unittest.TestCase):
    def _call_fut(self, request):
        from google.cloud.error_reporting.util import build_flask_context

        return build_flask_context(request)

    def test_flask_helper(self):
        import mock

        user_agent = mock.Mock(string="Google Cloud Unit Tests Agent")
        request = _Request(
            "http://google.com", "GET", user_agent, "http://gmail.com", "127.0.0.1"
        )

        context = self._call_fut(request)
        self.assertEqual(request.url, context.url)
        self.assertEqual(request.method, context.method)
        self.assertEqual(request.user_agent.string, context.userAgent)
        self.assertEqual(request.referrer, context.referrer)
        self.assertEqual(request.remote_addr, context.remoteIp)


class _Request(object):
    def __init__(self, url, method, user_agent, referrer, remote_addr):
        self.url = url
        self.method = method
        self.user_agent = user_agent
        self.referrer = referrer
        self.remote_addr = remote_addr
