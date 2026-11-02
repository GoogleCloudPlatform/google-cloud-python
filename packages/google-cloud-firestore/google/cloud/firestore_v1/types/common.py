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

__protobuf__ = proto.module(
    package="google.firestore.v1",
    manifest={
        "DocumentMask",
        "Precondition",
        "TransactionOptions",
        "RequestOptions",
    },
)


class DocumentMask(proto.Message):
    r"""A set of field paths on a document. Used to restrict a get or update
    operation on a document to a subset of its fields. This is different
    from standard field masks, as this is always scoped to a
    [Document][google.firestore.v1.Document], and takes in account the
    dynamic nature of [Value][google.firestore.v1.Value].

    Attributes:
        field_paths (MutableSequence[str]):
            The list of field paths in the mask. See
            [Document.fields][google.firestore.v1.Document.fields] for a
            field path syntax reference.
    """

    field_paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Precondition(proto.Message):
    r"""A precondition on a document, used for conditional
    operations.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        exists (bool):
            When set to ``true``, the target document must exist. When
            set to ``false``, the target document must not exist.

            This field is a member of `oneof`_ ``condition_type``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            When set, the target document must exist and
            have been last updated at that time. Timestamp
            must be microsecond aligned.

            This field is a member of `oneof`_ ``condition_type``.
    """

    exists: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="condition_type",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="condition_type",
        message=timestamp_pb2.Timestamp,
    )


class TransactionOptions(proto.Message):
    r"""Options for creating a new transaction.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_only (google.cloud.firestore_v1.types.TransactionOptions.ReadOnly):
            The transaction can only be used for read
            operations.

            This field is a member of `oneof`_ ``mode``.
        read_write (google.cloud.firestore_v1.types.TransactionOptions.ReadWrite):
            The transaction can be used for both read and
            write operations.

            This field is a member of `oneof`_ ``mode``.
    """

    class ConcurrencyMode(proto.Enum):
        r"""The type of concurrency control mode for transactions.

        Values:
            CONCURRENCY_MODE_UNSPECIFIED (0):
                Start the transaction with the database-level
                default concurrency mode.
            OPTIMISTIC (1):
                Use optimistic concurrency control for the
                new transaction.
            PESSIMISTIC (2):
                Use pessimistic concurrency control for the
                new transaction.
        """

        CONCURRENCY_MODE_UNSPECIFIED = 0
        OPTIMISTIC = 1
        PESSIMISTIC = 2

    class ReadWrite(proto.Message):
        r"""Options for a transaction that can be used to read and write
        documents.

        Attributes:
            retry_transaction (bytes):
                An optional transaction to retry.
            concurrency_mode (google.cloud.firestore_v1.types.TransactionOptions.ConcurrencyMode):
                Optional. The concurrency control mode to use
                for this transaction.
                A database is able to use different concurrency
                modes for different transactions simultaneously.

                3rd party auth requests are only allowed to
                create optimistic read-write transactions and
                must specify that here even if the
                database-level setting is already configured to
                optimistic.
        """

        retry_transaction: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )
        concurrency_mode: "TransactionOptions.ConcurrencyMode" = proto.Field(
            proto.ENUM,
            number=2,
            enum="TransactionOptions.ConcurrencyMode",
        )

    class ReadOnly(proto.Message):
        r"""Options for a transaction that can only be used to read
        documents.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            read_time (google.protobuf.timestamp_pb2.Timestamp):
                Reads documents at the given time.

                This must be a microsecond precision timestamp
                within the past one hour, or if Point-in-Time
                Recovery is enabled, can additionally be a whole
                minute timestamp within the past 7 days.

                This field is a member of `oneof`_ ``consistency_selector``.
        """

        read_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="consistency_selector",
            message=timestamp_pb2.Timestamp,
        )

    read_only: ReadOnly = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="mode",
        message=ReadOnly,
    )
    read_write: ReadWrite = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="mode",
        message=ReadWrite,
    )


class RequestOptions(proto.Message):
    r"""Options for a server request.

    Attributes:
        request_tags (MutableSequence[str]):
            The request tags for the request.
    """

    request_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
