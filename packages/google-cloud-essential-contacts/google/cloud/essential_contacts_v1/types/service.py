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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.essential_contacts_v1.types import enums

__protobuf__ = proto.module(
    package="google.cloud.essentialcontacts.v1",
    manifest={
        "Contact",
        "ListContactsRequest",
        "ListContactsResponse",
        "GetContactRequest",
        "DeleteContactRequest",
        "CreateContactRequest",
        "UpdateContactRequest",
        "ComputeContactsRequest",
        "ComputeContactsResponse",
        "SendTestMessageRequest",
    },
)


class Contact(proto.Message):
    r"""A contact that will receive notifications from Google Cloud.

    Attributes:
        name (str):
            Output only. The identifier for the contact. Format:
            {resource_type}/{resource_id}/contacts/{contact_id}
        email (str):
            Required. The email address to send
            notifications to. The email address does not
            need to be a Google Account.
        notification_category_subscriptions (MutableSequence[google.cloud.essential_contacts_v1.types.NotificationCategory]):
            Required. The categories of notifications
            that the contact will receive communications
            for.
        language_tag (str):
            Required. The preferred language for notifications, as a ISO
            639-1 language code. See `Supported
            languages <https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages>`__
            for a list of supported languages.
        validation_state (google.cloud.essential_contacts_v1.types.ValidationState):
            Output only. The validity of the contact. A
            contact is considered valid if it is the correct
            recipient for notifications for a particular
            resource.
        validate_time (google.protobuf.timestamp_pb2.Timestamp):
            The last time the validation_state was updated, either
            manually or automatically. A contact is considered stale if
            its validation state was updated more than 1 year ago.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    notification_category_subscriptions: MutableSequence[enums.NotificationCategory] = (
        proto.RepeatedField(
            proto.ENUM,
            number=3,
            enum=enums.NotificationCategory,
        )
    )
    language_tag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validation_state: enums.ValidationState = proto.Field(
        proto.ENUM,
        number=8,
        enum=enums.ValidationState,
    )
    validate_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class ListContactsRequest(proto.Message):
    r"""Request message for the ListContacts method.

    Attributes:
        parent (str):
            Required. The parent resource name. Format:
            organizations/{organization_id}, folders/{folder_id} or
            projects/{project_id}
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``next_page_token`` in the response indicates that more
            results might be available. If not specified, the default
            page_size is 100.
        page_token (str):
            Optional. If present, retrieves the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of other method parameters should be
            identical to those in the previous call.
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


class ListContactsResponse(proto.Message):
    r"""Response message for the ListContacts method.

    Attributes:
        contacts (MutableSequence[google.cloud.essential_contacts_v1.types.Contact]):
            The contacts for the specified resource.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token`` and the rest of the
            parameters the same as the original request.
    """

    @property
    def raw_page(self):
        return self

    contacts: MutableSequence["Contact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Contact",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetContactRequest(proto.Message):
    r"""Request message for the GetContact method.

    Attributes:
        name (str):
            Required. The name of the contact to retrieve. Format:
            organizations/{organization_id}/contacts/{contact_id},
            folders/{folder_id}/contacts/{contact_id} or
            projects/{project_id}/contacts/{contact_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteContactRequest(proto.Message):
    r"""Request message for the DeleteContact method.

    Attributes:
        name (str):
            Required. The name of the contact to delete. Format:
            organizations/{organization_id}/contacts/{contact_id},
            folders/{folder_id}/contacts/{contact_id} or
            projects/{project_id}/contacts/{contact_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateContactRequest(proto.Message):
    r"""Request message for the CreateContact method.

    Attributes:
        parent (str):
            Required. The resource to save this contact for. Format:
            organizations/{organization_id}, folders/{folder_id} or
            projects/{project_id}
        contact (google.cloud.essential_contacts_v1.types.Contact):
            Required. The contact to create. Must specify
            an email address and language tag.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    contact: "Contact" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Contact",
    )


class UpdateContactRequest(proto.Message):
    r"""Request message for the UpdateContact method.

    Attributes:
        contact (google.cloud.essential_contacts_v1.types.Contact):
            Required. The contact resource to replace the
            existing saved contact. Note: the email address
            of the contact cannot be modified.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The update mask applied to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    contact: "Contact" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Contact",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class ComputeContactsRequest(proto.Message):
    r"""Request message for the ComputeContacts method.

    Attributes:
        parent (str):
            Required. The name of the resource to compute contacts for.
            Format: organizations/{organization_id}, folders/{folder_id}
            or projects/{project_id}
        notification_categories (MutableSequence[google.cloud.essential_contacts_v1.types.NotificationCategory]):
            The categories of notifications to compute
            contacts for. If ALL is included in this list,
            contacts subscribed to any notification category
            will be returned.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``next_page_token`` in the response indicates that more
            results might be available. If not specified, the default
            page_size is 100.
        page_token (str):
            Optional. If present, retrieves the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of other method parameters should be
            identical to those in the previous call.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notification_categories: MutableSequence[enums.NotificationCategory] = (
        proto.RepeatedField(
            proto.ENUM,
            number=6,
            enum=enums.NotificationCategory,
        )
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ComputeContactsResponse(proto.Message):
    r"""Response message for the ComputeContacts method.

    Attributes:
        contacts (MutableSequence[google.cloud.essential_contacts_v1.types.Contact]):
            All contacts for the resource that are
            subscribed to the specified notification
            categories, including contacts inherited from
            any parent resources.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token`` and the rest of the
            parameters the same as the original request.
    """

    @property
    def raw_page(self):
        return self

    contacts: MutableSequence["Contact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Contact",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SendTestMessageRequest(proto.Message):
    r"""Request message for the SendTestMessage method.

    Attributes:
        contacts (MutableSequence[str]):
            Required. The list of names of the contacts to send a test
            message to. Format:
            organizations/{organization_id}/contacts/{contact_id},
            folders/{folder_id}/contacts/{contact_id} or
            projects/{project_id}/contacts/{contact_id}
        resource (str):
            Required. The name of the resource to send the test message
            for. All contacts must either be set directly on this
            resource or inherited from another resource that is an
            ancestor of this one. Format:
            organizations/{organization_id}, folders/{folder_id} or
            projects/{project_id}
        notification_category (google.cloud.essential_contacts_v1.types.NotificationCategory):
            Required. The notification category to send
            the test message for. All contacts must be
            subscribed to this category.
    """

    contacts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=2,
    )
    notification_category: enums.NotificationCategory = proto.Field(
        proto.ENUM,
        number=3,
        enum=enums.NotificationCategory,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
