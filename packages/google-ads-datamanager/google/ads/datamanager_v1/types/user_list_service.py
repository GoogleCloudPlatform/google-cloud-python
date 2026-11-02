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

from google.ads.datamanager_v1.types import user_list as gad_user_list

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "GetUserListRequest",
        "ListUserListsRequest",
        "ListUserListsResponse",
        "CreateUserListRequest",
        "UpdateUserListRequest",
        "DeleteUserListRequest",
    },
)


class GetUserListRequest(proto.Message):
    r"""Request message for GetUserList.

    Attributes:
        name (str):
            Required. The resource name of the UserList to retrieve.
            Format:
            accountTypes/{account_type}/accounts/{account}/userLists/{user_list}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserListsRequest(proto.Message):
    r"""Request message for ListUserLists.

    Attributes:
        parent (str):
            Required. The parent account which owns this collection of
            user lists. Format:
            accountTypes/{account_type}/accounts/{account}
        page_size (int):
            Optional. The maximum number of user lists to
            return. The service may return fewer than this
            value. If unspecified, at most 50 user lists
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListUserLists`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListUserLists`` must match the call that provided the page
            token.
        filter (str):
            Optional. A `filter string <https://google.aip.dev/160>`__.
            All fields need to be on the left hand side of each
            condition (for example: ``display_name = "list 1"``). Fields
            must be specified using either all `camel
            case <https://en.wikipedia.org/wiki/Camel_case>`__ or all
            `snake case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Don't use a combination of camel case and snake case.

            Supported operations:

            - ``AND``
            - ``=``
            - ``!=``
            - ``>``
            - ``>=``
            - ``<``
            - ``<=``
            - ``:`` (has)

            **Supported Functions:**

            - ``IN(field, value1, value2, ...)``: returns true if the
              field matches any of the values. Example:
              ``IN(display_name, "name1", "name2")``

            Supported fields:

            - ``id``
            - ``display_name``
            - ``description``
            - ``membership_status``
            - ``integration_code``
            - ``access_reason``
            - ``ingested_user_list_info.upload_key_types``
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


class ListUserListsResponse(proto.Message):
    r"""Response message for ListUserLists.

    Attributes:
        user_lists (MutableSequence[google.ads.datamanager_v1.types.UserList]):
            The user lists from the specified account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    user_lists: MutableSequence[gad_user_list.UserList] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gad_user_list.UserList,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateUserListRequest(proto.Message):
    r"""Request message for CreateUserList.

    Attributes:
        parent (str):
            Required. The parent account where this user list will be
            created. Format:
            accountTypes/{account_type}/accounts/{account}
        user_list (google.ads.datamanager_v1.types.UserList):
            Required. The user list to create.
        validate_only (bool):
            Optional. If true, the request is validated
            but not executed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_list: gad_user_list.UserList = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gad_user_list.UserList,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateUserListRequest(proto.Message):
    r"""Request message for UpdateUserList.

    Attributes:
        user_list (google.ads.datamanager_v1.types.UserList):
            Required. The user list to update.

            The user list's ``name`` field is used to identify the user
            list to update. Format:
            accountTypes/{account_type}/accounts/{account}/userLists/{user_list}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
        validate_only (bool):
            Optional. If true, the request is validated
            but not executed.
    """

    user_list: gad_user_list.UserList = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gad_user_list.UserList,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteUserListRequest(proto.Message):
    r"""Request message for DeleteUserList.

    Attributes:
        name (str):
            Required. The name of the user list to delete. Format:
            accountTypes/{account_type}/accounts/{account}/userLists/{user_list}
        validate_only (bool):
            Optional. If true, the request is validated
            but not executed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
