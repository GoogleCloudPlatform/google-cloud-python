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

import google.rpc.context.attribute_context_pb2 as attribute_context_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v2",
    manifest={
        "CheckRequest",
        "ResourceInfo",
        "CheckResponse",
        "ReportRequest",
        "ReportResponse",
        "ResourceInfoList",
    },
)


class CheckRequest(proto.Message):
    r"""Request message for the Check method.

    Attributes:
        service_name (str):
            The service name as specified in its service configuration.
            For example, ``"pubsub.googleapis.com"``.

            See
            `google.api.Service <https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service>`__
            for the definition of a service name.
        service_config_id (str):
            Specifies the version of the service
            configuration that should be used to process the
            request. Must not be empty. Set this field to
            'latest' to specify using the latest
            configuration.
        attributes (google.rpc.context.attribute_context_pb2.AttributeContext):
            Describes attributes about the operation
            being executed by the service.
        resources (MutableSequence[google.cloud.servicecontrol_v2.types.ResourceInfo]):
            Describes the resources and the policies
            applied to each resource.
        flags (str):
            Optional. Contains a comma-separated list of
            flags.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attributes: attribute_context_pb2.AttributeContext = proto.Field(
        proto.MESSAGE,
        number=3,
        message=attribute_context_pb2.AttributeContext,
    )
    resources: MutableSequence["ResourceInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ResourceInfo",
    )
    flags: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ResourceInfo(proto.Message):
    r"""Describes a resource referenced in the request.

    Attributes:
        name (str):
            The name of the resource referenced in the
            request.
        type_ (str):
            The resource type in the format of
            "{service}/{kind}".
        permission (str):
            The resource permission needed for this
            request. The format must be
            "{service}/{plural}.{verb}".
        container (str):
            Optional. The identifier of the container of this resource.
            For Google Cloud APIs, the resource container must be one of
            the following formats: -
            ``projects/<project-id or project-number>`` -
            ``folders/<folder-number>`` -
            ``organizations/<organization-number>`` Required for the
            policy enforcement on the container level (e.g. VPCSC,
            Location Policy check, Org Policy check).
        location (str):
            Optional. The location of the resource, it
            must be a valid zone, region or multiregion, for
            example: "europe-west4",
            "northamerica-northeast1-a". Required for
            location policy check.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permission: str = proto.Field(
        proto.STRING,
        number=3,
    )
    container: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CheckResponse(proto.Message):
    r"""Response message for the Check method.

    Attributes:
        status (google.rpc.status_pb2.Status):
            Operation is allowed when this field is not set. Any
            non-'OK' status indicates a denial;
            [google.rpc.Status.details][google.rpc.Status.details] would
            contain additional details about the denial.
        headers (MutableMapping[str, str]):
            Returns a set of request contexts generated from the
            ``CheckRequest``.
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class ReportRequest(proto.Message):
    r"""Request message for the Report method.

    Attributes:
        service_name (str):
            The service name as specified in its service configuration.
            For example, ``"pubsub.googleapis.com"``.

            See
            `google.api.Service <https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service>`__
            for the definition of a service name.
        service_config_id (str):
            Specifies the version of the service
            configuration that should be used to process the
            request. Must not be empty. Set this field to
            'latest' to specify using the latest
            configuration.
        operations (MutableSequence[google.rpc.context.attribute_context_pb2.AttributeContext]):
            Describes the list of operations to be
            reported. Each operation is represented as an
            AttributeContext, and contains all attributes
            around an API access.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operations: MutableSequence[attribute_context_pb2.AttributeContext] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=attribute_context_pb2.AttributeContext,
        )
    )


class ReportResponse(proto.Message):
    r"""Response message for the Report method.
    If the request contains any invalid data, the server returns an
    RPC error.

    """


class ResourceInfoList(proto.Message):
    r"""Message containing resource details in a batch mode.

    Attributes:
        resources (MutableSequence[google.cloud.servicecontrol_v2.types.ResourceInfo]):
            The resource details.
    """

    resources: MutableSequence["ResourceInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ResourceInfo",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
