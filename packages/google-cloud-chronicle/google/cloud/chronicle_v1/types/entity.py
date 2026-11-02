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

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "Watchlist",
        "WatchlistUserPreferences",
        "GetWatchlistRequest",
        "ListWatchlistsRequest",
        "ListWatchlistsResponse",
        "CreateWatchlistRequest",
        "UpdateWatchlistRequest",
        "DeleteWatchlistRequest",
    },
)


class Watchlist(proto.Message):
    r"""A watchlist is a list of entities that allows for bulk
    operations over the included entities.

    Attributes:
        name (str):
            Identifier. Resource name of the watchlist. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}``
        display_name (str):
            Required. Display name of the watchlist.
            Note that it must be at least one character and
            less than 63 characters
            (https://google.aip.dev/148).
        description (str):
            Optional. Description of the watchlist.
        multiplying_factor (float):
            Optional. Weight applied to the risk score
            for entities in this watchlist.
            The default is 1.0 if it is not specified.
        entity_population_mechanism (google.cloud.chronicle_v1.types.Watchlist.EntityPopulationMechanism):
            Required. Mechanism to populate entities in
            the watchlist.
        entity_count (google.cloud.chronicle_v1.types.Watchlist.EntityCount):
            Output only. Entity count in the watchlist.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the watchlist was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the watchlist was last
            updated.
        watchlist_user_preferences (google.cloud.chronicle_v1.types.WatchlistUserPreferences):
            Optional. User preferences for watchlist
            configuration.
    """

    class EntityPopulationMechanism(proto.Message):
        r"""Mechanism to populate entities in the watchlist.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            manual (google.cloud.chronicle_v1.types.Watchlist.EntityPopulationMechanism.Manual):
                Optional. Entities are added manually.

                This field is a member of `oneof`_ ``mechanism``.
        """

        class Manual(proto.Message):
            r"""Entities are added manually."""

        manual: "Watchlist.EntityPopulationMechanism.Manual" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="mechanism",
            message="Watchlist.EntityPopulationMechanism.Manual",
        )

    class EntityCount(proto.Message):
        r"""Count of different types of entities in the watchlist.

        Attributes:
            user (int):
                Output only. Count of user type entities in
                the watchlist.
            asset (int):
                Output only. Count of asset type entities in
                the watchlist.
        """

        user: int = proto.Field(
            proto.INT32,
            number=1,
        )
        asset: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    multiplying_factor: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    entity_population_mechanism: EntityPopulationMechanism = proto.Field(
        proto.MESSAGE,
        number=6,
        message=EntityPopulationMechanism,
    )
    entity_count: EntityCount = proto.Field(
        proto.MESSAGE,
        number=7,
        message=EntityCount,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    watchlist_user_preferences: "WatchlistUserPreferences" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="WatchlistUserPreferences",
    )


class WatchlistUserPreferences(proto.Message):
    r"""A collection of user preferences for watchlist UI
    configuration.

    Attributes:
        pinned (bool):
            Optional. Whether the watchlist is pinned on
            the dashboard.
    """

    pinned: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GetWatchlistRequest(proto.Message):
    r"""Request message for getting a watchlist.

    Attributes:
        name (str):
            Required. The parent, which owns this collection of
            watchlists. The name of the watchlist to retrieve. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListWatchlistsRequest(proto.Message):
    r"""Request message for listing watchlists.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            watchlists. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            Optional. The maximum number of watchlists to
            return. The service may return fewer than this
            value. If unspecified, at most 200 watchlists
            will be returned. The maximum value is 200;
            values above 200 will be coerced to 200.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListWatchlists`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListWatchlists`` must match the call that provided the
            page token.
        filter (str):
            Optional. Which watchlist to return in aip.dev/160 form.
            Currently, only the following filters are supported:

            - ``watchlist_user_preferences.pinned=true``
            - ``has_entity([ENTITY_INDICATOR],[ENTITY_TYPE])``
            - ``has_entity([ENTITY_INDICATOR],[ENTITY_TYPE],[NAMESPACE])``
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


class ListWatchlistsResponse(proto.Message):
    r"""Response message for listing watchlists.

    Attributes:
        watchlists (MutableSequence[google.cloud.chronicle_v1.types.Watchlist]):
            Optional. The watchlists from the specified
            instance.
        next_page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    watchlists: MutableSequence["Watchlist"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Watchlist",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateWatchlistRequest(proto.Message):
    r"""Request message for creating watchlist.

    Attributes:
        parent (str):
            Required. The parent resource where this watchlist will be
            created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        watchlist_id (str):
            Optional. The ID to use for the watchlist, which will become
            the final component of the watchlist's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
        watchlist (google.cloud.chronicle_v1.types.Watchlist):
            Required. The watchlist to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    watchlist_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    watchlist: "Watchlist" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Watchlist",
    )


class UpdateWatchlistRequest(proto.Message):
    r"""Request message for updating watchlist.

    Attributes:
        watchlist (google.cloud.chronicle_v1.types.Watchlist):
            Required. The watchlist to update.

            The watchlist's ``name`` field is used to identify the
            watchlist to update. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    watchlist: "Watchlist" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Watchlist",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteWatchlistRequest(proto.Message):
    r"""Request message for deleting watchlist.

    Attributes:
        name (str):
            Required. The name of the watchlist to delete. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}``
        force (bool):
            Optional. If set to true, any entities under
            this watchlist will also be deleted. (Otherwise,
            the request will only work if the watchlist has
            no entities.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
