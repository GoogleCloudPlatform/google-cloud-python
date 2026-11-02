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

"""Credentials implementation for Spanner Omni using OPAQUE login authentication."""

from __future__ import annotations

import asyncio
import base64
import datetime
import logging
import threading
from collections import namedtuple
from typing import Any, Callable, MutableMapping, Optional, Sequence

import google.auth.credentials
import grpc
import grpc.aio

from google.cloud.spanner_v1.omni.login_client import LoginClient

_LOGGER = logging.getLogger(__name__)


class _ClientCallDetails(
    namedtuple(
        "_ClientCallDetails",
        ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
    ),
    grpc.ClientCallDetails,
):
    pass


class _OmniAuthInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    """gRPC client interceptor that automatically attaches Spanner Omni Bearer tokens."""

    def __init__(self, credentials: SpannerOmniCredentials) -> None:
        self._credentials = credentials

    def _add_metadata(
        self, client_call_details: grpc.ClientCallDetails
    ) -> grpc.ClientCallDetails:
        if not self._credentials.valid:
            self._credentials.refresh()
        token = self._credentials.token
        metadata = list(client_call_details.metadata or [])
        metadata.append(("authorization", f"Bearer {token}"))

        return _ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=metadata,
            credentials=client_call_details.credentials,
            wait_for_ready=getattr(client_call_details, "wait_for_ready", None),
        )

    def intercept_unary_unary(
        self,
        continuation: Callable,
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ) -> Any:
        return continuation(self._add_metadata(client_call_details), request)

    def intercept_unary_stream(
        self,
        continuation: Callable,
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ) -> Any:
        return continuation(self._add_metadata(client_call_details), request)

    def intercept_stream_unary(
        self,
        continuation: Callable,
        client_call_details: grpc.ClientCallDetails,
        request_iterator: Any,
    ) -> Any:
        return continuation(self._add_metadata(client_call_details), request_iterator)

    def intercept_stream_stream(
        self,
        continuation: Callable,
        client_call_details: grpc.ClientCallDetails,
        request_iterator: Any,
    ) -> Any:
        return continuation(self._add_metadata(client_call_details), request_iterator)


class _AsyncClientCallDetails(
    namedtuple(
        "_AsyncClientCallDetails",
        ["method", "timeout", "metadata", "credentials", "wait_for_ready"],
    ),
    grpc.aio.ClientCallDetails,
):
    pass


class _AsyncBaseAuthInterceptor:
    """Base helper for async auth interceptors."""

    def __init__(self, credentials: SpannerOmniCredentials) -> None:
        self._credentials = credentials

    async def _add_metadata(
        self, client_call_details: grpc.aio.ClientCallDetails
    ) -> grpc.aio.ClientCallDetails:
        if not self._credentials.valid:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self._credentials.refresh)
        token = self._credentials.token
        metadata = list(client_call_details.metadata or [])
        metadata.append(("authorization", f"Bearer {token}"))

        return _AsyncClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            metadata=metadata,
            credentials=client_call_details.credentials,
            wait_for_ready=getattr(client_call_details, "wait_for_ready", None),
        )


class _AsyncUnaryUnaryAuthInterceptor(
    _AsyncBaseAuthInterceptor, grpc.aio.UnaryUnaryClientInterceptor
):
    """Async gRPC interceptor for unary-unary calls."""

    async def intercept_unary_unary(
        self,
        continuation: Callable,
        client_call_details: grpc.aio.ClientCallDetails,
        request: Any,
    ) -> Any:
        return await continuation(
            await self._add_metadata(client_call_details), request
        )


class _AsyncUnaryStreamAuthInterceptor(
    _AsyncBaseAuthInterceptor, grpc.aio.UnaryStreamClientInterceptor
):
    """Async gRPC interceptor for unary-stream calls."""

    async def intercept_unary_stream(
        self,
        continuation: Callable,
        client_call_details: grpc.aio.ClientCallDetails,
        request: Any,
    ) -> Any:
        return await continuation(
            await self._add_metadata(client_call_details), request
        )


