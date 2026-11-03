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

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "ExecuteOntapPostRequest",
        "ExecuteOntapPostResponse",
        "ExecuteOntapGetRequest",
        "ExecuteOntapGetResponse",
        "ExecuteOntapDeleteRequest",
        "ExecuteOntapDeleteResponse",
        "ExecuteOntapPatchRequest",
        "ExecuteOntapPatchResponse",
    },
)


class ExecuteOntapPostRequest(proto.Message):
    r"""Request message for ``ExecuteOntapPost`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            Required. The raw ``JSON`` body of the request. The body
            should be in the format of the ONTAP resource. For example:

            ::

               {
                 "body": {
                   "field1": "value1",
                   "field2": "value2",
                 }
               }
        ontap_path (str):
            Required. The path of the ONTAP resource. Format:
            ``projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}``.
            For example:
            ``projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes``.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    ontap_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExecuteOntapPostResponse(proto.Message):
    r"""Response message for ``ExecuteOntapPost`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            The raw ``JSON`` body of the response.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class ExecuteOntapGetRequest(proto.Message):
    r"""Request message for ``ExecuteOntapGet`` API.

    Attributes:
        ontap_path (str):
            Required. The resource path of the ONTAP resource. Format:
            ``projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}``.
            For example:
            ``projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes``.
    """

    ontap_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecuteOntapGetResponse(proto.Message):
    r"""Response message for ``ExecuteOntapGet`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            The raw ``JSON`` body of the response.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class ExecuteOntapDeleteRequest(proto.Message):
    r"""Request message for ``ExecuteOntapDelete`` API.

    Attributes:
        ontap_path (str):
            Required. The resource path of the ONTAP resource. Format:
            ``projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}``.
            For example:
            ``projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes``.
    """

    ontap_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExecuteOntapDeleteResponse(proto.Message):
    r"""Response message for ``ExecuteOntapDelete`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            The raw ``JSON`` body of the response.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class ExecuteOntapPatchRequest(proto.Message):
    r"""Request message for ``ExecuteOntapPatch`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            Required. The raw ``JSON`` body of the request. The body
            should be in the format of the ONTAP resource. For example:

            ::

               {
                 "body": {
                   "field1": "value1",
                   "field2": "value2",
                 }
               }
        ontap_path (str):
            Required. The resource path of the ONTAP resource. Format:
            ``projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}``.
            For example:
            ``projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes``.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    ontap_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExecuteOntapPatchResponse(proto.Message):
    r"""Response message for ``ExecuteOntapPatch`` API.

    Attributes:
        body (google.protobuf.struct_pb2.Struct):
            The raw ``JSON`` body of the response.
    """

    body: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
