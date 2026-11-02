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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.spanner_v1.types import type as gs_type

__protobuf__ = proto.module(
    package="google.spanner.v1",
    manifest={
        "Range",
        "Tablet",
        "Group",
        "KeyRecipe",
        "RecipeList",
        "CacheUpdate",
        "RoutingHint",
    },
)


class Range(proto.Message):
    r"""A ``Range`` represents a range of keys in a database. The keys
    themselves are encoded in "sortable string format", also known as
    ssformat. Consult Spanner's open source client libraries for details
    on the encoding.

    Each range represents a contiguous range of rows, possibly from
    multiple tables/indexes. Each range is associated with a single
    paxos group (known as a "group" throughout this API), a split (which
    names the exact range within the group), and a generation that can
    be used to determine whether a given ``Range`` represents a newer or
    older location for the key range.

    Attributes:
        start_key (bytes):
            The start key of the range, inclusive.
            Encoded in "sortable string format" (ssformat).
        limit_key (bytes):
            The limit key of the range, exclusive.
            Encoded in "sortable string format" (ssformat).
        group_uid (int):
            The UID of the paxos group where this range is stored. UIDs
            are unique within the database. References
            ``Group.group_uid``.
        split_id (int):
            A group can store multiple ranges of keys. Each key range is
            named by an ID (the split ID). Within a group, split IDs are
            unique. The ``split_id`` names the exact split in
            ``group_uid`` where this range is stored.
        generation (bytes):
            ``generation`` indicates the freshness of the range
            information contained in this proto. Generations can be
            compared lexicographically; if generation A is greater than
            generation B, then the ``Range`` corresponding to A is newer
            than the ``Range`` corresponding to B, and should be used
            preferentially.
    """

    start_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    limit_key: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    group_uid: int = proto.Field(
        proto.UINT64,
        number=3,
    )
    split_id: int = proto.Field(
        proto.UINT64,
        number=4,
    )
    generation: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class Tablet(proto.Message):
    r"""A ``Tablet`` represents a single replica of a ``Group``. A tablet is
    served by a single server at a time, and can move between servers
    due to server death or simply load balancing.

    Attributes:
        tablet_uid (int):
            The UID of the tablet, unique within the database. Matches
            the ``tablet_uids`` and ``leader_tablet_uid`` fields in
            ``Group``.
        server_address (str):
            The address of the server that is serving
            this tablet -- either an IP address or DNS
            hostname and a port number.
        location (str):
            Where this tablet is located. This is the
            name of a Google Cloud region, such as
            "us-central1".
        role (google.cloud.spanner_v1.types.Tablet.Role):
            The role of the tablet.
        incarnation (bytes):
            ``incarnation`` indicates the freshness of the tablet
            information contained in this proto. Incarnations can be
            compared lexicographically; if incarnation A is greater than
            incarnation B, then the ``Tablet`` corresponding to A is
            newer than the ``Tablet`` corresponding to B, and should be
            used preferentially.
        distance (int):
            Distances help the client pick the closest tablet out of the
            list of tablets for a given request. Tablets with lower
            distances should generally be preferred. Tablets with the
            same distance are approximately equally close; the client
            can choose arbitrarily.

            Distances do not correspond precisely to expected latency,
            geographical distance, or anything else. Distances should be
            compared only between tablets of the same group; they are
            not meaningful between different groups.

            A value of zero indicates that the tablet may be in the same
            zone as the client, and have minimum network latency. A
            value less than or equal to five indicates that the tablet
            is thought to be in the same region as the client, and may
            have a few milliseconds of network latency. Values greater
            than five are most likely in a different region, with
            non-trivial network latency.

            Clients should use the following algorithm:

            - If the request is using a directed read, eliminate any
              tablets that do not match the directed read's target zone
              and/or replica type.
            - (Read-write transactions only) Choose leader tablet if it
              has an distance <=5.
            - Group and sort tablets by distance. Choose a random tablet
              with the lowest distance. If the request is not a directed
              read, only consider replicas with distances <=5.
            - Send the request to the fallback endpoint.

            The tablet picked by this algorithm may be skipped, either
            because it is marked as ``skip`` by the server or because
            the corresponding server is unreachable, flow controlled,
            etc. Skipped tablets should be added to the
            ``skipped_tablet_uid`` field in ``RoutingHint``; the
            algorithm above should then be re-run without including the
            skipped tablet(s) to pick the next best tablet.
        skip (bool):
            If true, the tablet should not be chosen by the client.
            Typically, this signals that the tablet is unhealthy in some
            way. Tablets with ``skip`` set to true should be reported
            back to the server in ``RoutingHint.skipped_tablet_uid``;
            this cues the server to send updated information for this
            tablet should it become usable again.
    """

    class Role(proto.Enum):
        r"""Indicates the role of the tablet.

        Values:
            ROLE_UNSPECIFIED (0):
                Not specified.
            READ_WRITE (1):
                The tablet can perform reads and (if elected
                leader) writes.
            READ_ONLY (2):
                The tablet can only perform reads.
        """

        ROLE_UNSPECIFIED = 0
        READ_WRITE = 1
        READ_ONLY = 2

    tablet_uid: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    server_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    role: Role = proto.Field(
        proto.ENUM,
        number=4,
        enum=Role,
    )
    incarnation: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )
    distance: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    skip: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class Group(proto.Message):
    r"""A ``Group`` represents a paxos group in a database. A group is a set
    of tablets that are replicated across multiple servers. Groups may
    have a leader tablet. Groups store one (or sometimes more) ranges of
    keys.

    Attributes:
        group_uid (int):
            The UID of the paxos group, unique within the database.
            Matches the ``group_uid`` field in ``Range``.
        tablets (MutableSequence[google.cloud.spanner_v1.types.Tablet]):
            A list of tablets that are part of the group. Note that this
            list may not be exhaustive; it will only include tablets the
            server considers useful to the client. The returned list is
            ordered ascending by distance.

            Tablet UIDs reference ``Tablet.tablet_uid``.
        leader_index (int):
            The last known leader tablet of the group as an index into
            ``tablets``. May be negative if the group has no known
            leader.
        generation (bytes):
            ``generation`` indicates the freshness of the group
            information (including leader information) contained in this
            proto. Generations can be compared lexicographically; if
            generation A is greater than generation B, then the
            ``Group`` corresponding to A is newer than the ``Group``
            corresponding to B, and should be used preferentially.
    """

    group_uid: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    tablets: MutableSequence["Tablet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Tablet",
    )
    leader_index: int = proto.Field(
        proto.INT32,
        number=3,
    )
    generation: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )


