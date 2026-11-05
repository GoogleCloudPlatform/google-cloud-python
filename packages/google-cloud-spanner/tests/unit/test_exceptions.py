# Copyright 2026 Google LLC All rights reserved.
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

"""Tests for Spanner exception handling with request IDs."""

import unittest

from google.api_core.exceptions import Aborted

from google.cloud.spanner_v1.exceptions import wrap_with_request_id


class TestWrapWithRequestId(unittest.TestCase):
    """Test wrap_with_request_id function."""

    def test_wrap_with_request_id_with_google_api_error(self):
        """Test adding request_id to GoogleAPICallError preserves original type."""
        error = Aborted("Transaction aborted")
        request_id = "1.12345.1.0.1.1"

        result = wrap_with_request_id(error, request_id)

        # Should return the same error object (not wrapped)
        self.assertIs(result, error)
        # Should still be the original exception type
        self.assertIsInstance(result, Aborted)
        # Should have request_id attribute
        self.assertEqual(result.request_id, request_id)
        # String representation should include request_id
        self.assertIn(request_id, str(result))
        self.assertIn("Transaction aborted", str(result))

    def test_wrap_with_request_id_without_request_id(self):
        """Test that without request_id, error is returned unchanged."""
        error = Aborted("Transaction aborted")

        result = wrap_with_request_id(error)

        self.assertIs(result, error)
        self.assertFalse(hasattr(result, "request_id"))

    def test_wrap_with_request_id_with_non_google_api_error(self):
        """Test that non-GoogleAPICallError is returned unchanged."""
        error = Exception("Some other error")
        request_id = "1.12345.1.0.1.1"

        result = wrap_with_request_id(error, request_id)

        # Non-GoogleAPICallError should be returned unchanged
        self.assertIs(result, error)
        self.assertFalse(hasattr(result, "request_id"))

    def test_wrap_with_request_id_idempotent_and_retry(self):
        """Test that re-wrapping does not duplicate request_id suffix and updates on retry."""
        error = Aborted("Transaction aborted")
        req_id_1 = "1.12345.1.0.1.1"
        req_id_2 = "1.12345.1.0.1.2"

        # First wrap
        wrap_with_request_id(error, req_id_1)
        self.assertEqual(error.request_id, req_id_1)
        self.assertEqual(error.message, f"Transaction aborted, request_id = {req_id_1}")

        # Wrapping again with the same request_id should be a no-op
        wrap_with_request_id(error, req_id_1)
        self.assertEqual(error.request_id, req_id_1)
        self.assertEqual(error.message, f"Transaction aborted, request_id = {req_id_1}")

        # Wrapping with a new request_id on retry should replace the old request_id in message
        wrap_with_request_id(error, req_id_2)
        self.assertEqual(error.request_id, req_id_2)
        self.assertEqual(error.message, f"Transaction aborted, request_id = {req_id_2}")

        # Wrapping error with empty message sets request_id attribute without altering empty message
        empty_err = Aborted("")
        wrap_with_request_id(empty_err, req_id_1)
        self.assertEqual(empty_err.request_id, req_id_1)
        self.assertEqual(empty_err.message, "")

        # Wrapping error with non-string message (e.g. int/mock) sets request_id without raising TypeError
        non_str_err = Aborted("msg")
        non_str_err.message = 12345
        wrap_with_request_id(non_str_err, req_id_1)
        self.assertEqual(non_str_err.request_id, req_id_1)
        self.assertEqual(non_str_err.message, 12345)


if __name__ == "__main__":
    unittest.main()
