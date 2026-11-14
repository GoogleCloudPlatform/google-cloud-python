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

"""Protobuf message descriptors for `google.cloud.storage.accelerator.v1`.

Backed by `google.protobuf`'s native C/upb extension (`descriptor_pool` +
`message_factory`) matching `proto/storage_accelerator.proto`.
"""

from __future__ import annotations

from typing import Any

from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

PACKAGE_NAME = "google.cloud.storage.accelerator.v1"


def _add_field(
    msg: descriptor_pb2.DescriptorProto,
    name: str,
    number: int,
    field_type: int,
    label: int = descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL,
    type_name: str | None = None,
) -> None:
    """Append a field definition to a message descriptor proto."""
    field = msg.field.add()
    field.name = name
    field.number = number
    field.type = field_type
    field.label = label
    if type_name is not None:
        field.type_name = type_name


def _build_file_descriptor() -> descriptor_pb2.FileDescriptorProto:
    """Construct the `FileDescriptorProto` for `storage_accelerator.proto`."""
    fdp = descriptor_pb2.FileDescriptorProto()
    fdp.name = "storage_accelerator.proto"
    fdp.name = "storage_accelerator_v1_shm.proto"
    fdp.package = PACKAGE_NAME
    fdp.syntax = "proto3"

    f_type = descriptor_pb2.FieldDescriptorProto
    opt = f_type.LABEL_OPTIONAL
    rep = f_type.LABEL_REPEATED

    # 1. PingRequest
    ping_req = fdp.message_type.add()
    ping_req.name = "PingRequest"

    # 2. PingResponse
    ping_resp = fdp.message_type.add()
    ping_resp.name = "PingResponse"
    _add_field(ping_resp, "pid", 1, f_type.TYPE_UINT32, opt)
    _add_field(ping_resp, "worker_threads", 2, f_type.TYPE_UINT32, opt)
    _add_field(ping_resp, "version", 3, f_type.TYPE_STRING, opt)

    # 3. ByteRange
    byte_range = fdp.message_type.add()
    byte_range.name = "ByteRange"
    _add_field(byte_range, "offset", 1, f_type.TYPE_UINT64, opt)
    _add_field(byte_range, "length", 2, f_type.TYPE_UINT64, opt)

    # 4. ReadRangesRequest
    read_req = fdp.message_type.add()
    read_req.name = "ReadRangesRequest"
    _add_field(read_req, "bucket", 1, f_type.TYPE_STRING, opt)
    _add_field(read_req, "object", 2, f_type.TYPE_STRING, opt)
    _add_field(
        read_req,
        "ranges",
        3,
        f_type.TYPE_MESSAGE,
        rep,
        type_name=f".{PACKAGE_NAME}.ByteRange",
    )
    _add_field(read_req, "endpoint", 4, f_type.TYPE_STRING, opt)
    _add_field(read_req, "simulated", 5, f_type.TYPE_BOOL, opt)
    _add_field(read_req, "shm_path", 6, f_type.TYPE_STRING, opt)

    # 5. ReadRangesResponse
    read_resp = fdp.message_type.add()
    read_resp.name = "ReadRangesResponse"
    _add_field(read_resp, "chunks", 1, f_type.TYPE_BYTES, rep)
    _add_field(read_resp, "actual_lengths", 2, f_type.TYPE_UINT64, rep)

    # 6. ReadRangeChunk
    read_chunk = fdp.message_type.add()
    read_chunk.name = "ReadRangeChunk"
    _add_field(read_chunk, "range_index", 1, f_type.TYPE_UINT32, opt)
    _add_field(read_chunk, "data", 2, f_type.TYPE_BYTES, opt)

    # 7. WriteObjectRequest
    write_req = fdp.message_type.add()
    write_req.name = "WriteObjectRequest"
    _add_field(write_req, "bucket", 1, f_type.TYPE_STRING, opt)
    _add_field(write_req, "object", 2, f_type.TYPE_STRING, opt)
    _add_field(write_req, "data", 3, f_type.TYPE_BYTES, opt)
    _add_field(write_req, "endpoint", 4, f_type.TYPE_STRING, opt)
    _add_field(write_req, "simulated", 5, f_type.TYPE_BOOL, opt)
    _add_field(write_req, "shm_path", 6, f_type.TYPE_STRING, opt)
    _add_field(write_req, "shm_length", 7, f_type.TYPE_UINT64, opt)

    # 8. ObjectMetadata
    obj_meta = fdp.message_type.add()
    obj_meta.name = "ObjectMetadata"
    _add_field(obj_meta, "name", 1, f_type.TYPE_STRING, opt)
    _add_field(obj_meta, "bucket", 2, f_type.TYPE_STRING, opt)
    _add_field(obj_meta, "generation", 3, f_type.TYPE_INT64, opt)
    _add_field(obj_meta, "metageneration", 4, f_type.TYPE_INT64, opt)
    _add_field(obj_meta, "size", 5, f_type.TYPE_INT64, opt)
    _add_field(obj_meta, "storage_class", 6, f_type.TYPE_STRING, opt)
    _add_field(obj_meta, "etag", 7, f_type.TYPE_STRING, opt)
    _add_field(obj_meta, "crc32c", 8, f_type.TYPE_UINT32, opt)
    _add_field(obj_meta, "has_crc32c", 9, f_type.TYPE_BOOL, opt)

    # 9. ListObjectsRequest
    list_req = fdp.message_type.add()
    list_req.name = "ListObjectsRequest"
    _add_field(list_req, "bucket", 1, f_type.TYPE_STRING, opt)
    _add_field(list_req, "prefix", 2, f_type.TYPE_STRING, opt)
    _add_field(list_req, "delimiter", 3, f_type.TYPE_STRING, opt)
    _add_field(list_req, "versions", 4, f_type.TYPE_BOOL, opt)
    _add_field(list_req, "include_folders_as_prefixes", 5, f_type.TYPE_BOOL, opt)
    _add_field(list_req, "max_results", 6, f_type.TYPE_UINT32, opt)
    _add_field(list_req, "endpoint", 7, f_type.TYPE_STRING, opt)
    _add_field(list_req, "simulated_count", 8, f_type.TYPE_UINT32, opt)

    # 10. ListObjectsResponse
    list_resp = fdp.message_type.add()
    list_resp.name = "ListObjectsResponse"
    _add_field(
        list_resp,
        "objects",
        1,
        f_type.TYPE_MESSAGE,
        rep,
        type_name=f".{PACKAGE_NAME}.ObjectMetadata",
    )
    _add_field(list_resp, "prefixes", 2, f_type.TYPE_STRING, rep)

    return fdp


_POOL = descriptor_pool.Default()
try:
    _FILE_DESC = _POOL.FindFileByName("storage_accelerator.proto")
    _FILE_DESC = _POOL.FindFileByName("storage_accelerator_v1_shm.proto")
except KeyError:
    _FILE_DESC = _POOL.AddSerializedFile(_build_file_descriptor().SerializeToString())


def _msg_cls(name: str) -> Any:
    return message_factory.GetMessageClass(
        _FILE_DESC.message_types_by_name[name]
    )


PingRequest = _msg_cls("PingRequest")
PingResponse = _msg_cls("PingResponse")
ByteRange = _msg_cls("ByteRange")
ReadRangesRequest = _msg_cls("ReadRangesRequest")
ReadRangesResponse = _msg_cls("ReadRangesResponse")
ReadRangeChunk = _msg_cls("ReadRangeChunk")
WriteObjectRequest = _msg_cls("WriteObjectRequest")
ObjectMetadata = _msg_cls("ObjectMetadata")
ListObjectsRequest = _msg_cls("ListObjectsRequest")
ListObjectsResponse = _msg_cls("ListObjectsResponse")

