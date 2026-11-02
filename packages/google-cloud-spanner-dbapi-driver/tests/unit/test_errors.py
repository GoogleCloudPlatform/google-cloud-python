# Copyright 2026 Google LLC
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

from google.api_core import exceptions
from google.cloud.spannerlib.internal.errors import SpannerLibError

from google.cloud.spanner_driver import errors


class TestErrors(unittest.TestCase):
    def test_map_spanner_lib_error(self):
        err = SpannerLibError("Internal Error")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.DatabaseError)

    def test_map_not_found(self):
        err = exceptions.NotFound("Not found")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.ProgrammingError)

    def test_map_already_exists(self):
        err = exceptions.AlreadyExists("Exists")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.IntegrityError)

    def test_map_invalid_argument(self):
        err = exceptions.InvalidArgument("Invalid")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.ProgrammingError)

    def test_map_failed_precondition(self):
        err = exceptions.FailedPrecondition("Precondition")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.OperationalError)

    def test_map_out_of_range(self):
        err = exceptions.OutOfRange("OOR")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.DataError)

    def test_map_unknown(self):
        err = exceptions.Unknown("Unknown")
        mapped_err = errors.map_spanner_error(err)
        self.assertIsInstance(mapped_err, errors.DatabaseError)
