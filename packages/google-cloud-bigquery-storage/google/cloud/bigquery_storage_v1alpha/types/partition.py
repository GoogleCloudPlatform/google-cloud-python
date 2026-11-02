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
    package="google.cloud.bigquery.storage.v1alpha",
    manifest={
        "FieldSchema",
        "StorageDescriptor",
        "SerDeInfo",
        "MetastorePartition",
        "MetastorePartitionList",
        "ReadStream",
        "StreamList",
        "MetastorePartitionValues",
    },
)


class FieldSchema(proto.Message):
    r"""Schema description of a metastore partition column.

    Attributes:
        name (str):
            Required. The name of the column.
            The maximum length of the name is 1024
            characters
        type_ (str):
            Required. The type of the metastore partition
            column. Maximum allowed length is 1024
            characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StorageDescriptor(proto.Message):
    r"""Contains information about the physical storage of the data
    in the metastore partition.

    Attributes:
        location_uri (str):
            Optional. The physical location of the metastore partition
            (e.g.
            ``gs://spark-dataproc-data/pangea-data/case_sensitive/`` or
            ``gs://spark-dataproc-data/pangea-data/*``).
        input_format (str):
            Optional. Specifies the fully qualified class
            name of the InputFormat (e.g.
            "org.apache.hadoop.hive.ql.io.orc.OrcInputFormat").
            The maximum length is 128 characters.
        output_format (str):
            Optional. Specifies the fully qualified class
            name of the OutputFormat (e.g.
            "org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat").
            The maximum length is 128 characters.
        serde_info (google.cloud.bigquery_storage_v1alpha.types.SerDeInfo):
            Optional. Serializer and deserializer
            information.
    """

    location_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_format: str = proto.Field(
        proto.STRING,
        number=2,
    )
    output_format: str = proto.Field(
        proto.STRING,
        number=3,
    )
    serde_info: "SerDeInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SerDeInfo",
    )


class SerDeInfo(proto.Message):
    r"""Serializer and deserializer information.

    Attributes:
        name (str):
            Optional. Name of the SerDe.
            The maximum length is 256 characters.
        serialization_library (str):
            Required. Specifies a fully-qualified class
            name of the serialization library that is
            responsible for the translation of data between
            table representation and the underlying
            low-level input and output format structures.
            The maximum length is 256 characters.
        parameters (MutableMapping[str, str]):
            Optional. Key-value pairs that define the
            initialization parameters for the serialization
            library. Maximum size 10 Kib.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serialization_library: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class MetastorePartition(proto.Message):
    r"""Information about a Hive partition.

    Attributes:
        values (MutableSequence[str]):
            Required. Represents the values of the
            partition keys, where each value corresponds to
            a specific partition key in the order in which
            the keys are defined. Each value is limited to
            1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            partition.
        storage_descriptor (google.cloud.bigquery_storage_v1alpha.types.StorageDescriptor):
            Optional. Contains information about the
            physical storage of the data in the partition.
        parameters (MutableMapping[str, str]):
            Optional. Additional parameters or metadata
            associated with the partition. Maximum size 10
            KiB.
        fields (MutableSequence[google.cloud.bigquery_storage_v1alpha.types.FieldSchema]):
            Optional. List of columns.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    storage_descriptor: "StorageDescriptor" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StorageDescriptor",
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    fields: MutableSequence["FieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="FieldSchema",
    )


class MetastorePartitionList(proto.Message):
    r"""List of metastore partitions.

    Attributes:
        partitions (MutableSequence[google.cloud.bigquery_storage_v1alpha.types.MetastorePartition]):
            Required. List of partitions.
    """

    partitions: MutableSequence["MetastorePartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MetastorePartition",
    )


class ReadStream(proto.Message):
    r"""Information about a single stream that is used to read
    partitions.

    Attributes:
        name (str):
            Output only. Identifier. Name of the stream, in the form
            ``projects/{project_id}/locations/{location}/sessions/{session_id}/streams/{stream_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StreamList(proto.Message):
    r"""List of streams.

    Attributes:
        streams (MutableSequence[google.cloud.bigquery_storage_v1alpha.types.ReadStream]):
            Output only. List of streams.
    """

    streams: MutableSequence["ReadStream"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReadStream",
    )


class MetastorePartitionValues(proto.Message):
    r"""Represents the values of a metastore partition.

    Attributes:
        values (MutableSequence[str]):
            Required. The values of the partition keys,
            where each value corresponds to a specific
            partition key in the order in which the keys are
            defined.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
