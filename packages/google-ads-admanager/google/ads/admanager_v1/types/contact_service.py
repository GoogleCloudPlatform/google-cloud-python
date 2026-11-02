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
import proto  # type: ignore

from google.ads.admanager_v1.types import contact_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetContactRequest",
        "ListContactsRequest",
        "ListContactsResponse",
        "CreateContactRequest",
        "BatchCreateContactsRequest",
        "BatchCreateContactsResponse",
        "UpdateContactRequest",
        "BatchUpdateContactsRequest",
        "BatchUpdateContactsResponse",
    },
)


class GetContactRequest(proto.Message):
    r"""Request object for ``GetContact`` method.

    Attributes:
        name (str):
            Required. The resource name of the Contact. Format:
            ``networks/{network_code}/contacts/{contact_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListContactsRequest(proto.Message):
    r"""Request object for ``ListContacts`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Contacts. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Contacts`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Contacts`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListContacts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListContacts`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``address``
            - ``cellPhone``
            - ``comment``
            - ``company``
            - ``displayName``
            - ``email``
            - ``fax``
            - ``name``
            - ``status``
            - ``title``
            - ``workPhone``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListContactsResponse(proto.Message):
    r"""Response object for ``ListContactsRequest`` containing matching
    ``Contact`` objects.

    Attributes:
        contacts (MutableSequence[google.ads.admanager_v1.types.Contact]):
            The ``Contact`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Contact`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    contacts: MutableSequence[contact_messages.Contact] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=contact_messages.Contact,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateContactRequest(proto.Message):
    r"""Request object for ``CreateContact`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Contact`` will be
            created. Format: ``networks/{network_code}``
        contact (google.ads.admanager_v1.types.Contact):
            Required. The ``Contact`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    contact: contact_messages.Contact = proto.Field(
        proto.MESSAGE,
        number=2,
        message=contact_messages.Contact,
    )


class BatchCreateContactsRequest(proto.Message):
    r"""Request object for ``BatchCreateContacts`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Contacts`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateContactRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateContactRequest]):
            Required. The ``Contact`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateContactRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateContactRequest",
    )


class BatchCreateContactsResponse(proto.Message):
    r"""Response object for ``BatchCreateContacts`` method.

    Attributes:
        contacts (MutableSequence[google.ads.admanager_v1.types.Contact]):
            The ``Contact`` objects created.
    """

    contacts: MutableSequence[contact_messages.Contact] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=contact_messages.Contact,
    )


class UpdateContactRequest(proto.Message):
    r"""Request object for ``UpdateContact`` method.

    Attributes:
        contact (google.ads.admanager_v1.types.Contact):
            Required. The ``Contact`` to update.

            The ``Contact``'s ``name`` is used to identify the
            ``Contact`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    contact: contact_messages.Contact = proto.Field(
        proto.MESSAGE,
        number=1,
        message=contact_messages.Contact,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateContactsRequest(proto.Message):
    r"""Request object for ``BatchUpdateContacts`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Contacts`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateContactRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateContactRequest]):
            Required. The ``Contact`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateContactRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateContactRequest",
    )


class BatchUpdateContactsResponse(proto.Message):
    r"""Response object for ``BatchUpdateContacts`` method.

    Attributes:
        contacts (MutableSequence[google.ads.admanager_v1.types.Contact]):
            The ``Contact`` objects updated.
    """

    contacts: MutableSequence[contact_messages.Contact] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=contact_messages.Contact,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