class _AsyncStreamUnaryAuthInterceptor(
    _AsyncBaseAuthInterceptor, grpc.aio.StreamUnaryClientInterceptor
):
    """Async gRPC interceptor for stream-unary calls."""

    async def intercept_stream_unary(
        self,
        continuation: Callable,
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: Any,
    ) -> Any:
        return await continuation(
            await self._add_metadata(client_call_details), request_iterator
        )


class _AsyncStreamStreamAuthInterceptor(
    _AsyncBaseAuthInterceptor, grpc.aio.StreamStreamClientInterceptor
):
    """Async gRPC interceptor for stream-stream calls."""

    async def intercept_stream_stream(
        self,
        continuation: Callable,
        client_call_details: grpc.aio.ClientCallDetails,
        request_iterator: Any,
    ) -> Any:
        return await continuation(
            await self._add_metadata(client_call_details), request_iterator
        )


class SpannerOmniCredentials(google.auth.credentials.Credentials):
    """Credentials for Spanner Omni authentication using the OPAQUE protocol.

    Args:
        username (str): The username for login.
        password (str | bytes): The password for login.
        target (str): The endpoint / target address for Spanner Omni.
        use_plain_text (bool): Whether to use an insecure (plaintext) connection.
        ca_certificate (str, optional): Path to the root CA certificate file.
        client_certificate (str, optional): Path to the client certificate file for mTLS.
        client_key (str, optional): Path to the client private key file for mTLS.
        ssl_credentials (grpc.ChannelCredentials, optional): Pre-constructed SSL channel credentials.
    """

    def __init__(
        self,
        username: str,
        password: str | bytes,
        target: str,
        use_plain_text: bool = False,
        ca_certificate: Optional[str] = None,
        client_certificate: Optional[str] = None,
        client_key: Optional[str] = None,
        ssl_credentials: Optional[grpc.ChannelCredentials] = None,
    ) -> None:
        super().__init__()
        if not username:
            raise ValueError("username cannot be empty")
        if not password:
            raise ValueError("password cannot be empty")
        if not target:
            raise ValueError("target cannot be empty")

        self.username = username
        self._password: bytes = (
            password.encode("utf-8") if isinstance(password, str) else bytes(password)
        )

        # Parse target scheme
        if target.startswith("http://"):
            self.target = target[7:]
            self.use_plain_text = True
            _LOGGER.warning("Using plaintext connection for Spanner Omni credentials.")
        elif target.startswith("https://"):
            self.target = target[8:]
            self.use_plain_text = use_plain_text
        else:
            self.target = target
            self.use_plain_text = use_plain_text

        self.ca_certificate = ca_certificate
        self.client_certificate = client_certificate
        self.client_key = client_key
        self.ssl_credentials = ssl_credentials

        self.token: Optional[str] = None
        self.expiry: Optional[datetime.datetime] = None
        self._lock = threading.Lock()

    def init_channel(
        self,
        use_plain_text: bool = False,
        ca_certificate: Optional[str] = None,
        client_certificate: Optional[str] = None,
        client_key: Optional[str] = None,
        ssl_credentials: Optional[grpc.ChannelCredentials] = None,
    ) -> None:
        """Initializes or updates channel TLS/transport settings."""
        self.use_plain_text = use_plain_text
        if self.use_plain_text:
            _LOGGER.warning("Using plaintext connection for Spanner Omni credentials.")
        self.ca_certificate = ca_certificate
        self.client_certificate = client_certificate
        self.client_key = client_key
        self.ssl_credentials = ssl_credentials

    def create_auth_interceptor(self, is_async: bool = False) -> Any:
        """Creates a gRPC interceptor that attaches the Bearer token."""
        if is_async:
            return self.create_async_auth_interceptors()
        return _OmniAuthInterceptor(self)

    def create_async_auth_interceptors(
        self,
    ) -> Sequence[grpc.aio.ClientInterceptor]:
        """Creates async gRPC interceptors that attach the Bearer token."""
        return [
            _AsyncUnaryUnaryAuthInterceptor(self),
            _AsyncUnaryStreamAuthInterceptor(self),
            _AsyncStreamUnaryAuthInterceptor(self),
            _AsyncStreamStreamAuthInterceptor(self),
        ]

    def create_async_auth_interceptor(
        self,
    ) -> Sequence[grpc.aio.ClientInterceptor]:
        """Creates async gRPC interceptors that attach the Bearer token."""
        return self.create_async_auth_interceptors()

    def _perform_refresh_token(self, request: Any = None) -> None:
        """Refreshes the access token by performing the OPAQUE login flow with Spanner Omni.

        Args:
            request (Any, optional): Unused; part of google.auth.credentials.Credentials interface.
        """
        with self._lock:
            if self.valid:
                return
            login_channel = None
            try:
                if self.use_plain_text:
                    login_channel = grpc.insecure_channel(self.target)
                elif self.ssl_credentials is not None:
                    login_channel = grpc.secure_channel(
                        self.target, self.ssl_credentials
                    )
                elif self.ca_certificate:
                    with open(self.ca_certificate, "rb") as f:
                        ca_cert = f.read()
                    if self.client_certificate and self.client_key:
                        with open(self.client_certificate, "rb") as f:
                            client_cert = f.read()
                        with open(self.client_key, "rb") as f:
                            private_key = f.read()
                        ssl_creds = grpc.ssl_channel_credentials(
                            root_certificates=ca_cert,
                            private_key=private_key,
                            certificate_chain=client_cert,
                        )
                    elif self.client_certificate or self.client_key:
                        raise ValueError(
                            "Both client_certificate and client_key must be provided for mTLS"
                        )
                    else:
                        ssl_creds = grpc.ssl_channel_credentials(
                            root_certificates=ca_cert
                        )
                    login_channel = grpc.secure_channel(self.target, ssl_creds)
                else:
                    raise ValueError(
                        "TLS/mTLS connection requires ca_certificate to be set for Spanner Omni"
                    )

                client = LoginClient(login_channel)
                proto_token = client.login(self.username, self._password)

                token_bytes = proto_token.SerializeToString()
                self.token = base64.b64encode(token_bytes).decode("ascii")

                if proto_token.HasField("expiration_time") and (
                    proto_token.expiration_time.seconds > 0
                    or proto_token.expiration_time.nanos > 0
                ):
                    seconds = proto_token.expiration_time.seconds
                    nanos = proto_token.expiration_time.nanos
                    self.expiry = datetime.datetime.fromtimestamp(
                        seconds + nanos / 1e9, tz=datetime.timezone.utc
                    ).replace(tzinfo=None)
                else:
                    self.expiry = datetime.datetime.now(datetime.timezone.utc).replace(
                        tzinfo=None
                    ) + datetime.timedelta(hours=1)
            except (grpc.RpcError, google.auth.exceptions.RefreshError):
                raise
            except Exception as e:
                raise google.auth.exceptions.RefreshError(
                    f"Failed to login to Spanner Omni: {e}"
                ) from e
            finally:
                if login_channel is not None:
                    login_channel.close()

    def refresh(self, request: Any = None) -> None:
        """Refreshes the access token.

        Args:
            request (Any, optional): Unused; part of google.auth.credentials.Credentials interface.
        """
        self._perform_refresh_token(request)

    def apply(
        self, headers: MutableMapping[str, str], token: Optional[str] = None
    ) -> None:
        """Applies the access token to request headers."""
        headers["authorization"] = f"Bearer {token or self.token}"

    def before_request(
        self,
        request: Any,
        method: str,
        url: str,
        headers: MutableMapping[str, str],
    ) -> None:
        """Performs token refresh if expired/missing and applies authorization header."""
        if not self.valid:
            self.refresh(request)
        self.apply(headers)
