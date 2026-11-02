# Copyright 2016 Google LLC
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


class TestBaseHandler(unittest.TestCase):
    PROJECT = "PROJECT"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging.handlers.transports import Transport

        return Transport

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_send_is_abstract(self):
        target = self._make_one("client", "name")
        with self.assertRaises(NotImplementedError):
            target.send(None, None, resource=None)

    def test_resource_is_valid_argunent(self):
        self._make_one("client", "name", resource="resource")

    def test_flush_is_abstract_and_optional(self):
        target = self._make_one("client", "name")
        target.flush()

    def test_close_is_abstract_and_optional(self):
        target = self._make_one("client", "name")
        target.close()
