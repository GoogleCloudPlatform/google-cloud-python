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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.vectorsearch.v1",
    manifest={
        "DataObject",
        "Vector",
        "DenseVector",
        "SparseVector",
    },
)


class DataObject(proto.Message):
    r"""A dataObject resource in Vector Search.

    Attributes:
        name (str):
            Identifier. The fully qualified resource name of the
            dataObject.

            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/dataObjects/{data_object_id}``
            The data_object_id must be 1-63 characters long, and comply
            with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
        data_object_id (str):
            Output only. The id of the dataObject.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the dataObject was
            created at.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the dataObject was
            last updated.
        data (google.protobuf.struct_pb2.Struct):
            Optional. The data of the dataObject.
        vectors (MutableMapping[str, google.cloud.vectorsearch_v1.types.Vector]):
            Optional. The vectors of the dataObject.
        etag (str):
            Optional. The etag of the dataObject.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_object_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    data: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    vectors: MutableMapping[str, "Vector"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message="Vector",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )


class Vector(proto.Message):
    r"""A vector which can be either dense or sparse.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dense (google.cloud.vectorsearch_v1.types.DenseVector):
            A dense vector.

            This field is a member of `oneof`_ ``vector_type``.
        sparse (google.cloud.vectorsearch_v1.types.SparseVector):
            A sparse vector.

            This field is a member of `oneof`_ ``vector_type``.
    """

    dense: "DenseVector" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="vector_type",
        message="DenseVector",
    )
    sparse: "SparseVector" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="vector_type",
        message="SparseVector",
    )


class DenseVector(proto.Message):
    r"""A dense vector.

    Attributes:
        values (MutableSequence[float]):
            Required. The values of the vector.
    """

    values: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=1,
    )


class SparseVector(proto.Message):
    r"""A sparse vector.

    Attributes:
        values (MutableSequence[float]):
            Required. The values of the vector.
        indices (MutableSequence[int]):
            Required. The corresponding indices for the
            values.
    """

    values: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=1,
    )
    indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
