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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.agentidentitycredentials.v1",
    manifest={
        "RetrieveCredentialsRequest",
        "RetrieveCredentialsResponse",
        "FinalizeCredentialsRequest",
        "FinalizeCredentialsResponse",
    },
)


class RetrieveCredentialsRequest(proto.Message):
    r"""Request message for RetrieveCredentials.

    Attributes:
        auth_provider (str):
            Required. The parent resource name of the AuthProvider.
            Format:
            ``projects/{project}/locations/{location}/authProviders/{auth_provider}``
        user_id (str):
            Required. The identity of the end user.
        scopes (MutableSequence[str]):
            Optional. The OAuth scopes required for this
            access.
        continue_uri (str):
            Optional. The URI to redirect the user to
            after consent is completed. This field is
            required for authproviders using the 3-legged
            OAuth flow. For other authprovider types, this
            field is unused but not rejected.
        force_refresh_token (str):
            Optional. Input only. Set this field only if
            the previous token was expired or invalid. This
            value must be the full, previously returned
            token string. Will trigger a refresh of the
            access token with a stored refresh token, if
            possible, or a new consent flow.
    """

    auth_provider: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    continue_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    force_refresh_token: str = proto.Field(
        proto.STRING,
        number=7,
    )


class RetrieveCredentialsResponse(proto.Message):
    r"""Response message for RetrieveCredentials.
    Contains the access tokens and related artifacts.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        success (google.cloud.agentidentitycredentials_v1.types.RetrieveCredentialsResponse.Success):
            Message indicating credentials were
            successfully retrieved.

            This field is a member of `oneof`_ ``result``.
        pending (google.cloud.agentidentitycredentials_v1.types.RetrieveCredentialsResponse.Pending):
            Message indicating credential retrieval is
            pending.

            This field is a member of `oneof`_ ``result``.
        uri_consent_required (google.cloud.agentidentitycredentials_v1.types.RetrieveCredentialsResponse.UriConsentRequired):
            Message indicating uri based consent is
            required.

            This field is a member of `oneof`_ ``result``.
        consent_rejected (google.cloud.agentidentitycredentials_v1.types.RetrieveCredentialsResponse.ConsentRejected):
            Message indicating consent was rejected.

            This field is a member of `oneof`_ ``result``.
    """

    class Success(proto.Message):
        r"""Message indicating successful retrieval of credentials.

        Attributes:
            token (str):
                The retrieved access token or credential for the end user.

                On MCPTool call, for an invalid token OAuth spec says this
                should return 401 or 403, but MCPServers may implement this
                differently. If you get any flavor of ``PERMISSION_DENIED``,
                retry your original request to RetrieveCredentials with
                [force_refresh_token][google.cloud.agentidentitycredentials.v1.RetrieveCredentialsRequest.force_refresh_token]
                set to the expired/invalid token string, which will fetch a
                new token or initiate a new consent flow.
            header (str):
                The HTTP header name where the token should
                be placed.
            expire_time (google.protobuf.timestamp_pb2.Timestamp):
                The expiration time of the token.

                This does not guarantee that the token will be
                valid until this time, since the token could be
                revoked earlier. There could also be clock skew
                between the auth provider and the client so it
                may expire slightly earlier. If not set, the
                token might be permanent or it may be that the
                service does not (or cannot) know when it will
                expire.
            scopes (MutableSequence[str]):
                The scopes actually associated with the
                retrieved token.
                End users may have rejected some requested
                scopes, or the third-party authorization servers
                can return a different set of scopes than what
                was asked for. Callers should verify that all
                required scopes for their intended use are
                included in this list.
        """

        token: str = proto.Field(
            proto.STRING,
            number=1,
        )
        header: str = proto.Field(
            proto.STRING,
            number=2,
        )
        expire_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        scopes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class UriConsentRequired(proto.Message):
        r"""Indicates that the user must visit the provided URI to
        consent to delegate permission to the agent to act on their
        behalf. The caller can either poll the provided operation, or
        await the user ID validation callback

        Attributes:
            authorization_uri (str):
                Output only. The URL where the user should be
                redirected to grant consent. This will always be
                present.
            consent_nonce (str):
                Output only. A one-time, randomly generated
                value that validates the entire consent flow is
                handled by a single user, avoiding CSRF attacks.
                It must be submitted with the
                FinalizeCredentials request to complete the
                OAuth exchange. This will always be present.
                Implemented per
                https://www.rfc-editor.org/rfc/rfc6819#section-5.3.5
        """

        authorization_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        consent_nonce: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Pending(proto.Message):
        r"""Indicates that the credential retrieval is pending. The
        caller should retry the RetrieveCredentials request after some
        time.

        """

    class ConsentRejected(proto.Message):
        r"""Indicates the user has rejected the permission delegation or
        cancelled the request.

        """

    success: Success = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message=Success,
    )
    pending: Pending = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="result",
        message=Pending,
    )
    uri_consent_required: UriConsentRequired = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=UriConsentRequired,
    )
    consent_rejected: ConsentRejected = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="result",
        message=ConsentRejected,
    )


class FinalizeCredentialsRequest(proto.Message):
    r"""Request message for FinalizeCredentials.

    Attributes:
        auth_provider (str):
            Required. The resource name of the AuthProvider. Format:
            ``projects/{project}/locations/{location}/authProviders/{auth_provider}``
        user_id (str):
            Required. The identity of the end user.
        user_id_validation_state (bytes):
            Required. The encrypted state passed back
            from the consent flow.
        consent_nonce (str):
            Required. The same consent_nonce value that was provided
            during redirect in the UriConsentRequired metadata.
    """

    auth_provider: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_id_validation_state: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    consent_nonce: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FinalizeCredentialsResponse(proto.Message):
    r"""Response message for FinalizeCredentials. Intentionally empty"""


__all__ = tuple(sorted(__protobuf__.manifest))
