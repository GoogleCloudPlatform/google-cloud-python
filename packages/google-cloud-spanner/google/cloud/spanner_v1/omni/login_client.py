# -*- coding: utf-8 -*-
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
#

"""Client for Spanner Omni LoginService gRPC API."""

from __future__ import annotations

import queue
from typing import Iterator, Optional

import grpc

from google.cloud.spanner_v1.omni.opaque import (
    EXPECTED_ENVELOPE_SIZE,
    UserAuthenticator,
)
from google.cloud.spanner_v1.omni.proto import (
    authentication_pb2,
    login_pb2,
    login_pb2_grpc,
)


class _RequestIterator(Iterator[login_pb2.LoginRequest]):
    """Thread-safe request iterator for gRPC bidirectional streaming."""

    def __init__(self) -> None:
        self._queue: queue.Queue[Optional[login_pb2.LoginRequest]] = queue.Queue()
        self._closed = False

    def send(self, request: login_pb2.LoginRequest) -> None:
        self._queue.put(request)

    def close(self) -> None:
        if not self._closed:
            self._closed = True
            self._queue.put(None)

    def __iter__(self) -> _RequestIterator:
        return self

    def __next__(self) -> login_pb2.LoginRequest:
        item = self._queue.get()
        if item is None:
            raise StopIteration
        return item


class LoginClient:
    """Client for Spanner Omni LoginService."""

    EXPECTED_ENVELOPE_SIZE = EXPECTED_ENVELOPE_SIZE

    def __init__(self, channel: grpc.Channel) -> None:
        self._stub = login_pb2_grpc.LoginServiceStub(channel)

    def login(
        self, username: str, password: str | bytes, timeout: float = 60.0
    ) -> login_pb2.AccessToken:
        """Performs the full OPAQUE authentication handshake and returns an AccessToken.

        Args:
            username (str): The username for login.
            password (str | bytes): The password for login.
            timeout (float): RPC timeout in seconds.

        Returns:
            login_pb2.AccessToken: The issued access token proto.

        Raises:
            ValueError: If handshake validation fails.
            grpc.RpcError: If gRPC communication fails.
        """
        if not username:
            raise ValueError("username cannot be empty")
        if not password:
            raise ValueError("password cannot be empty")

        req_iterator = _RequestIterator()
        try:
            call = self._stub.Login(req_iterator, timeout=timeout)

            def _safe_next(stage: str) -> login_pb2.LoginResponse:
                try:
                    return next(call)
                except StopIteration:
                    raise ValueError(f"Server closed stream prematurely during {stage}")

            # Step 1: Handshake Request
            handshake_req = login_pb2.LoginRequest(
                username=username,
                handshake_request=authentication_pb2.PasswordAuthenticationHandshakeRequest(),
            )
            req_iterator.send(handshake_req)
            handshake_resp = _safe_next("handshake")

            if not handshake_resp.HasField("handshake_response"):
                raise ValueError("Failed to receive handshake response from server")

            method = handshake_resp.handshake_response.password_authentication_protocol
            if (
                method
                != authentication_pb2.PasswordAuthenticationProtocol.PASSWORD_AUTHENTICATION_PROTOCOL_OPAQUE
            ):
                raise ValueError(
                    f"Unsupported password authentication protocol: {method}"
                )

            if not handshake_resp.handshake_response.HasField("hash_parameters"):
                raise ValueError("Handshake response missing hash_parameters")

            hash_params = handshake_resp.handshake_response.hash_parameters
            authenticator = UserAuthenticator(username, password, hash_params)

            # Step 2: Initial OPAQUE Request
            initial_req = authenticator.initial_request()
            req_iterator.send(initial_req)
            initial_resp = _safe_next("initial OPAQUE exchange")

            # Step 3: Final OPAQUE Request
            final_req = authenticator.final_request(initial_resp)
            req_iterator.send(final_req)
            req_iterator.close()

            # Final Response with AccessToken
            final_resp = _safe_next("final OPAQUE exchange")
            if not final_resp.HasField("access_token"):
                raise ValueError(
                    "Server failed to return an access token in final response"
                )

            return final_resp.access_token
        except Exception:
            if "call" in locals() and hasattr(call, "cancel"):
                call.cancel()
            req_iterator.close()
            raise