class KeyRecipe(proto.Message):
    r"""A ``KeyRecipe`` provides the metadata required to translate reads,
    mutations, and queries into a byte array in "sortable string format"
    (ssformat)that can be used with ``Range``\ s to route requests. Note
    that the client *must* tolerate ``KeyRecipe``\ s that appear to be
    invalid, since the ``KeyRecipe`` format may change over time.
    Requests with invalid ``KeyRecipe``\ s should be routed to a default
    server.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table_name (str):
            A table name, matching the name from the
            database schema.

            This field is a member of `oneof`_ ``target``.
        index_name (str):
            An index name, matching the name from the
            database schema.

            This field is a member of `oneof`_ ``target``.
        operation_uid (int):
            The UID of a query, matching the UID from ``RoutingHint``.

            This field is a member of `oneof`_ ``target``.
        part (MutableSequence[google.cloud.spanner_v1.types.KeyRecipe.Part]):
            Parts are in the order they should appear in
            the encoded key.
    """

    class Part(proto.Message):
        r"""An ssformat key is composed of a sequence of tag numbers and key
        column values. ``Part`` represents a single tag or key column value.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tag (int):
                If non-zero, ``tag`` is the only field present in this
                ``Part``. The part is encoded by appending ``tag`` to the
                ssformat key.
            order (google.cloud.spanner_v1.types.KeyRecipe.Part.Order):
                Whether the key column is sorted ascending or descending.
                Only present if ``tag`` is zero.
            null_order (google.cloud.spanner_v1.types.KeyRecipe.Part.NullOrder):
                How NULLs are represented in the encoded key part. Only
                present if ``tag`` is zero.
            type_ (google.cloud.spanner_v1.types.Type):
                The type of the key part. Only present if ``tag`` is zero.
            identifier (str):
                ``identifier`` is the name of the column or query parameter.

                This field is a member of `oneof`_ ``value_type``.
            value (google.protobuf.struct_pb2.Value):
                The constant value of the key part.
                It is present when query uses a constant as a
                part of the key.

                This field is a member of `oneof`_ ``value_type``.
            random (bool):
                If true, the client is responsible to fill in
                the value randomly. It's relevant only for the
                INT64 type.

                This field is a member of `oneof`_ ``value_type``.
            struct_identifiers (MutableSequence[int]):
                It is a repeated field to support fetching key columns from
                nested structs, such as ``STRUCT`` query parameters.
        """

        class Order(proto.Enum):
            r"""The remaining fields encode column values.

            Values:
                ORDER_UNSPECIFIED (0):
                    Default value, equivalent to ``ASCENDING``.
                ASCENDING (1):
                    The key is ascending - corresponds to ``ASC`` in the schema
                    definition.
                DESCENDING (2):
                    The key is descending - corresponds to ``DESC`` in the
                    schema definition.
            """

            ORDER_UNSPECIFIED = 0
            ASCENDING = 1
            DESCENDING = 2

        class NullOrder(proto.Enum):
            r"""The null order of the key column. This dictates where NULL values
            sort in the sorted order. Note that columns which are ``NOT NULL``
            can have a special encoding.

            Values:
                NULL_ORDER_UNSPECIFIED (0):
                    Default value. This value is unused.
                NULLS_FIRST (1):
                    NULL values sort before any non-NULL values.
                NULLS_LAST (2):
                    NULL values sort after any non-NULL values.
                NOT_NULL (3):
                    The column does not support NULL values.
            """

            NULL_ORDER_UNSPECIFIED = 0
            NULLS_FIRST = 1
            NULLS_LAST = 2
            NOT_NULL = 3

        tag: int = proto.Field(
            proto.UINT32,
            number=1,
        )
        order: "KeyRecipe.Part.Order" = proto.Field(
            proto.ENUM,
            number=2,
            enum="KeyRecipe.Part.Order",
        )
        null_order: "KeyRecipe.Part.NullOrder" = proto.Field(
            proto.ENUM,
            number=3,
            enum="KeyRecipe.Part.NullOrder",
        )
        type_: gs_type.Type = proto.Field(
            proto.MESSAGE,
            number=4,
            message=gs_type.Type,
        )
        identifier: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="value_type",
        )
        value: struct_pb2.Value = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="value_type",
            message=struct_pb2.Value,
        )
        random: bool = proto.Field(
            proto.BOOL,
            number=8,
            oneof="value_type",
        )
        struct_identifiers: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=7,
        )

    table_name: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="target",
    )
    index_name: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="target",
    )
    operation_uid: int = proto.Field(
        proto.UINT64,
        number=3,
        oneof="target",
    )
    part: MutableSequence[Part] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Part,
    )


