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
    package="google.cloud.networksecurity.v1beta1",
    manifest={
        "DnsThreatDetector",
        "ListDnsThreatDetectorsRequest",
        "ListDnsThreatDetectorsResponse",
        "GetDnsThreatDetectorRequest",
        "CreateDnsThreatDetectorRequest",
        "UpdateDnsThreatDetectorRequest",
        "DeleteDnsThreatDetectorRequest",
    },
)


class DnsThreatDetector(proto.Message):
    r"""A DNS threat detector sends DNS query logs to a *provider* that then
    analyzes the logs to identify threat events in the DNS queries. By
    default, all VPC networks in your projects are included. You can
    exclude specific networks by supplying ``excluded_networks``.

    Attributes:
        name (str):
            Immutable. Identifier. Name of the
            DnsThreatDetector resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Any labels associated with the
            DnsThreatDetector, listed as key value pairs.
        excluded_networks (MutableSequence[str]):
            Optional. A list of network resource names which aren't
            monitored by this DnsThreatDetector.

            Example:
            ``projects/PROJECT_ID/global/networks/NETWORK_NAME``.
        provider (google.cloud.network_security_v1beta1.types.DnsThreatDetector.Provider):
            Required. The provider used for DNS threat
            analysis.
    """

    class Provider(proto.Enum):
        r"""Name of the provider used for DNS threat analysis.

        Values:
            PROVIDER_UNSPECIFIED (0):
                An unspecified provider.
            INFOBLOX (1):
                The Infoblox DNS threat detector provider.
        """

        PROVIDER_UNSPECIFIED = 0
        INFOBLOX = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    excluded_networks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    provider: Provider = proto.Field(
        proto.ENUM,
        number=6,
        enum=Provider,
    )


class ListDnsThreatDetectorsRequest(proto.Message):
    r"""The message for requesting a list of DnsThreatDetectors in
    the project.

    Attributes:
        parent (str):
            Required. The parent value for
            ``ListDnsThreatDetectorsRequest``.
        page_size (int):
            Optional. The requested page size. The server
            may return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A page token received from a previous
            ``ListDnsThreatDetectorsRequest`` call. Provide this to
            retrieve the subsequent page.
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


class ListDnsThreatDetectorsResponse(proto.Message):
    r"""The response message to requesting a list of
    DnsThreatDetectors.

    Attributes:
        dns_threat_detectors (MutableSequence[google.cloud.network_security_v1beta1.types.DnsThreatDetector]):
            The list of DnsThreatDetector resources.
        next_page_token (str):
            A token, which can be sent as ``page_token``, to retrieve
            the next page.
        unreachable (MutableSequence[str]):
            Unordered list. Unreachable ``DnsThreatDetector`` resources.
    """

    @property
    def raw_page(self):
        return self

    dns_threat_detectors: MutableSequence["DnsThreatDetector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DnsThreatDetector",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDnsThreatDetectorRequest(proto.Message):
    r"""The message sent to get a DnsThreatDetector.

    Attributes:
        name (str):
            Required. Name of the DnsThreatDetector
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDnsThreatDetectorRequest(proto.Message):
    r"""The message to create a DnsThreatDetector.

    Attributes:
        parent (str):
            Required. The value for the parent of the
            DnsThreatDetector resource.
        dns_threat_detector_id (str):
            Optional. The ID of the requesting
            DnsThreatDetector object. If this field is not
            supplied, the service generates an identifier.
        dns_threat_detector (google.cloud.network_security_v1beta1.types.DnsThreatDetector):
            Required. The ``DnsThreatDetector`` resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dns_threat_detector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dns_threat_detector: "DnsThreatDetector" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DnsThreatDetector",
    )


class UpdateDnsThreatDetectorRequest(proto.Message):
    r"""The message for updating a DnsThreatDetector.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The field mask is used to specify the fields to be
            overwritten in the DnsThreatDetector resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the mask is not provided then all
            fields present in the request will be overwritten.
        dns_threat_detector (google.cloud.network_security_v1beta1.types.DnsThreatDetector):
            Required. The DnsThreatDetector resource
            being updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    dns_threat_detector: "DnsThreatDetector" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DnsThreatDetector",
    )


class DeleteDnsThreatDetectorRequest(proto.Message):
    r"""The message for deleting a DnsThreatDetector.

    Attributes:
        name (str):
            Required. Name of the DnsThreatDetector
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
