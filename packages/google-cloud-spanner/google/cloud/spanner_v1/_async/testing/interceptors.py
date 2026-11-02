# Copyright 2024 Google LLC All rights reserved.
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
from collections import defaultdict

import grpc
from google.api_core.exceptions import Aborted

from google.cloud.spanner_v1.request_id_header import parse_request_id


class MethodCountAsyncInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self):
        self._counts = defaultdict(int)

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        self._counts[client_call_details.method] += 1
        return await continuation(client_call_details, request)

    def reset(self):
        self._counts = defaultdict(int)


class MethodAbortAsyncInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self):
        self._method_to_abort = None
        self._count = 0
        self._max_raise_count = 1
        self._connection = None

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        if (
            self._count < self._max_raise_count
            and client_call_details.method == self._method_to_abort
        ):
            self._count += 1
            if self._connection is not None:
                # Note: This assumes the connection rollback is sync or handled elsewhere
                # For async connection, we might need a different approach if rollback is async
                self._connection._transaction.rollback()
            raise Aborted("Thrown from Async ClientInterceptor for testing")
        return await continuation(client_call_details, request)

    def set_method_to_abort(self, method_to_abort, connection=None, max_raise_count=1):
        self._method_to_abort = method_to_abort
        self._count = 0
        self._max_raise_count = max_raise_count
        self._connection = connection

    def reset(self):
        self._method_to_abort = None
        self._count = 0
        self._connection = None


X_GOOG_REQUEST_ID = "x-goog-spanner-request-id"


class XGoogRequestIDHeaderAsyncInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self):
        self._unary_req_segments = []
        self._stream_req_segments = []
        self.__lock = threading.Lock()

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        metadata = client_call_details.metadata
        x_goog_request_id = None
        for key, value in metadata:
            if key == X_GOOG_REQUEST_ID:
                x_goog_request_id = value
                break

        if not x_goog_request_id:
            raise Exception(
                f"Missing {X_GOOG_REQUEST_ID} header in {client_call_details.method}"
            )

        with self.__lock:
            self._unary_req_segments.append(
                (client_call_details.method, parse_request_id(x_goog_request_id))
            )

        return await continuation(client_call_details, request)

    @property
    def unary_request_ids(self):
        return self._unary_req_segments

    @property
    def stream_request_ids(self):
        return self._stream_req_segments

    def reset(self):
        self._stream_req_segments.clear()
        self._unary_req_segments.clear()
