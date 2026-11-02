# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC All rights reserved.
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


class TestLoggingShim(unittest.TestCase):
    def test_root_shim_matches_logging_v2(self):
        from google.cloud import logging, logging_v2

        self.assertEqual(logging.__all__, logging_v2.__all__)

        for name in logging.__all__:
            found = getattr(logging, name)
            expected = getattr(logging_v2, name)
            if name == "handlers":
                # handler has separate shim
                self.assertTrue(found)
                self.assertIs(type(found), type(expected))
            else:
                # other attributes should be identical
                self.assertIs(found, expected)

    def test_handler_shim_matches_logging_v2(self):
        from google.cloud.logging import handlers
        from google.cloud.logging_v2 import handlers as handlers_2

        self.assertEqual(handlers.__all__, handlers_2.__all__)

        for name in handlers.__all__:
            found = getattr(handlers, name)
            expected = getattr(handlers_2, name)
            self.assertIs(found, expected)

    def test_middleware_shim_matches_logging_v2(self):
        from google.cloud.logging.handlers import middleware
        from google.cloud.logging_v2.handlers import middleware as middleware_2

        self.assertEqual(middleware.__all__, middleware_2.__all__)

        for name in middleware.__all__:
            found = getattr(middleware, name)
            expected = getattr(middleware_2, name)
            self.assertIs(found, expected)

    def test_transports_shim_matches_logging_v2(self):
        from google.cloud.logging.handlers import transports
        from google.cloud.logging_v2.handlers import transports as transports_2

        self.assertEqual(transports.__all__, transports_2.__all__)

        for name in transports.__all__:
            found = getattr(transports, name)
            expected = getattr(transports_2, name)
            self.assertIs(found, expected)
