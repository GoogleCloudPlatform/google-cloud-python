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

from google.cloud.network_services_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "Mesh",
        "ListMeshesRequest",
        "ListMeshesResponse",
        "GetMeshRequest",
        "CreateMeshRequest",
        "UpdateMeshRequest",
        "DeleteMeshRequest",
    },
)


class Mesh(proto.Message):
    r"""Mesh represents a logical configuration grouping for workload
    to workload communication within a service mesh. Routes that
    point to mesh dictate how requests are routed within this
    logical mesh boundary.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the Mesh resource. It matches pattern
            ``projects/*/locations/*/meshes/<mesh_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the Mesh resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        interception_port (int):
            Optional. If set to a valid TCP port
            (1-65535), instructs the SIDECAR proxy to listen
            on the specified port of localhost (127.0.0.1)
            address. The SIDECAR proxy will expect all
            traffic to be redirected to this port regardless
            of its actual ip:port destination. If unset, a
            port '15001' is used as the interception port.
            This is applicable only for sidecar proxy
            deployments.
        envoy_headers (google.cloud.network_services_v1.types.EnvoyHeaders):
            Optional. Determines if envoy will insert
            internal debug headers into upstream requests.
            Other Envoy headers may still be injected. By
            default, envoy will not insert any debug
            headers.

            This field is a member of `oneof`_ ``_envoy_headers``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    interception_port: int = proto.Field(
        proto.INT32,
        number=8,
    )
    envoy_headers: common.EnvoyHeaders = proto.Field(
        proto.ENUM,
        number=16,
        optional=True,
        enum=common.EnvoyHeaders,
    )


class ListMeshesRequest(proto.Message):
    r"""Request used with the ListMeshes method.

    Attributes:
        parent (str):
            Required. The project and location from which the Meshes
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of Meshes to return per call.
        page_token (str):
            The value returned by the last ``ListMeshesResponse``
            Indicates that this is a continuation of a prior
            ``ListMeshes`` call, and that the system should return the
            next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
            Otherwise if one of the locations is down or
            unreachable, the Aggregated List request will
            fail.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListMeshesResponse(proto.Message):
    r"""Response returned by the ListMeshes method.

    Attributes:
        meshes (MutableSequence[google.cloud.network_services_v1.types.Mesh]):
            List of Mesh resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            ``return_partial_success`` and reading across collections
            e.g. when attempting to list all resources across all
            supported locations.
    """

    @property
    def raw_page(self):
        return self

    meshes: MutableSequence["Mesh"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Mesh",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMeshRequest(proto.Message):
    r"""Request used by the GetMesh method.

    Attributes:
        name (str):
            Required. A name of the Mesh to get. Must be in the format
            ``projects/*/locations/*/meshes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMeshRequest(proto.Message):
    r"""Request used by the CreateMesh method.

    Attributes:
        parent (str):
            Required. The parent resource of the Mesh. Must be in the
            format ``projects/*/locations/*``.
        mesh_id (str):
            Required. Short name of the Mesh resource to
            be created.
        mesh (google.cloud.network_services_v1.types.Mesh):
            Required. Mesh resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mesh_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mesh: "Mesh" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Mesh",
    )


class UpdateMeshRequest(proto.Message):
    r"""Request used by the UpdateMesh method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Mesh resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        mesh (google.cloud.network_services_v1.types.Mesh):
            Required. Updated Mesh resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    mesh: "Mesh" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Mesh",
    )


class DeleteMeshRequest(proto.Message):
    r"""Request used by the DeleteMesh method.

    Attributes:
        name (str):
            Required. A name of the Mesh to delete. Must be in the
            format ``projects/*/locations/*/meshes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
