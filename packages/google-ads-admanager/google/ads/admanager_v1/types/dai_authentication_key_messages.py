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

from google.ads.admanager_v1.types import dai_authentication_key_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "DaiAuthenticationKey",
    },
)


class DaiAuthenticationKey(proto.Message):
    r"""A DaiAuthenticationKey is used to authenticate stream
    requests to the IMA SDK API.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``DaiAuthenticationKey``. Format:
            ``networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}``
        key (str):
            Output only. The value of the secure key.

            This field is a member of `oneof`_ ``_key``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time this
            DaiAuthenticationKey was created.
        status (google.ads.admanager_v1.types.DaiAuthenticationKeyStatusEnum.DaiAuthenticationKeyStatus):
            Output only. The status of this DaiAuthenticationKey.

            DAI authentication keys are created in the
            [``ACTIVE``][google.ads.admanager.v1.DaiAuthenticationKeyStatusEnum.DaiAuthenticationKeyStatus.ACTIVE]
            state.

            Only active keys will be accepted by the IMA SDK API as
            valid.

            This field is a member of `oneof`_ ``_status``.
        display_name (str):
            Required. The name for this
            DaiAuthenticationKey.

            This field is a member of `oneof`_ ``_display_name``.
        key_type (google.ads.admanager_v1.types.DaiAuthenticationKeyTypeEnum.DaiAuthenticationKeyType):
            Optional. The type of this key, which
            determines how it should be used on stream
            create requests.

            This field is a member of `oneof`_ ``_key_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    status: dai_authentication_key_enums.DaiAuthenticationKeyStatusEnum.DaiAuthenticationKeyStatus = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=dai_authentication_key_enums.DaiAuthenticationKeyStatusEnum.DaiAuthenticationKeyStatus,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    key_type: dai_authentication_key_enums.DaiAuthenticationKeyTypeEnum.DaiAuthenticationKeyType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=dai_authentication_key_enums.DaiAuthenticationKeyTypeEnum.DaiAuthenticationKeyType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
