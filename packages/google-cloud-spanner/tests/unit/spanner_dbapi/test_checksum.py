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


class Test_compare_checksums(unittest.TestCase):
    def test_equal(self):
        from google.cloud.spanner_dbapi.checksum import (
            ResultsChecksum,
            _compare_checksums,
        )

        original = ResultsChecksum()
        original.consume_result(5)

        retried = ResultsChecksum()
        retried.consume_result(5)

        self.assertIsNone(_compare_checksums(original, retried))

    def test_less_results(self):
        from google.cloud.spanner_dbapi.checksum import (
            ResultsChecksum,
            _compare_checksums,
        )
        from google.cloud.spanner_dbapi.exceptions import RetryAborted

        original = ResultsChecksum()
        original.consume_result(5)

        retried = ResultsChecksum()

        with self.assertRaises(RetryAborted):
            _compare_checksums(original, retried)

    def test_more_results(self):
        from google.cloud.spanner_dbapi.checksum import (
            ResultsChecksum,
            _compare_checksums,
        )
        from google.cloud.spanner_dbapi.exceptions import RetryAborted

        original = ResultsChecksum()
        original.consume_result(5)

        retried = ResultsChecksum()
        retried.consume_result(5)
        retried.consume_result(2)

        with self.assertRaises(RetryAborted):
            _compare_checksums(original, retried)

    def test_mismatch(self):
        from google.cloud.spanner_dbapi.checksum import (
            ResultsChecksum,
            _compare_checksums,
        )
        from google.cloud.spanner_dbapi.exceptions import RetryAborted

        original = ResultsChecksum()
        original.consume_result(5)

        retried = ResultsChecksum()
        retried.consume_result(2)

        with self.assertRaises(RetryAborted):
            _compare_checksums(original, retried)
