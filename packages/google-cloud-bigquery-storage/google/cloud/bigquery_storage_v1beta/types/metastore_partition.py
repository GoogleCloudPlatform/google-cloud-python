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

from google.cloud.bigquery_storage_v1beta.types import partition

__protobuf__ = proto.module(
    package="google.cloud.bigquery.storage.v1beta",
    manifest={
        "CreateMetastorePartitionRequest",
        "BatchCreateMetastorePartitionsRequest",
        "BatchCreateMetastorePartitionsResponse",
        "BatchDeleteMetastorePartitionsRequest",
        "UpdateMetastorePartitionRequest",
        "BatchUpdateMetastorePartitionsRequest",
        "BatchUpdateMetastorePartitionsResponse",
        "ListMetastorePartitionsRequest",
        "ListMetastorePartitionsResponse",
        "StreamMetastorePartitionsRequest",
        "StreamMetastorePartitionsResponse",
        "BatchSizeTooLargeError",
    },
)


class CreateMetastorePartitionRequest(proto.Message):
    r"""Request message for CreateMetastorePartition. The
    MetastorePartition is uniquely identified by values, which is an
    ordered list. Hence, there is no separate name or partition id
    field.

    Attributes:
        parent (str):
            Required. Reference to the table to where the
            metastore partition to be added, in the format
            of
            projects/{project}/databases/{databases}/tables/{table}.
        metastore_partition (google.cloud.bigquery_storage_v1beta.types.MetastorePartition):
            Required. The metastore partition to be
            added.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metastore_partition: partition.MetastorePartition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=partition.MetastorePartition,
    )


class BatchCreateMetastorePartitionsRequest(proto.Message):
    r"""Request message for BatchCreateMetastorePartitions.

    Attributes:
        parent (str):
            Required. Reference to the table to where the
            metastore partitions to be added, in the format
            of
            projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.
        requests (MutableSequence[google.cloud.bigquery_storage_v1beta.types.CreateMetastorePartitionRequest]):
            Required. Requests to add metastore
            partitions to the table.
        skip_existing_partitions (bool):
            Optional. Mimics the ifNotExists flag in IMetaStoreClient
            add_partitions(..). If the flag is set to false, the server
            will return ALREADY_EXISTS if any partition already exists.
            If the flag is set to true, the server will skip existing
            partitions and insert only the non-existing partitions. A
            maximum of 900 partitions can be inserted in a batch.
        trace_id (str):
            Optional. Optional trace id to be used for debugging. It is
            expected that the client sets the same ``trace_id`` for all
            the batches in the same operation, so that it is possible to
            tie together the logs to all the batches in the same
            operation. Limited to 256 characters. This is expected, but
            not required, to be globally unique.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateMetastorePartitionRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateMetastorePartitionRequest",
    )
    skip_existing_partitions: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class BatchCreateMetastorePartitionsResponse(proto.Message):
    r"""Response message for BatchCreateMetastorePartitions.

    Attributes:
        partitions (MutableSequence[google.cloud.bigquery_storage_v1beta.types.MetastorePartition]):
            The list of metastore partitions that have
            been created.
    """

    partitions: MutableSequence[partition.MetastorePartition] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=partition.MetastorePartition,
    )


