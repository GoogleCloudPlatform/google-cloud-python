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
    package="google.cloud.iamconnectorcredentials.v1alpha",
    manifest={
        "RetrieveCredentialsRequest",
        "RetrieveCredentialsResponse",
        "RetrieveCredentialsMetadata",
        "FinalizeCredentialsRequest",
        "FinalizeCredentialsResponse",
    },
)


class RetrieveCredentialsRequest(proto.Message):
    r"""Request message for RetrieveCredentials.

    Attributes:
        connector (str):
            Required. The parent resource name of the Connector. Format:
            ``projects/{project}/locations/{location}/connectors/{connector}``
        user_id (str):
            Required. The identity of the end user.
        scopes (MutableSequence[str]):
            Optional. The OAuth scopes required for this
            access.
        continue_uri (str):
            Optional. The URI to redirect the user to
            after consent is completed.
        force_refresh (bool):
            Optional. If true, forces fetching a fresh
            access token. Use only if the previously
            supplied token was expired or invalid. If the
            token cannot be refreshed without a login, the
            user is prompted for consent.
    """

    connector: str = proto.Field(
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
    force_refresh: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class RetrieveCredentialsResponse(proto.Message):
    r"""Response message for RetrieveCredentials.
    Contains the access tokens and related artifacts.

    Attributes:
        token (str):
            The retrieved access token or credential for the end user.

            On MCPTool call, for an invalid token OAuth spec says this
            should return 401 or 403, but MCPServers may implement this
            differently. If you get any flavor of ``PERMISSION_DENIED``,
            retry your original request to RetrieveCredentials with
            [force_refresh][google.cloud.iamconnectorcredentials.v1alpha.RetrieveCredentialsRequest.force_refresh]
            set to ``true``, which will fetch a new token or initiate a
            new consent flow.
        header (str):
            The HTTP header name where the token should
            be placed.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The expiration time of the token.

            This does not guarantee that the token will be
            valid until this time, since the token could be
            revoked earlier.
            There could also be clock skew between the auth
            provider and the client so it may expire
            slightly earlier.
            If not set, the token might be permanent or it
            may be that the service does not (or cannot)
            know when it will expire.
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


class RetrieveCredentialsMetadata(proto.Message):
    r"""Metadata for the RetrieveCredentials operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        consent_pending (google.cloud.iamconnectorcredentials_v1alpha.types.RetrieveCredentialsMetadata.ConsentPending):
            Message indicating consent is pending.

            This field is a member of `oneof`_ ``status``.
        uri_consent_required (google.cloud.iamconnectorcredentials_v1alpha.types.RetrieveCredentialsMetadata.UriConsentRequired):
            Message indicating uri based consent is
            required.

            This field is a member of `oneof`_ ``status``.
        consent_rejected (google.cloud.iamconnectorcredentials_v1alpha.types.RetrieveCredentialsMetadata.ConsentRejected):
            Message indicating consent was rejected.

            This field is a member of `oneof`_ ``status``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the operation was
            created.
    """

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

    class ConsentPending(proto.Message):
        r"""Indicates that the consent flow is pending external action.
        No action is required by the caller. Simply retry the
        RetrieveCredentials request.

        """

    class ConsentRejected(proto.Message):
        r"""Indicates the user has rejected the permission delegation or
        cancelled the request.

        """

    consent_pending: ConsentPending = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="status",
        message=ConsentPending,
    )
    uri_consent_required: UriConsentRequired = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="status",
        message=UriConsentRequired,
    )
    consent_rejected: ConsentRejected = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="status",
        message=ConsentRejected,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class FinalizeCredentialsRequest(proto.Message):
    r"""Request message for FinalizeCredentials.

    Attributes:
        connector (str):
            Required. The resource name of the Connector. Format:
            ``projects/{project}/locations/{location}/connectors/{connector}``
        user_id (str):
            Required. The identity of the end user.
        user_id_validation_state (bytes):
            Required. The encrypted state passed back
            from the consent flow.
        consent_nonce (str):
            Required. The same consent_nonce value that was provided
            during redirect in the UriConsentRequired metadata.
    """

    connector: str = proto.Field(
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
