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

from google.cloud.dataplex_v1.types import business_glossary, catalog

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "ChangeRequest",
        "DataProductAccessRequest",
    },
)


class ChangeRequest(proto.Message):
    r"""Represents a proposed change to a metadata resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The relative resource name of the ChangeRequest,
            of the form:
            projects/{project_number}/locations/{location_id}/changeRequests/{change_request_id}
        uid (str):
            Output only. System generated globally unique
            ID for the ChangeRequest.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the ChangeRequest
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the ChangeRequest
            was last updated.
        justification (str):
            Optional. Justification of the ChangeRequest. This should
            explain *why* the change is needed or why it should be
            approved.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            ChangeRequest.
        author (str):
            Output only. The email address of the user
            who created the ChangeRequest.
        state (google.cloud.dataplex_v1.types.ChangeRequest.State):
            Output only. The current state of the
            ChangeRequest.
        resource (str):
            Output only. The full resource name of the
            target resource to be modified. Example:

            //dataplex.googleapis.com/projects/my-project/locations/us-central1/entryGroups/my-group/entries/my-entry
        create_entry (google.cloud.dataplex_v1.types.CreateEntryRequest):
            Payload for creating an Entry.

            This field is a member of `oneof`_ ``change_payload``.
        update_entry (google.cloud.dataplex_v1.types.UpdateEntryRequest):
            Payload for updating an Entry.

            This field is a member of `oneof`_ ``change_payload``.
        delete_entry (google.cloud.dataplex_v1.types.DeleteEntryRequest):
            Payload for deleting an Entry.

            This field is a member of `oneof`_ ``change_payload``.
        create_entry_link (google.cloud.dataplex_v1.types.CreateEntryLinkRequest):
            Payload for creating an EntryLink.

            This field is a member of `oneof`_ ``change_payload``.
        delete_entry_link (google.cloud.dataplex_v1.types.DeleteEntryLinkRequest):
            Payload for deleting an EntryLink.

            This field is a member of `oneof`_ ``change_payload``.
        create_glossary (google.cloud.dataplex_v1.types.CreateGlossaryRequest):
            Payload for creating a Glossary.

            This field is a member of `oneof`_ ``change_payload``.
        update_glossary (google.cloud.dataplex_v1.types.UpdateGlossaryRequest):
            Payload for updating a Glossary.

            This field is a member of `oneof`_ ``change_payload``.
        delete_glossary (google.cloud.dataplex_v1.types.DeleteGlossaryRequest):
            Payload for deleting a Glossary.

            This field is a member of `oneof`_ ``change_payload``.
        create_glossary_category (google.cloud.dataplex_v1.types.CreateGlossaryCategoryRequest):
            Payload for creating a GlossaryCategory.

            This field is a member of `oneof`_ ``change_payload``.
        update_glossary_category (google.cloud.dataplex_v1.types.UpdateGlossaryCategoryRequest):
            Payload for updating a GlossaryCategory.

            This field is a member of `oneof`_ ``change_payload``.
        delete_glossary_category (google.cloud.dataplex_v1.types.DeleteGlossaryCategoryRequest):
            Payload for deleting a GlossaryCategory.

            This field is a member of `oneof`_ ``change_payload``.
        create_glossary_term (google.cloud.dataplex_v1.types.CreateGlossaryTermRequest):
            Payload for creating a GlossaryTerm.

            This field is a member of `oneof`_ ``change_payload``.
        update_glossary_term (google.cloud.dataplex_v1.types.UpdateGlossaryTermRequest):
            Payload for updating a GlossaryTerm.

            This field is a member of `oneof`_ ``change_payload``.
        delete_glossary_term (google.cloud.dataplex_v1.types.DeleteGlossaryTermRequest):
            Payload for deleting a GlossaryTerm.

            This field is a member of `oneof`_ ``change_payload``.
        data_product_access_request (google.cloud.dataplex_v1.types.DataProductAccessRequest):
            Payload for Data Product access request.

            This field is a member of `oneof`_ ``change_payload``.
        change_type (google.cloud.dataplex_v1.types.ChangeRequest.ChangeType):
            Output only. The type of change represented by the
            change_payload. This field is derived from the populated
            field in the change_payload oneof.
        rejection_comment (str):
            Output only. The reason provided for
            rejecting the ChangeRequest.
        approver (str):
            Output only. The email address of the user
            who approved/rejected the ChangeRequest.
        etag (str):
            Optional. This checksum is computed by the
            service. It can be sent on update and delete
            requests to ensure the client has an up-to-date
            value before proceeding.
    """

    class State(proto.Enum):
        r"""Possible states of a ChangeRequest.

        Values:
            STATE_UNSPECIFIED (0):
                State unspecified.
            NEW (1):
                The change is proposed and new.
            APPROVED (2):
                The change has been approved.
            REJECTED (3):
                The change has been rejected.
            EXPIRED (4):
                The change request has expired.
            REVOKED (5):
                The approved change has been revoked.
        """

        STATE_UNSPECIFIED = 0
        NEW = 1
        APPROVED = 2
        REJECTED = 3
        EXPIRED = 4
        REVOKED = 5

    class ChangeType(proto.Enum):
        r"""Enum representing the type of change in the payload.

        Values:
            CHANGE_TYPE_UNSPECIFIED (0):
                State unspecified.
            CREATE_ENTRY (1):
                Request to create an Entry.
            UPDATE_ENTRY (2):
                Request to update an Entry.
            DELETE_ENTRY (3):
                Request to delete an Entry.
            CREATE_ENTRY_LINK (4):
                Request to create an EntryLink.
            DELETE_ENTRY_LINK (5):
                Request to delete an EntryLink.
            CREATE_GLOSSARY (7):
                Request to create a Glossary.
            UPDATE_GLOSSARY (8):
                Request to update a Glossary.
            DELETE_GLOSSARY (9):
                Request to delete a Glossary.
            CREATE_GLOSSARY_CATEGORY (10):
                Request to create a GlossaryCategory.
            UPDATE_GLOSSARY_CATEGORY (11):
                Request to update a GlossaryCategory.
            DELETE_GLOSSARY_CATEGORY (13):
                Request to delete a GlossaryCategory.
            CREATE_GLOSSARY_TERM (14):
                Request to create a GlossaryTerm.
            UPDATE_GLOSSARY_TERM (15):
                Request to update a GlossaryTerm.
            DELETE_GLOSSARY_TERM (17):
                Request to delete a GlossaryTerm.
            REQUEST_DATA_PRODUCT_ACCESS (33):
                Request to request Data Product access.
        """

        CHANGE_TYPE_UNSPECIFIED = 0
        CREATE_ENTRY = 1
        UPDATE_ENTRY = 2
        DELETE_ENTRY = 3
        CREATE_ENTRY_LINK = 4
        DELETE_ENTRY_LINK = 5
        CREATE_GLOSSARY = 7
        UPDATE_GLOSSARY = 8
        DELETE_GLOSSARY = 9
        CREATE_GLOSSARY_CATEGORY = 10
        UPDATE_GLOSSARY_CATEGORY = 11
        DELETE_GLOSSARY_CATEGORY = 13
        CREATE_GLOSSARY_TERM = 14
        UPDATE_GLOSSARY_TERM = 15
        DELETE_GLOSSARY_TERM = 17
        REQUEST_DATA_PRODUCT_ACCESS = 33

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    justification: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    author: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_entry: catalog.CreateEntryRequest = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="change_payload",
        message=catalog.CreateEntryRequest,
    )
    update_entry: catalog.UpdateEntryRequest = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="change_payload",
        message=catalog.UpdateEntryRequest,
    )
    delete_entry: catalog.DeleteEntryRequest = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="change_payload",
        message=catalog.DeleteEntryRequest,
    )
    create_entry_link: catalog.CreateEntryLinkRequest = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="change_payload",
        message=catalog.CreateEntryLinkRequest,
    )
    delete_entry_link: catalog.DeleteEntryLinkRequest = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="change_payload",
        message=catalog.DeleteEntryLinkRequest,
    )
    create_glossary: business_glossary.CreateGlossaryRequest = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="change_payload",
        message=business_glossary.CreateGlossaryRequest,
    )
    update_glossary: business_glossary.UpdateGlossaryRequest = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="change_payload",
        message=business_glossary.UpdateGlossaryRequest,
    )
    delete_glossary: business_glossary.DeleteGlossaryRequest = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="change_payload",
        message=business_glossary.DeleteGlossaryRequest,
    )
    create_glossary_category: business_glossary.CreateGlossaryCategoryRequest = (
        proto.Field(
            proto.MESSAGE,
            number=23,
            oneof="change_payload",
            message=business_glossary.CreateGlossaryCategoryRequest,
        )
    )
    update_glossary_category: business_glossary.UpdateGlossaryCategoryRequest = (
        proto.Field(
            proto.MESSAGE,
            number=24,
            oneof="change_payload",
            message=business_glossary.UpdateGlossaryCategoryRequest,
        )
    )
    delete_glossary_category: business_glossary.DeleteGlossaryCategoryRequest = (
        proto.Field(
            proto.MESSAGE,
            number=26,
            oneof="change_payload",
            message=business_glossary.DeleteGlossaryCategoryRequest,
        )
    )
    create_glossary_term: business_glossary.CreateGlossaryTermRequest = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="change_payload",
        message=business_glossary.CreateGlossaryTermRequest,
    )
    update_glossary_term: business_glossary.UpdateGlossaryTermRequest = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="change_payload",
        message=business_glossary.UpdateGlossaryTermRequest,
    )
    delete_glossary_term: business_glossary.DeleteGlossaryTermRequest = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="change_payload",
        message=business_glossary.DeleteGlossaryTermRequest,
    )
    data_product_access_request: "DataProductAccessRequest" = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="change_payload",
        message="DataProductAccessRequest",
    )
    change_type: ChangeType = proto.Field(
        proto.ENUM,
        number=19,
        enum=ChangeType,
    )
    rejection_comment: str = proto.Field(
        proto.STRING,
        number=16,
    )
    approver: str = proto.Field(
        proto.STRING,
        number=17,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=18,
    )


class DataProductAccessRequest(proto.Message):
    r"""Message for requesting access to a Data Product. This will be used
    to create a ChangeRequest of type REQUEST_DATA_PRODUCT_ACCESS.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The resource name of the data product. Format:
            projects/{project_number}/locations/{location_id}/dataProducts/{data_product_id}
        access_group_id (str):
            Required. The ID of the access group for
            which access is being requested. This
            corresponds to the unique identifier of the
            AccessGroup defined in the Data Product.
        access_group_display_name (str):
            Output only. The display name of the access
            group defined in the Data Product for which
            access is being requested.
        requested_principal (str):
            Optional. The principal for which access is being requested
            in IAM format. If not specified, the requestor's principal
            will be used. Example:
            ``serviceAccount:my-sa@my-project.iam.gserviceaccount.com``.
            Only service account principals are currently supported.
            https://cloud.google.com/iam/docs/principal-identifiers

            This field is a member of `oneof`_ ``_requested_principal``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    access_group_display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    requested_principal: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
