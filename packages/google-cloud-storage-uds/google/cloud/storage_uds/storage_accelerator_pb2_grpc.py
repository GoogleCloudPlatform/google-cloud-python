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

"""gRPC client stub for `google.cloud.storage.accelerator.v1.StorageAccelerator`."""

from __future__ import annotations

from typing import Any

import grpc

from google.cloud.storage_uds import storage_accelerator_pb2 as pb2

SERVICE_PREFIX = "/google.cloud.storage.accelerator.v1.StorageAccelerator"


class StorageAcceleratorStub:
    """gRPC client stub compatible with both `grpc.Channel` and `grpc.aio.Channel`."""

    def __init__(self, channel: grpc.Channel | grpc.aio.Channel) -> None:
        """Bind stub methods to the underlying sync or async gRPC channel.

        Args:
            channel: A sync `grpc.Channel` or async `grpc.aio.Channel` connected
                to the `gcs-accelerator-server` Unix Domain Socket.
        """
        self.Ping: Any = channel.unary_unary(
            f"{SERVICE_PREFIX}/Ping",
            request_serializer=pb2.PingRequest.SerializeToString,
            response_deserializer=pb2.PingResponse.FromString,
        )
        self.ReadRanges: Any = channel.unary_unary(
            f"{SERVICE_PREFIX}/ReadRanges",
            request_serializer=pb2.ReadRangesRequest.SerializeToString,
            response_deserializer=pb2.ReadRangesResponse.FromString,
        )
        self.ReadObjectStream: Any = channel.unary_stream(
            f"{SERVICE_PREFIX}/ReadObjectStream",
            request_serializer=pb2.ReadRangesRequest.SerializeToString,
            response_deserializer=pb2.ReadRangeChunk.FromString,
        )
        self.WriteObject: Any = channel.unary_unary(
            f"{SERVICE_PREFIX}/WriteObject",
            request_serializer=pb2.WriteObjectRequest.SerializeToString,
            response_deserializer=pb2.ObjectMetadata.FromString,
        )
        self.ListObjects: Any = channel.unary_unary(
            f"{SERVICE_PREFIX}/ListObjects",
            request_serializer=pb2.ListObjectsRequest.SerializeToString,
            response_deserializer=pb2.ListObjectsResponse.FromString,
        )

