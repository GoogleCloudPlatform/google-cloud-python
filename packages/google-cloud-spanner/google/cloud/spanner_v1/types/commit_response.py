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

from google.cloud.spanner_v1.types import location, transaction

__protobuf__ = proto.module(
    package="google.spanner.v1",
    manifest={
        "CommitResponse",
    },
)


class CommitResponse(proto.Message):
    r"""The response for [Commit][google.spanner.v1.Spanner.Commit].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        commit_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The Cloud Spanner timestamp at which the
            transaction committed.
        commit_stats (google.cloud.spanner_v1.types.CommitResponse.CommitStats):
            The statistics about this ``Commit``. Not returned by
            default. For more information, see
            [CommitRequest.return_commit_stats][google.spanner.v1.CommitRequest.return_commit_stats].
        precommit_token (google.cloud.spanner_v1.types.MultiplexedSessionPrecommitToken):
            If specified, transaction has not committed
            yet. You must retry the commit with the new
            precommit token.

            This field is a member of `oneof`_ ``MultiplexedSessionRetry``.
        snapshot_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            If ``TransactionOptions.isolation_level`` is set to
            ``IsolationLevel.REPEATABLE_READ``, then the snapshot
            timestamp is the timestamp at which all reads in the
            transaction ran. This timestamp is never returned.
        cache_update (google.cloud.spanner_v1.types.CacheUpdate):
            Optional. A cache update expresses a set of changes the
            client should incorporate into its location cache. The
            client should discard the changes if they are older than the
            data it already has. This data can be obtained in response
            to requests that included a ``RoutingHint`` field, but may
            also be obtained by explicit location-fetching RPCs which
            may be added in the future.
        isolation_level (google.cloud.spanner_v1.types.TransactionOptions.IsolationLevel):
            The isolation level used for the read-write
            transaction.
        read_lock_mode (google.cloud.spanner_v1.types.TransactionOptions.ReadWrite.ReadLockMode):
            The read lock mode used for the read-write
            transaction.
    """

    class CommitStats(proto.Message):
        r"""Additional statistics about a commit.

        Attributes:
            mutation_count (int):
                The total number of mutations for the transaction. Knowing
                the ``mutation_count`` value can help you maximize the
                number of mutations in a transaction and minimize the number
                of API round trips. You can also monitor this value to
                prevent transactions from exceeding the system
                `limit <https://cloud.google.com/spanner/quotas#limits_for_creating_reading_updating_and_deleting_data>`__.
                If the number of mutations exceeds the limit, the server
                returns
                `INVALID_ARGUMENT <https://cloud.google.com/spanner/docs/reference/rest/v1/Code#ENUM_VALUES.INVALID_ARGUMENT>`__.
        """

        mutation_count: int = proto.Field(
            proto.INT64,
            number=1,
        )

    commit_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    commit_stats: CommitStats = proto.Field(
        proto.MESSAGE,
        number=2,
        message=CommitStats,
    )
    precommit_token: transaction.MultiplexedSessionPrecommitToken = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="MultiplexedSessionRetry",
        message=transaction.MultiplexedSessionPrecommitToken,
    )
    snapshot_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    cache_update: location.CacheUpdate = proto.Field(
        proto.MESSAGE,
        number=6,
        message=location.CacheUpdate,
    )
    isolation_level: transaction.TransactionOptions.IsolationLevel = proto.Field(
        proto.ENUM,
        number=7,
        enum=transaction.TransactionOptions.IsolationLevel,
    )
    read_lock_mode: transaction.TransactionOptions.ReadWrite.ReadLockMode = proto.Field(
        proto.ENUM,
        number=8,
        enum=transaction.TransactionOptions.ReadWrite.ReadLockMode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
