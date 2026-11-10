# Copyright 2025 Google LLC All rights reserved.
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

import threading
from collections import deque

from google.longrunning import operations_pb2 as operations_pb2
from google.protobuf import empty_pb2

import tests.mockserver_tests.spanner_database_admin_pb2_grpc as database_admin_grpc


# An in-memory mock DatabaseAdmin server that can be used for testing.
class DatabaseAdminServicer(database_admin_grpc.DatabaseAdminServicer):
    """Thread-safe in-memory Spanner DatabaseAdmin servicer for mock tests."""

    def __init__(self):
        self._lock = threading.Lock()
        self._requests = []
        self._errors = deque()

    @property
    def requests(self):
        """Return a snapshot list of recorded UpdateDatabaseDdl requests."""
        with self._lock:
            return list(self._requests)

    def add_error(self, status_code, details="Injected DDL failure"):
        """Queue a gRPC error to abort the next UpdateDatabaseDdl call."""
        with self._lock:
            self._errors.append((status_code, details))

    def clear_requests(self):
        """Clear recorded UpdateDatabaseDdl requests and queued gRPC errors."""
        with self._lock:
            self._requests = []
            self._errors.clear()

    def UpdateDatabaseDdl(self, request, context):
        """Record an UpdateDatabaseDdl RPC or abort if an error was queued."""
        with self._lock:
            self._requests.append(request)
            queued_error = self._errors.popleft() if self._errors else None
        if queued_error is not None:
            status_code, details = queued_error
            context.abort(status_code, details)
        operation = operations_pb2.Operation()
        operation.done = True
        operation.name = "projects/test-project/operations/test-operation"
        operation.response.Pack(empty_pb2.Empty())
        return operation
