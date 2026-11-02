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

import sys
from unittest.mock import MagicMock

import google.cloud


# 1. Define Exception Classes
class MockGoogleAPICallError(Exception):
    def __init__(self, message=None, errors=None, response=None, **kwargs):
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.response = response
        self.reason = "reason"
        self.domain = "domain"
        self.metadata = {}
        self.details = []


class AlreadyExists(MockGoogleAPICallError):
    pass


class NotFound(MockGoogleAPICallError):
    pass


class InvalidArgument(MockGoogleAPICallError):
    pass


class FailedPrecondition(MockGoogleAPICallError):
    pass


class OutOfRange(MockGoogleAPICallError):
    pass


class Unauthenticated(MockGoogleAPICallError):
    pass


class PermissionDenied(MockGoogleAPICallError):
    pass


class DeadlineExceeded(MockGoogleAPICallError):
    pass


class ServiceUnavailable(MockGoogleAPICallError):
    pass


class Aborted(MockGoogleAPICallError):
    pass


class InternalServerError(MockGoogleAPICallError):
    pass


class Unknown(MockGoogleAPICallError):
    pass


class Cancelled(MockGoogleAPICallError):
    pass


class DataLoss(MockGoogleAPICallError):
    pass


class MockSpannerLibError(Exception):
    pass


# 2. Define Type/Proto Classes
class MockTypeCode:
    STRING = 1
    BYTES = 2
    BOOL = 3
    INT64 = 4
    FLOAT64 = 5
    DATE = 6
    TIMESTAMP = 7
    NUMERIC = 8
    JSON = 9
    PROTO = 10
    ENUM = 11


class MockExecuteSqlRequest:
    def __init__(self, sql=None, params=None):
        self.sql = sql
        self.params = params


class MockType:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return isinstance(other, MockType) and self.code == other.code

    def __repr__(self):
        return f"MockType(code={self.code})"


class MockStructField:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_  # Avoid conflict with builtin type

    def __eq__(self, other):
        return (
            isinstance(other, MockStructField)
            and self.name == other.name
            and self.type == other.type
        )


class MockStructType:
    def __init__(self, fields):
        self.fields = fields


# 3. Create Module Mocks
# google.cloud.spanner_v1
spanner_v1 = MagicMock()
spanner_v1.TypeCode = MockTypeCode
spanner_v1.ExecuteSqlRequest = MockExecuteSqlRequest
spanner_v1.Type = MockType
spanner_v1.StructField = MockStructField
spanner_v1.StructType = MockStructType

# google.cloud.spanner_v1.types
spanner_v1_types = MagicMock()
spanner_v1_types.Type = MockType
spanner_v1_types.StructField = MockStructField
spanner_v1_types.StructType = MockStructType

# google.api_core.exceptions
exceptions_module = MagicMock()
exceptions_module.GoogleAPICallError = MockGoogleAPICallError
exceptions_module.AlreadyExists = AlreadyExists
exceptions_module.NotFound = NotFound
exceptions_module.InvalidArgument = InvalidArgument
exceptions_module.FailedPrecondition = FailedPrecondition
exceptions_module.OutOfRange = OutOfRange
exceptions_module.Unauthenticated = Unauthenticated
exceptions_module.PermissionDenied = PermissionDenied
exceptions_module.DeadlineExceeded = DeadlineExceeded
exceptions_module.ServiceUnavailable = ServiceUnavailable
exceptions_module.Aborted = Aborted
exceptions_module.InternalServerError = InternalServerError
exceptions_module.Unknown = Unknown
exceptions_module.Cancelled = Cancelled
exceptions_module.DataLoss = DataLoss

# google.cloud.spannerlib
spannerlib = MagicMock()
# internal.errors
spannerlib_internal_errors = MagicMock()
spannerlib_internal_errors.SpannerLibError = MockSpannerLibError
spannerlib.internal.errors = spannerlib_internal_errors

# pool
spannerlib_pool = MagicMock()
spannerlib.pool = spannerlib_pool


# pool.Pool class
class MockPool:
    @staticmethod
    def create_pool(connection_string):
        return MockPool()

    def create_connection(self):
        return MagicMock()


spannerlib.pool.Pool = MockPool

# connection
spannerlib_connection = MagicMock()
spannerlib.connection = spannerlib_connection

# 4. Inject into sys.modules
sys.modules["google.cloud.spanner_v1"] = spanner_v1
sys.modules["google.cloud.spanner_v1.types"] = spanner_v1_types
sys.modules["google.api_core.exceptions"] = exceptions_module
sys.modules["google.api_core"] = MagicMock(exceptions=exceptions_module)
sys.modules["google.cloud.spannerlib"] = spannerlib
sys.modules["google.cloud.spannerlib.internal"] = spannerlib.internal
sys.modules["google.cloud.spannerlib.internal.errors"] = spannerlib_internal_errors
sys.modules["google.cloud.spannerlib.pool"] = spannerlib_pool
sys.modules["google.cloud.spannerlib.connection"] = spannerlib_connection


# 4. Patch google.cloud
# This is tricky because google is a namespace package
# but spannerlib might need to be explicitly set in google.cloud
google.cloud.spannerlib = spannerlib
google.cloud.spanner_v1 = spanner_v1
