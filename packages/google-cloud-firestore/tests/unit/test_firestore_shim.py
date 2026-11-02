# -*- coding: utf-8 -*-
# Copyright 2017 Google LLC All rights reserved.
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


class TestFirestoreShim(unittest.TestCase):
    def test_version_from_gapic_version_meatches_firestore_v1(self):
        from google.cloud.firestore import gapic_version
        from google.cloud.firestore_v1 import gapic_version as gapic_version_v1

        self.assertEqual(gapic_version.__version__, gapic_version_v1.__version__)

    def test_shim_matches_firestore_v1(self):
        from google.cloud import firestore, firestore_v1

        self.assertEqual(firestore.__all__, firestore_v1.__all__)

        for name in firestore.__all__:
            found = getattr(firestore, name)
            expected = getattr(firestore_v1, name)
            self.assertIs(found, expected)
