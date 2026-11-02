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

from google.ads.admanager_v1.types import user_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetUserRequest",
        "ListUsersRequest",
        "ListUsersResponse",
        "CreateUserRequest",
        "BatchCreateUsersRequest",
        "BatchCreateUsersResponse",
        "UpdateUserRequest",
        "BatchUpdateUsersRequest",
        "BatchUpdateUsersResponse",
        "BatchActivateUsersRequest",
        "BatchActivateUsersResponse",
        "BatchDeactivateUsersRequest",
        "BatchDeactivateUsersResponse",
    },
)


class GetUserRequest(proto.Message):
    r"""Request object for GetUser method.

    Attributes:
        name (str):
            Required. The resource name of the User. Format:
            ``networks/{network_code}/users/{user_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUsersRequest(proto.Message):
    r"""Request object for ListUsers method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Users.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of Users to
            return. The service may return fewer than this
            value. If unspecified, at most 50 users will be
            returned. The maximum value is 1000; values
            greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListUsers`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListUsers`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``active``
            - ``displayName``
            - ``email``
            - ``externalId``
            - ``name``
            - ``role``
            - ``serviceAccount``
            - ``userId``
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


class ListUsersResponse(proto.Message):
    r"""Response object for ListUsersRequest containing matching User
    resources.

    Attributes:
        users (MutableSequence[google.ads.admanager_v1.types.User]):
            The User from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of Users. If a filter was included in the
            request, this reflects the total number after the filtering
            is applied.

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

    users: MutableSequence[user_messages.User] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=user_messages.User,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateUserRequest(proto.Message):
    r"""Request object for ``CreateUser`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``User`` will be
            created. Format: ``networks/{network_code}``
        user (google.ads.admanager_v1.types.User):
            Required. The ``User`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user: user_messages.User = proto.Field(
        proto.MESSAGE,
        number=2,
        message=user_messages.User,
    )


class BatchCreateUsersRequest(proto.Message):
    r"""Request object for ``BatchCreateUsers`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Users`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateUserRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateUserRequest]):
            Required. The ``User`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateUserRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateUserRequest",
    )


class BatchCreateUsersResponse(proto.Message):
    r"""Response object for ``BatchCreateUsers`` method.

    Attributes:
        users (MutableSequence[google.ads.admanager_v1.types.User]):
            The ``User`` objects created.
    """

    users: MutableSequence[user_messages.User] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=user_messages.User,
    )


class UpdateUserRequest(proto.Message):
    r"""Request object for ``UpdateUser`` method.

    Attributes:
        user (google.ads.admanager_v1.types.User):
            Required. The ``User`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    user: user_messages.User = proto.Field(
        proto.MESSAGE,
        number=1,
        message=user_messages.User,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateUsersRequest(proto.Message):
    r"""Request object for ``BatchUpdateUsers`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Users`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateUserRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateUserRequest]):
            Required. The ``User`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateUserRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateUserRequest",
    )


class BatchUpdateUsersResponse(proto.Message):
    r"""Response object for ``BatchUpdateUsers`` method.

    Attributes:
        users (MutableSequence[google.ads.admanager_v1.types.User]):
            The ``User`` objects updated.
    """

    users: MutableSequence[user_messages.User] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=user_messages.User,
    )


class BatchActivateUsersRequest(proto.Message):
    r"""Request message for ``BatchActivateUsers`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``User`` objects to
            activate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateUsersResponse(proto.Message):
    r"""Response object for ``BatchActivateUsers`` method."""


class BatchDeactivateUsersRequest(proto.Message):
    r"""Request message for ``BatchDeactivateUsers`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``User`` objects to
            deactivate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateUsersResponse(proto.Message):
    r"""Response object for ``BatchDeactivateUsers`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