class BatchDeleteMetastorePartitionsRequest(proto.Message):
    r"""Request message for BatchDeleteMetastorePartitions. The
    MetastorePartition is uniquely identified by values, which is an
    ordered list. Hence, there is no separate name or partition id
    field.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these metastore partitions belong, in the format
            of
            projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.
        partition_values (MutableSequence[google.cloud.bigquery_storage_v1beta.types.MetastorePartitionValues]):
            Required. The list of metastore partitions
            (identified by its values) to be deleted. A
            maximum of 900 partitions can be deleted in a
            batch.
        trace_id (str):
            Optional. Optional trace id to be used for debugging. It is
            expected that the client sets the same ``trace_id`` for all
            the batches in the same operation, so that it is possible to
            tie together the logs to all the batches in the same
            operation. This is expected, but not required, to be
            globally unique.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partition_values: MutableSequence[partition.MetastorePartitionValues] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=partition.MetastorePartitionValues,
        )
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMetastorePartitionRequest(proto.Message):
    r"""Request message for UpdateMetastorePartition.

    Attributes:
        metastore_partition (google.cloud.bigquery_storage_v1beta.types.MetastorePartition):
            Required. The metastore partition to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    metastore_partition: partition.MetastorePartition = proto.Field(
        proto.MESSAGE,
        number=1,
        message=partition.MetastorePartition,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateMetastorePartitionsRequest(proto.Message):
    r"""Request message for BatchUpdateMetastorePartitions.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these metastore partitions belong, in the format
            of
            projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.
        requests (MutableSequence[google.cloud.bigquery_storage_v1beta.types.UpdateMetastorePartitionRequest]):
            Required. Requests to update metastore
            partitions in the table.
        trace_id (str):
            Optional. Optional trace id to be used for debugging. It is
            expected that the client sets the same ``trace_id`` for all
            the batches in the same operation, so that it is possible to
            tie together the logs to all the batches in the same
            operation. This is expected, but not required, to be
            globally unique.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateMetastorePartitionRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateMetastorePartitionRequest",
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class BatchUpdateMetastorePartitionsResponse(proto.Message):
    r"""Response message for BatchUpdateMetastorePartitions.

    Attributes:
        partitions (MutableSequence[google.cloud.bigquery_storage_v1beta.types.MetastorePartition]):
            The list of metastore partitions that have
            been updated. A maximum of 900 partitions can be
            updated in a batch.
    """

    partitions: MutableSequence[partition.MetastorePartition] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=partition.MetastorePartition,
    )


class ListMetastorePartitionsRequest(proto.Message):
    r"""Request message for ListMetastorePartitions.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these metastore partitions belong, in the format
            of
            projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.
        filter (str):
            Optional. SQL text filtering statement, similar to a WHERE
            clause in a query. Only supports single-row expressions.
            Aggregate functions are not supported.

            Examples:

            - "int_field > 5"
            - "date_field = CAST('2014-9-27' as DATE)"
            - "nullable_field is not NULL"
            - "st_equals(geo_field, st_geofromtext("POINT(2, 2)"))"
            - "numeric_field BETWEEN 1.0 AND 5.0"

            Restricted to a maximum length of 1 MB.
        trace_id (str):
            Optional. Optional trace id to be used for debugging. It is
            expected that the client sets the same ``trace_id`` for all
            the batches in the same operation, so that it is possible to
            tie together the logs to all the batches in the same
            operation. Limited to 256 characters. This is expected, but
            not required, to be globally unique.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListMetastorePartitionsResponse(proto.Message):
    r"""Response message for ListMetastorePartitions.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        partitions (google.cloud.bigquery_storage_v1beta.types.MetastorePartitionList):
            The list of partitions.

            This field is a member of `oneof`_ ``response``.
        streams (google.cloud.bigquery_storage_v1beta.types.StreamList):
            The list of streams.

            This field is a member of `oneof`_ ``response``.
    """

    partitions: partition.MetastorePartitionList = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message=partition.MetastorePartitionList,
    )
    streams: partition.StreamList = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="response",
        message=partition.StreamList,
    )


class StreamMetastorePartitionsRequest(proto.Message):
    r"""The top-level message sent by the client to the
    [Partitions.StreamMetastorePartitions][] method. Follows the default
    gRPC streaming maximum size of 4 MB.

    Attributes:
        parent (str):
            Required. Reference to the table to where the
            partition to be added, in the format of
            projects/{project}/locations/{location}/datasets/{dataset}/tables/{table}.
        metastore_partitions (MutableSequence[google.cloud.bigquery_storage_v1beta.types.MetastorePartition]):
            Optional. A list of metastore partitions to
            be added to the table.
        skip_existing_partitions (bool):
            Optional. Mimics the ifNotExists flag in IMetaStoreClient
            add_partitions(..). If the flag is set to false, the server
            will return ALREADY_EXISTS on commit if any partition
            already exists. If the flag is set to true:

            1) the server will skip existing partitions insert only the
               non-existing partitions as part of the commit.
            2) The client must set the ``skip_existing_partitions``
               field to true for all requests in the stream.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metastore_partitions: MutableSequence[partition.MetastorePartition] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=partition.MetastorePartition,
        )
    )
    skip_existing_partitions: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class StreamMetastorePartitionsResponse(proto.Message):
    r"""This is the response message sent by the server to the client for
    the [Partitions.StreamMetastorePartitions][] method when the commit
    is successful. Server will close the stream after sending this
    message.

    Attributes:
        total_partitions_streamed_count (int):
            Total count of partitions streamed by the
            client during the lifetime of the stream. This
            is only set in the final response message before
            closing the stream.
        total_partitions_inserted_count (int):
            Total count of partitions inserted by the
            server during the lifetime of the stream. This
            is only set in the final response message before
            closing the stream.
    """

    total_partitions_streamed_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    total_partitions_inserted_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class BatchSizeTooLargeError(proto.Message):
    r"""Structured custom error message for batch size too large
    error. The error can be attached as error details in the
    returned rpc Status for more structured error handling in the
    client.

    Attributes:
        max_batch_size (int):
            The maximum number of items that are
            supported in a single batch. This is returned as
            a hint to the client to adjust the batch size.
        error_message (str):
            Optional. The error message that is returned
            to the client.
    """

    max_batch_size: int = proto.Field(
        proto.INT64,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
