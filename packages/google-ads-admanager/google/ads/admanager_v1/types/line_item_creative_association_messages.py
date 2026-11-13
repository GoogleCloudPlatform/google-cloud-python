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

from google.ads.admanager_v1.types import line_item_creative_association_enums, size

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "LineItemCreativeAssociation",
        "LineItemCreativeAssociationStats",
    },
)


class LineItemCreativeAssociation(proto.Message):
    r"""A LineItemCreativeAssociation associates a
    [Creative][google.ads.admanager.v1.Creative] or
    [CreativeSet][google.ads.admanager.v1.CreativeSet] with a
    [LineItem][google.ads.admanager.v1.LineItem] so that the creative
    can be served in ad units targeted by the line item.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``LineItemCreativeAssociation``. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
        line_item (str):
            Required. Immutable. The
            [LineItem][google.ads.admanager.v1.LineItem] to which the
            LineItemCreativeAssociation belongs.

            This field is a member of `oneof`_ ``_line_item``.
        creative (str):
            Optional. Immutable. The
            [Creative][google.ads.admanager.v1.Creative] to which the
            LineItemCreativeAssociation associated. Optional if
            [creativeSet][google.ads.admanager.v1.LineItemCreativeAssociation.creative_set]
            is set.

            This field is a member of `oneof`_ ``_creative``.
        creative_set (str):
            Optional. Immutable. The
            [CreativeSet][google.ads.admanager.v1.CreativeSet] to which
            the LineItemCreativeAssociation associated. Optional if
            [creative][google.ads.admanager.v1.LineItemCreativeAssociation.creative]
            is set.

            This field is a member of `oneof`_ ``_creative_set``.
        status (google.ads.admanager_v1.types.LineItemCreativeAssociationStatusEnum.LineItemCreativeAssociationStatus):
            Output only. The status of the association.

            This field is a member of `oneof`_ ``_status``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Overrides the value set for
            [startTime][google.ads.admanager.v1.LineItem.start_time] of
            the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item].
            This value is only valid for Ad Manager 360 networks. If
            unset, the
            [startTime][google.ads.admanager.v1.LineItem.start_time] of
            the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item]
            will be used.

            This field is a member of `oneof`_ ``_start_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Overrides
            [endTime][google.ads.admanager.v1.LineItem.end_time] of the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item].
            This value is only valid for Ad Manager 360 networks. If
            unset, the
            [endTime][google.ads.admanager.v1.LineItem.end_time] of the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item]
            will be used.

            This field is a member of `oneof`_ ``_end_time``.
        sizes (MutableSequence[google.ads.admanager_v1.types.Size]):
            Optional. Overrides the value set for
            [size][google.ads.admanager.v1.Creative.size] of the
            [creative][google.ads.admanager.v1.LineItemCreativeAssociation.creative],
            which allows the creative to be served to ad units that
            would otherwise not be compatible for its actual size.
        destination_url (str):
            Optional. Overrides the value set for
            [destinationUrl][Creative.destination_url] of the
            [creative][google.ads.admanager.v1.LineItemCreativeAssociation.creative].
            This value is only valid for Ad Manager 360 networks.

            This field is a member of `oneof`_ ``_destination_url``.
        manual_creative_rotation_weight (float):
            Optional. Non-empty default. The weight of the
            [creative][google.ads.admanager.v1.LineItemCreativeAssociation.creative].
            This value is only used if the
            [creativeRotationType][google.ads.admanager.v1.LineItem.creative_rotation_type]
            of the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item]
            is set to
            [WEIGHTED][google.ads.admanager.v1.CreativeRotationTypeEnum.CreativeRotationType.WEIGHTED].
            Defaults to 10.

            This field is a member of `oneof`_ ``_manual_creative_rotation_weight``.
        sequential_creative_rotation_index (int):
            Optional. Non-empty default. The sequential rotation index
            of the Creative. This value is used only if the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item]'s
            [creativeRotationType][google.ads.admanager.v1.LineItem.creative_rotation_type]
            is set to
            [SEQUENTIAL][google.ads.admanager.v1.CreativeRotationTypeEnum.CreativeRotationType.SEQUENTIAL].
            Defaults to 1.

            This field is a member of `oneof`_ ``_sequential_creative_rotation_index``.
        targeting_display_name (str):
            Optional. Specifies creative targeting for this line item
            creative association. It should match the
            [targetingName][CreativePlaceholder.targeting_name]
            specified on the corresponding
            [creativePlaceholder][LineItem.creative_placeholder] on the
            [lineItem][google.ads.admanager.v1.LineItemCreativeAssociation.line_item].
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time this
            association was last modified.

            This field is a member of `oneof`_ ``_update_time``.
        stats (google.ads.admanager_v1.types.LineItemCreativeAssociationStats):
            Output only. Contains trafficking statistics
            for the association.

            This field is a member of `oneof`_ ``_stats``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    line_item: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    creative: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    creative_set: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    status: line_item_creative_association_enums.LineItemCreativeAssociationStatusEnum.LineItemCreativeAssociationStatus = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=line_item_creative_association_enums.LineItemCreativeAssociationStatusEnum.LineItemCreativeAssociationStatus,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    sizes: MutableSequence[size.Size] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=size.Size,
    )
    destination_url: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    manual_creative_rotation_weight: float = proto.Field(
        proto.DOUBLE,
        number=10,
        optional=True,
    )
    sequential_creative_rotation_index: int = proto.Field(
        proto.INT32,
        number=11,
        optional=True,
    )
    targeting_display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    stats: "LineItemCreativeAssociationStats" = proto.Field(
        proto.MESSAGE,
        number=25,
        optional=True,
        message="LineItemCreativeAssociationStats",
    )


class LineItemCreativeAssociationStats(proto.Message):
    r"""Contains statistics such as impressions, clicks delivered, and
    viewable impressions for a
    [LineItemCreativeAssociation][google.ads.admanager.v1.LineItemCreativeAssociation].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        impressions_delivered (int):
            Output only. The number of impressions
            delivered.

            This field is a member of `oneof`_ ``_impressions_delivered``.
        clicks_delivered (int):
            Output only. The number of clicks delivered.

            This field is a member of `oneof`_ ``_clicks_delivered``.
        viewable_impressions_delivered (int):
            Output only. The number of viewable
            impressions delivered.

            This field is a member of `oneof`_ ``_viewable_impressions_delivered``.
        creative_set_stats (MutableMapping[int, google.ads.admanager_v1.types.LineItemCreativeAssociationStats.CreativeStats]):
            Output only. Creative set stats.
    """

    class CreativeStats(proto.Message):
        r"""Contains statistics such as impressions, clicks delivered, and
        viewable impressions for creatives belonging to a
        [CreativeSet][google.ads.admanager.v1.CreativeSet].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            impressions_delivered (int):
                Output only. The number of impressions
                delivered.

                This field is a member of `oneof`_ ``_impressions_delivered``.
            clicks_delivered (int):
                Output only. The number of clicks delivered.

                This field is a member of `oneof`_ ``_clicks_delivered``.
            viewable_impressions_delivered (int):
                Output only. The number of video completions
                delivered.

                This field is a member of `oneof`_ ``_viewable_impressions_delivered``.
        """

        impressions_delivered: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        clicks_delivered: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        viewable_impressions_delivered: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )

    impressions_delivered: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    clicks_delivered: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    viewable_impressions_delivered: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    creative_set_stats: MutableMapping[int, CreativeStats] = proto.MapField(
        proto.INT64,
        proto.MESSAGE,
        number=4,
        message=CreativeStats,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