class RecipeList(proto.Message):
    r"""A ``RecipeList`` contains a list of ``KeyRecipe``\ s, which share
    the same schema generation.

    Attributes:
        schema_generation (bytes):
            The schema generation of the recipes. To be sent to the
            server in ``RoutingHint.schema_generation`` whenever one of
            the recipes is used. ``schema_generation`` values are
            comparable with each other; if generation A compares greater
            than generation B, then A is a more recent schema than B.
            Clients should in general aim to cache only the latest
            schema generation, and discard more stale recipes.
        recipe (MutableSequence[google.cloud.spanner_v1.types.KeyRecipe]):
            A list of recipes to be cached.
    """

    schema_generation: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    recipe: MutableSequence["KeyRecipe"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="KeyRecipe",
    )


class CacheUpdate(proto.Message):
    r"""A ``CacheUpdate`` expresses a set of changes the client should
    incorporate into its location cache. These changes may or may not be
    newer than what the client has in its cache, and should be discarded
    if necessary. ``CacheUpdate``\ s can be obtained in response to
    requests that included a ``RoutingHint`` field, but may also be
    obtained by explicit location-fetching RPCs which may be added in
    the future.

    Attributes:
        database_id (int):
            An internal ID for the database. Database
            names can be reused if a database is deleted and
            re-created. Each time the database is
            re-created, it will get a new database ID, which
            will never be re-used for any other database.
        range_ (MutableSequence[google.cloud.spanner_v1.types.Range]):
            A list of ranges to be cached.
        group (MutableSequence[google.cloud.spanner_v1.types.Group]):
            A list of groups to be cached.
        key_recipes (google.cloud.spanner_v1.types.RecipeList):
            A list of recipes to be cached.
    """

    database_id: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    range_: MutableSequence["Range"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Range",
    )
    group: MutableSequence["Group"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Group",
    )
    key_recipes: "RecipeList" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RecipeList",
    )


