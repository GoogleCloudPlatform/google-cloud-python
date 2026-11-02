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

from google.ads.admanager_v1.types import placement_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Placement",
    },
)


class Placement(proto.Message):
    r"""The ``Placement`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Placement``. Format:
            ``networks/{network_code}/placements/{placement_id}``
        placement_id (int):
            Output only. Deprecated: ``Placement`` ID.
        display_name (str):
            Required. The display name of the placement.
            This attribute has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. A description of the Placement.
            This attribute has a maximum length of 65,535
            characters.

            This field is a member of `oneof`_ ``_description``.
        placement_code (str):
            Output only. A string used to uniquely
            identify the Placement for purposes of serving
            the ad. This attribute is assigned by Google.

            This field is a member of `oneof`_ ``_placement_code``.
        status (google.ads.admanager_v1.types.PlacementStatusEnum.PlacementStatus):
            Output only. The status of the Placement.

            This field is a member of `oneof`_ ``_status``.
        targeted_ad_units (MutableSequence[str]):
            Optional. The resource names of AdUnits that constitute the
            Placement. Format:
            "networks/{network_code}/adUnits/{ad_unit}".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant this Placement was
            last modified.

            This field is a member of `oneof`_ ``_update_time``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    placement_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    placement_code: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    status: placement_enums.PlacementStatusEnum.PlacementStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=placement_enums.PlacementStatusEnum.PlacementStatus,
    )
    targeted_ad_units: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
