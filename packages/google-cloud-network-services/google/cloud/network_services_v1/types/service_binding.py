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

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "ServiceBinding",
        "ListServiceBindingsRequest",
        "ListServiceBindingsResponse",
        "GetServiceBindingRequest",
        "CreateServiceBindingRequest",
        "UpdateServiceBindingRequest",
        "DeleteServiceBindingRequest",
    },
)


class ServiceBinding(proto.Message):
    r"""ServiceBinding can be used to:

    - Bind a Service Directory Service to be used in a
      BackendService resource.   This feature will be deprecated
      soon.
    - Bind a Private Service Connect producer service to be used in
      consumer   Cloud Service Mesh or Application Load Balancers.
    - Bind a Cloud Run service to be used in consumer Cloud Service
      Mesh or   Application Load Balancers.

    Attributes:
        name (str):
            Identifier. Name of the ServiceBinding resource. It matches
            pattern
            ``projects/*/locations/*/serviceBindings/<service_binding_name>``.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        service (str):
            Optional. The full Service Directory Service name of the
            format ``projects/*/locations/*/namespaces/*/services/*``.
            This field is for Service Directory integration which will
            be deprecated soon.
        service_id (str):
            Output only. The unique identifier of the
            Service Directory Service against which the
            ServiceBinding resource is validated. This is
            populated when the Service Binding resource is
            used in another resource (like Backend Service).
            This is of the UUID4 format. This field is for
            Service Directory integration which will be
            deprecated soon.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the ServiceBinding resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    service: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class ListServiceBindingsRequest(proto.Message):
    r"""Request used with the ListServiceBindings method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ServiceBindings should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of ServiceBindings to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListServiceBindingsResponse`` Indicates that this is a
            continuation of a prior ``ListRouters`` call, and that the
            system should return the next page of data.
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


class ListServiceBindingsResponse(proto.Message):
    r"""Response returned by the ListServiceBindings method.

    Attributes:
        service_bindings (MutableSequence[google.cloud.network_services_v1.types.ServiceBinding]):
            List of ServiceBinding resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the
            request attempts to list all resources across
            all supported locations, while some locations
            are temporarily unavailable.
    """

    @property
    def raw_page(self):
        return self

    service_bindings: MutableSequence["ServiceBinding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ServiceBinding",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServiceBindingRequest(proto.Message):
    r"""Request used by the GetServiceBinding method.

    Attributes:
        name (str):
            Required. A name of the ServiceBinding to get. Must be in
            the format ``projects/*/locations/*/serviceBindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceBindingRequest(proto.Message):
    r"""Request used by the ServiceBinding method.

    Attributes:
        parent (str):
            Required. The parent resource of the ServiceBinding. Must be
            in the format ``projects/*/locations/*``.
        service_binding_id (str):
            Required. Short name of the ServiceBinding
            resource to be created.
        service_binding (google.cloud.network_services_v1.types.ServiceBinding):
            Required. ServiceBinding resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_binding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_binding: "ServiceBinding" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceBinding",
    )


class UpdateServiceBindingRequest(proto.Message):
    r"""Request used by the UpdateServiceBinding method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServiceBinding resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        service_binding (google.cloud.network_services_v1.types.ServiceBinding):
            Required. Updated ServiceBinding resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    service_binding: "ServiceBinding" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceBinding",
    )


class DeleteServiceBindingRequest(proto.Message):
    r"""Request used by the DeleteServiceBinding method.

    Attributes:
        name (str):
            Required. A name of the ServiceBinding to delete. Must be in
            the format ``projects/*/locations/*/serviceBindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
