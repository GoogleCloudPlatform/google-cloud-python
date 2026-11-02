# Copyright 2025 Google LLC
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

import datetime
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from google.cloud.spanner_v1.omni.proto import authentication_pb2 as _authentication_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AccessToken(_message.Message):
    __slots__ = (
        "username",
        "creation_time",
        "expiration_time",
        "signature",
        "key_id",
        "access_token_type",
    )
    class AccessTokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_TOKEN_TYPE_UNSPECIFIED: _ClassVar[AccessToken.AccessTokenType]
        ACCESS_TOKEN_TYPE_API: _ClassVar[AccessToken.AccessTokenType]
        ACCESS_TOKEN_TYPE_UI: _ClassVar[AccessToken.AccessTokenType]

    ACCESS_TOKEN_TYPE_UNSPECIFIED: AccessToken.AccessTokenType
    ACCESS_TOKEN_TYPE_API: AccessToken.AccessTokenType
    ACCESS_TOKEN_TYPE_UI: AccessToken.AccessTokenType
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    username: str
    creation_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    signature: bytes
    key_id: int
    access_token_type: AccessToken.AccessTokenType
    def __init__(
        self,
        username: _Optional[str] = ...,
        creation_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        expiration_time: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        signature: _Optional[bytes] = ...,
        key_id: _Optional[int] = ...,
        access_token_type: _Optional[_Union[AccessToken.AccessTokenType, str]] = ...,
    ) -> None: ...

class InitialOpaqueLoginRequest(_message.Message):
    __slots__ = ("blinded_message", "client_nonce", "client_public_keyshare")
    BLINDED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NONCE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PUBLIC_KEYSHARE_FIELD_NUMBER: _ClassVar[int]
    blinded_message: bytes
    client_nonce: bytes
    client_public_keyshare: bytes
    def __init__(
        self,
        blinded_message: _Optional[bytes] = ...,
        client_nonce: _Optional[bytes] = ...,
        client_public_keyshare: _Optional[bytes] = ...,
    ) -> None: ...

class FinalOpaqueLoginRequest(_message.Message):
    __slots__ = ("client_mac",)
    CLIENT_MAC_FIELD_NUMBER: _ClassVar[int]
    client_mac: bytes
    def __init__(self, client_mac: _Optional[bytes] = ...) -> None: ...

class InitialOpaqueLoginResponse(_message.Message):
    __slots__ = (
        "server_nonce",
        "server_public_keyshare",
        "server_mac",
        "evaluated_message",
        "masking_nonce",
        "masked_response",
    )
    SERVER_NONCE_FIELD_NUMBER: _ClassVar[int]
    SERVER_PUBLIC_KEYSHARE_FIELD_NUMBER: _ClassVar[int]
    SERVER_MAC_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MASKING_NONCE_FIELD_NUMBER: _ClassVar[int]
    MASKED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    server_nonce: bytes
    server_public_keyshare: bytes
    server_mac: bytes
    evaluated_message: bytes
    masking_nonce: bytes
    masked_response: bytes
    def __init__(
        self,
        server_nonce: _Optional[bytes] = ...,
        server_public_keyshare: _Optional[bytes] = ...,
        server_mac: _Optional[bytes] = ...,
        evaluated_message: _Optional[bytes] = ...,
        masking_nonce: _Optional[bytes] = ...,
        masked_response: _Optional[bytes] = ...,
    ) -> None: ...

class OpaqueLoginRequest(_message.Message):
    __slots__ = ("initial_request", "final_request")
    INITIAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    initial_request: InitialOpaqueLoginRequest
    final_request: FinalOpaqueLoginRequest
    def __init__(
        self,
        initial_request: _Optional[_Union[InitialOpaqueLoginRequest, _Mapping]] = ...,
        final_request: _Optional[_Union[FinalOpaqueLoginRequest, _Mapping]] = ...,
    ) -> None: ...

class OpaqueLoginResponse(_message.Message):
    __slots__ = ("initial_response", "final_response")
    class FinalResponse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    INITIAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FINAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    initial_response: InitialOpaqueLoginResponse
    final_response: OpaqueLoginResponse.FinalResponse
    def __init__(
        self,
        initial_response: _Optional[_Union[InitialOpaqueLoginResponse, _Mapping]] = ...,
        final_response: _Optional[
            _Union[OpaqueLoginResponse.FinalResponse, _Mapping]
        ] = ...,
    ) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("username", "opaque_request", "handshake_request")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    username: str
    opaque_request: OpaqueLoginRequest
    handshake_request: _authentication_pb2.PasswordAuthenticationHandshakeRequest
    def __init__(
        self,
        username: _Optional[str] = ...,
        opaque_request: _Optional[_Union[OpaqueLoginRequest, _Mapping]] = ...,
        handshake_request: _Optional[
            _Union[_authentication_pb2.PasswordAuthenticationHandshakeRequest, _Mapping]
        ] = ...,
    ) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("access_token", "opaque_response", "handshake_response")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    access_token: AccessToken
    opaque_response: OpaqueLoginResponse
    handshake_response: _authentication_pb2.PasswordAuthenticationHandshakeResponse
    def __init__(
        self,
        access_token: _Optional[_Union[AccessToken, _Mapping]] = ...,
        opaque_response: _Optional[_Union[OpaqueLoginResponse, _Mapping]] = ...,
        handshake_response: _Optional[
            _Union[
                _authentication_pb2.PasswordAuthenticationHandshakeResponse, _Mapping
            ]
        ] = ...,
    ) -> None: ...