class RoutingHint(proto.Message):
    r"""``RoutingHint`` can be optionally added to location-aware Spanner
    requests. It gives the server hints that can be used to route the
    request to an appropriate server, potentially significantly
    decreasing latency and improving throughput. To achieve improved
    performance, most fields must be filled in with accurate values.

    The presence of a valid ``RoutingHint`` tells the server that the
    client is location-aware.

    ``RoutingHint`` does not change the semantics of the request; it is
    purely a performance hint; the request will perform the same actions
    on the database's data as if ``RoutingHint`` were not present.
    However, if the ``RoutingHint`` is incomplete or incorrect, the
    response may include a ``CacheUpdate`` the client can use to correct
    its location cache.

    Attributes:
        operation_uid (int):
            A session-scoped unique ID for the operation, computed
            client-side. Requests with the same ``operation_uid`` should
            have a shared 'shape', meaning that some fields are expected
            to be the same, such as the SQL query, the target
            table/columns (for reads) etc. Requests with the same
            ``operation_uid`` are meant to differ only in fields like
            keys/key ranges/query parameters, transaction IDs, etc.

            ``operation_uid`` must be non-zero for ``RoutingHint`` to be
            valid.
        database_id (int):
            The database ID of the database being accessed, see
            ``CacheUpdate.database_id``. Should match the cache entries
            that were used to generate the rest of the fields in this
            ``RoutingHint``.
        schema_generation (bytes):
            The schema generation of the recipe that was used to
            generate ``key`` and ``limit_key``. See also
            ``RecipeList.schema_generation``.
        key (bytes):
            The key / key range that this request accesses. For
            operations that access a single key, ``key`` should be set
            and ``limit_key`` should be empty. For operations that
            access a key range, ``key`` and ``limit_key`` should both be
            set, to the inclusive start and exclusive end of the range
            respectively.

            The keys are encoded in "sortable string format" (ssformat),
            using a ``KeyRecipe`` that is appropriate for the request.
            See ``KeyRecipe`` for more details.
        limit_key (bytes):
            If this request targets a key range, this is the exclusive
            end of the range. See ``key`` for more details.
        group_uid (int):
            The group UID of the group that the client believes serves
            the range defined by ``key`` and ``limit_key``. See
            ``Range.group_uid`` for more details.
        split_id (int):
            The split ID of the split that the client believes contains
            the range defined by ``key`` and ``limit_key``. See
            ``Range.split_id`` for more details.
        tablet_uid (int):
            The tablet UID of the tablet from group ``group_uid`` that
            the client believes is best to serve this request. See
            ``Group.local_tablet_uids`` and ``Group.leader_tablet_uid``.
        skipped_tablet_uid (MutableSequence[google.cloud.spanner_v1.types.RoutingHint.SkippedTablet]):
            If the client had multiple options for tablet selection, and
            some of its first choices were unhealthy (e.g., the server
            is unreachable, or ``Tablet.skip`` is true), this field will
            contain the tablet UIDs of those tablets, with their
            incarnations. The server may include a ``CacheUpdate`` with
            new locations for those tablets.
        client_location (str):
            If present, the client's current location.
            This should be the name of a Google Cloud zone
            or region, such as "us-central1".

            If absent, the client's location will be assumed
            to be the same as the location of the server the
            client ends up connected to.

            Locations are primarily valuable for clients
            that connect from regions other than the ones
            that contain the Spanner database.
    """

    class SkippedTablet(proto.Message):
        r"""A tablet that was skipped by the client. See ``Tablet.tablet_uid``
        and ``Tablet.incarnation``.

        Attributes:
            tablet_uid (int):
                The tablet UID of the tablet that was skipped. See
                ``Tablet.tablet_uid``.
            incarnation (bytes):
                The incarnation of the tablet that was skipped. See
                ``Tablet.incarnation``.
        """

        tablet_uid: int = proto.Field(
            proto.UINT64,
            number=1,
        )
        incarnation: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )

    operation_uid: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    database_id: int = proto.Field(
        proto.UINT64,
        number=2,
    )
    schema_generation: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    key: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    limit_key: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )
    group_uid: int = proto.Field(
        proto.UINT64,
        number=6,
    )
    split_id: int = proto.Field(
        proto.UINT64,
        number=7,
    )
    tablet_uid: int = proto.Field(
        proto.UINT64,
        number=8,
    )
    skipped_tablet_uid: MutableSequence[SkippedTablet] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=SkippedTablet,
    )
    client_location: str = proto.Field(
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
