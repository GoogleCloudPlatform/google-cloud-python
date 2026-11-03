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

from google.cloud.apphub_v1.types import attributes as gca_attributes
from google.cloud.apphub_v1.types import properties

__protobuf__ = proto.module(
    package="google.cloud.apphub.v1",
    manifest={
        "Workload",
        "WorkloadReference",
        "WorkloadProperties",
        "DiscoveredWorkload",
    },
)


class Workload(proto.Message):
    r"""Workload is an App Hub data model that contains a discovered
    workload, which represents a binary deployment (such as managed
    instance groups (MIGs) and GKE deployments) that performs the
    smallest logical subset of business functionality.

    Attributes:
        name (str):
            Identifier. The resource name of the Workload. Format:
            ``"projects/{host-project-id}/locations/{location}/applications/{application-id}/workloads/{workload-id}"``
        display_name (str):
            Optional. User-defined name for the Workload.
            Can have a maximum length of 63 characters.
        description (str):
            Optional. User-defined description of a
            Workload. Can have a maximum length of 2048
            characters.
        workload_reference (google.cloud.apphub_v1.types.WorkloadReference):
            Output only. Reference of an underlying
            compute resource represented by the Workload.
            These are immutable.
        workload_properties (google.cloud.apphub_v1.types.WorkloadProperties):
            Output only. Properties of an underlying
            compute resource represented by the Workload.
            These are immutable.
        discovered_workload (str):
            Required. Immutable. The resource name of the
            original discovered workload.
        attributes (google.cloud.apphub_v1.types.Attributes):
            Optional. Consumer provided attributes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        uid (str):
            Output only. A universally unique identifier (UUID) for the
            ``Workload`` in the UUID4 format.
        state (google.cloud.apphub_v1.types.Workload.State):
            Output only. Workload state.
    """

    class State(proto.Enum):
        r"""Workload state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The Workload is being created.
            ACTIVE (2):
                The Workload is ready.
            DELETING (3):
                The Workload is being deleted.
            DETACHED (4):
                The underlying compute resources have been
                deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        DETACHED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    workload_reference: "WorkloadReference" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="WorkloadReference",
    )
    workload_properties: "WorkloadProperties" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="WorkloadProperties",
    )
    discovered_workload: str = proto.Field(
        proto.STRING,
        number=6,
    )
    attributes: gca_attributes.Attributes = proto.Field(
        proto.MESSAGE,
        number=7,
        message=gca_attributes.Attributes,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )


class WorkloadReference(proto.Message):
    r"""Reference of an underlying compute resource represented by
    the Workload.

    Attributes:
        uri (str):
            Output only. The underlying compute resource
            uri.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WorkloadProperties(proto.Message):
    r"""Properties of an underlying compute resource represented by
    the Workload.

    Attributes:
        gcp_project (str):
            Output only. The service project identifier
            that the underlying cloud resource resides in.
            Empty for non-cloud resources.
        location (str):
            Output only. The location that the underlying
            compute resource resides in (for example,
            us-west1).
        zone (str):
            Output only. The location that the underlying
            compute resource resides in if it is zonal (for
            example, us-west1-a).
        functional_type (google.cloud.apphub_v1.types.FunctionalType):
            Output only. The type of the workload.
        extended_metadata (MutableMapping[str, google.cloud.apphub_v1.types.ExtendedMetadata]):
            Output only. Additional metadata specific to the resource
            type. The key is a string that identifies the type of
            metadata and the value is the metadata contents specific to
            that type. Key format:
            ``apphub.googleapis.com/{metadataType}``
        identity (google.cloud.apphub_v1.types.Identity):
            Output only. The identity associated with the
            workload.
    """

    gcp_project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    functional_type: properties.FunctionalType = proto.Field(
        proto.MESSAGE,
        number=4,
        message=properties.FunctionalType,
    )
    extended_metadata: MutableMapping[str, properties.ExtendedMetadata] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=5,
            message=properties.ExtendedMetadata,
        )
    )
    identity: properties.Identity = proto.Field(
        proto.MESSAGE,
        number=6,
        message=properties.Identity,
    )


class DiscoveredWorkload(proto.Message):
    r"""DiscoveredWorkload is a binary deployment (such as managed
    instance groups (MIGs) and GKE deployments) that performs the
    smallest logical subset of business functionality. A discovered
    workload can be registered to an App Hub Workload.

    Attributes:
        name (str):
            Identifier. The resource name of the discovered workload.
            Format:
            ``"projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}"``
        workload_reference (google.cloud.apphub_v1.types.WorkloadReference):
            Output only. Reference of an underlying
            compute resource represented by the Workload.
            These are immutable.
        workload_properties (google.cloud.apphub_v1.types.WorkloadProperties):
            Output only. Properties of an underlying
            compute resource represented by the Workload.
            These are immutable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_reference: "WorkloadReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="WorkloadReference",
    )
    workload_properties: "WorkloadProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="WorkloadProperties",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
