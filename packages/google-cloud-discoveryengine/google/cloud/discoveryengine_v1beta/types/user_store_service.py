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

from google.cloud.discoveryengine_v1beta.types import user_store as gcd_user_store

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "GetUserStoreRequest",
        "UpdateUserStoreRequest",
    },
)


class GetUserStoreRequest(proto.Message):
    r"""Request message for
    [UserStoreService.GetUserStore][google.cloud.discoveryengine.v1beta.UserStoreService.GetUserStore]

    Attributes:
        name (str):
            Required. The name of the User Store to get. Format:
            ``projects/{project}/locations/{location}/userStores/{user_store_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateUserStoreRequest(proto.Message):
    r"""Request message for
    [UserStoreService.UpdateUserStore][google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore]
    method.

    Attributes:
        user_store (google.cloud.discoveryengine_v1beta.types.UserStore):
            Required. The User Store to update. Format:
            ``projects/{project}/locations/{location}/userStores/{user_store_id}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    user_store: gcd_user_store.UserStore = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_user_store.UserStore,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
