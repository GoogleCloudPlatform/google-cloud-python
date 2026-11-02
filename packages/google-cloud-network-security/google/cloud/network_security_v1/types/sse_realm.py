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
    package="google.cloud.networksecurity.v1",
    manifest={
        "SACRealm",
        "ListSACRealmsRequest",
        "ListSACRealmsResponse",
        "GetSACRealmRequest",
        "CreateSACRealmRequest",
        "DeleteSACRealmRequest",
        "SACAttachment",
        "ListSACAttachmentsRequest",
        "ListSACAttachmentsResponse",
        "GetSACAttachmentRequest",
        "CreateSACAttachmentRequest",
        "DeleteSACAttachmentRequest",
    },
)


class SACRealm(proto.Message):
    r"""Represents a Secure Access Connect (SAC) realm resource.

    A Secure Access Connect realm establishes a connection between
    your Google Cloud project and an SSE service.

    Attributes:
        name (str):
            Identifier. Resource name, in the form
            ``projects/{project}/locations/global/sacRealms/{sacRealm}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the realm was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the realm was
            last updated.
        labels (MutableMapping[str, str]):
            Optional. Optional list of labels applied to
            the resource.
        security_service (google.cloud.network_security_v1.types.SACRealm.SecurityService):
            Immutable. SSE service provider associated
            with the realm.
        pairing_key (google.cloud.network_security_v1.types.SACRealm.PairingKey):
            Output only. Key to be shared with SSE
            service provider during pairing.
        state (google.cloud.network_security_v1.types.SACRealm.State):
            Output only. State of the realm.
    """

    class SecurityService(proto.Enum):
        r"""SSE service provider

        Values:
            SECURITY_SERVICE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            PALO_ALTO_PRISMA_ACCESS (1):
                `Palo Alto Networks Prisma
                Access <https://www.paloaltonetworks.com/sase/access>`__.
        """

        SECURITY_SERVICE_UNSPECIFIED = 0
        PALO_ALTO_PRISMA_ACCESS = 1

    class State(proto.Enum):
        r"""State of the realm.

        Values:
            STATE_UNSPECIFIED (0):
                No state specified. This should not be used.
            PENDING_PARTNER_ATTACHMENT (7):
                Has never been attached to a partner.
                Used only for Prisma Access.
            PARTNER_ATTACHED (1):
                Currently attached to a partner.
            PARTNER_DETACHED (2):
                Was once attached to a partner but has been
                detached.
            KEY_EXPIRED (3):
                Is not attached to a partner and has an
                expired pairing key. Used only for Prisma
                Access.
        """

        STATE_UNSPECIFIED = 0
        PENDING_PARTNER_ATTACHMENT = 7
        PARTNER_ATTACHED = 1
        PARTNER_DETACHED = 2
        KEY_EXPIRED = 3

    class PairingKey(proto.Message):
        r"""Key to be shared with SSE service provider to establish
        global handshake.

        Attributes:
            key (str):
                Output only. Key value.
            expire_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Timestamp in UTC of when this
                resource is considered expired. It expires 7
                days after creation.
        """

        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        expire_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    security_service: SecurityService = proto.Field(
        proto.ENUM,
        number=5,
        enum=SecurityService,
    )
    pairing_key: PairingKey = proto.Field(
        proto.MESSAGE,
        number=6,
        message=PairingKey,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class ListSACRealmsRequest(proto.Message):
    r"""Request for ``ListSACRealms`` method.

    Attributes:
        parent (str):
            Required. The parent, in the form
            ``projects/{project}/locations/global``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression that filters the list
            of results.
        order_by (str):
            Optional. Sort the results by a certain
            order.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSACRealmsResponse(proto.Message):
    r"""Response for ``ListSACRealms`` method.

    Attributes:
        sac_realms (MutableSequence[google.cloud.network_security_v1.types.SACRealm]):
            The list of SACRealms.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    sac_realms: MutableSequence["SACRealm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SACRealm",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSACRealmRequest(proto.Message):
    r"""Request for ``GetSACRealm`` method.

    Attributes:
        name (str):
            Required. Name of the resource, in the form
            ``projects/{project}/locations/global/sacRealms/{sacRealm}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSACRealmRequest(proto.Message):
    r"""Request for ``CreateSACRealm`` method.

    Attributes:
        parent (str):
            Required. The parent, in the form
            ``projects/{project}/locations/global``.
        sac_realm_id (str):
            Required. ID of the created realm. The ID must be 1-63
            characters long, and comply with RFC1035. Specifically, it
            must be 1-63 characters long and match the regular
            expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` which means the
            first character must be a lowercase letter, and all
            following characters must be a dash, lowercase letter, or
            digit, except the last character, which cannot be a dash.
        sac_realm (google.cloud.network_security_v1.types.SACRealm):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sac_realm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sac_realm: "SACRealm" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SACRealm",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteSACRealmRequest(proto.Message):
    r"""Request for ``DeleteSACRealm`` method.

    Attributes:
        name (str):
            Required. Name of the resource, in the form
            ``projects/{project}/locations/global/sacRealms/{sacRealm}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SACAttachment(proto.Message):
    r"""Represents a Secure Access Connect (SAC) attachment resource.

    A Secure Access Connect attachment enables NCC Gateway to
    process traffic with an SSE product.

    Attributes:
        name (str):
            Identifier. Resource name, in the form
            ``projects/{project}/locations/{location}/sacAttachments/{sac_attachment}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the attachment
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the attachment
            was last updated.
        labels (MutableMapping[str, str]):
            Optional. Optional list of labels applied to
            the resource.
        sac_realm (str):
            Required. SAC Realm which owns the attachment. This can be
            input as an ID or a full resource name. The output always
            has the form
            ``projects/{project_number}/locations/{location}/sacRealms/{sac_realm}``.
        ncc_gateway (str):
            Required. NCC Gateway associated with the attachment. This
            can be input as an ID or a full resource name. The output
            always has the form
            ``projects/{project_number}/locations/{location}/spokes/{ncc_gateway}``.
        state (google.cloud.network_security_v1.types.SACAttachment.State):
            Output only. State of the attachment.
    """

    class State(proto.Enum):
        r"""State of the attachment.

        Values:
            STATE_UNSPECIFIED (0):
                No state specified. This should not be used.
            PENDING_PARTNER_ATTACHMENT (1):
                Has never been attached to a partner.
            PARTNER_ATTACHED (2):
                Currently attached to a partner.
            PARTNER_DETACHED (3):
                Was once attached to a partner but has been
                detached.
        """

        STATE_UNSPECIFIED = 0
        PENDING_PARTNER_ATTACHMENT = 1
        PARTNER_ATTACHED = 2
        PARTNER_DETACHED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    sac_realm: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ncc_gateway: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )


class ListSACAttachmentsRequest(proto.Message):
    r"""Request for ``ListSACAttachments`` method.

    Attributes:
        parent (str):
            Required. The parent, in the form
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression that filters the list
            of results.
        order_by (str):
            Optional. Sort the results by a certain
            order.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSACAttachmentsResponse(proto.Message):
    r"""Response for ``ListSACAttachments`` method.

    Attributes:
        sac_attachments (MutableSequence[google.cloud.network_security_v1.types.SACAttachment]):
            The list of SACAttachments.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    sac_attachments: MutableSequence["SACAttachment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SACAttachment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSACAttachmentRequest(proto.Message):
    r"""Request for ``GetSACAttachment`` method.

    Attributes:
        name (str):
            Required. Name of the resource, in the form
            ``projects/{project}/locations/{location}/sacAttachments/{sac_attachment}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSACAttachmentRequest(proto.Message):
    r"""Request for ``CreateSACAttachment`` method.

    Attributes:
        parent (str):
            Required. The parent, in the form
            ``projects/{project}/locations/{location}``.
        sac_attachment_id (str):
            Required. ID of the created attachment. The ID must be 1-63
            characters long, and comply with RFC1035. Specifically, it
            must be 1-63 characters long and match the regular
            expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` which means the
            first character must be a lowercase letter, and all
            following characters must be a dash, lowercase letter, or
            digit, except the last character, which cannot be a dash.
        sac_attachment (google.cloud.network_security_v1.types.SACAttachment):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sac_attachment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sac_attachment: "SACAttachment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SACAttachment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteSACAttachmentRequest(proto.Message):
    r"""Request for ``DeleteSACAttachment`` method.

    Attributes:
        name (str):
            Required. Name of the resource, in the form
            ``projects/{project}/locations/{location}/sacAttachments/{sac_attachment}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
