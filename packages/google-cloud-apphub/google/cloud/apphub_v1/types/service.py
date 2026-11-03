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
        "Service",
        "ServiceReference",
        "ServiceProperties",
        "DiscoveredService",
    },
)


class Service(proto.Message):
    r"""Service is an App Hub data model that contains a discovered
    service, which represents a network or API interface that
    exposes some functionality to clients for consumption over the
    network.

    Attributes:
        name (str):
            Identifier. The resource name of a Service. Format:
            ``"projects/{host-project-id}/locations/{location}/applications/{application-id}/services/{service-id}"``
        display_name (str):
            Optional. User-defined name for the Service.
            Can have a maximum length of 63 characters.
        description (str):
            Optional. User-defined description of a
            Service. Can have a maximum length of 2048
            characters.
        service_reference (google.cloud.apphub_v1.types.ServiceReference):
            Output only. Reference to an underlying
            networking resource that can comprise a Service.
            These are immutable.
        service_properties (google.cloud.apphub_v1.types.ServiceProperties):
            Output only. Properties of an underlying
            compute resource that can comprise a Service.
            These are immutable.
        attributes (google.cloud.apphub_v1.types.Attributes):
            Optional. Consumer provided attributes.
        discovered_service (str):
            Required. Immutable. The resource name of the
            original discovered service.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        uid (str):
            Output only. A universally unique identifier (UUID) for the
            ``Service`` in the UUID4 format.
        state (google.cloud.apphub_v1.types.Service.State):
            Output only. Service state.
    """

    class State(proto.Enum):
        r"""Service state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The service is being created.
            ACTIVE (2):
                The service is ready.
            DELETING (3):
                The service is being deleted.
            DETACHED (4):
                The underlying networking resources have been
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
    service_reference: "ServiceReference" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ServiceReference",
    )
    service_properties: "ServiceProperties" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ServiceProperties",
    )
    attributes: gca_attributes.Attributes = proto.Field(
        proto.MESSAGE,
        number=6,
        message=gca_attributes.Attributes,
    )
    discovered_service: str = proto.Field(
        proto.STRING,
        number=7,
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


class ServiceReference(proto.Message):
    r"""Reference to an underlying networking resource that can
    comprise a Service.

    Attributes:
        uri (str):
            Output only. The underlying resource URI. For
            example, URI of Forwarding Rule, URL Map, and
            Backend Service.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ServiceProperties(proto.Message):
    r"""Properties of an underlying cloud resource that can comprise
    a Service.

    Attributes:
        gcp_project (str):
            Output only. The service project identifier
            that the underlying cloud resource resides in.
        location (str):
            Output only. The location that the underlying
            resource resides in, for example, us-west1.
        zone (str):
            Output only. The location that the underlying
            resource resides in if it is zonal, for example,
            us-west1-a).
        functional_type (google.cloud.apphub_v1.types.FunctionalType):
            Output only. The type of the service.
        registration_type (google.cloud.apphub_v1.types.RegistrationType):
            Output only. The registration type of the
            service.
        extended_metadata (MutableMapping[str, google.cloud.apphub_v1.types.ExtendedMetadata]):
            Output only. Additional metadata specific to the resource
            type. The key is a string that identifies the type of
            metadata and the value is the metadata contents specific to
            that type. Key format:
            ``apphub.googleapis.com/{metadataType}``
        identity (google.cloud.apphub_v1.types.Identity):
            Output only. The identity associated with the
            service.
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
    registration_type: properties.RegistrationType = proto.Field(
        proto.MESSAGE,
        number=5,
        message=properties.RegistrationType,
    )
    extended_metadata: MutableMapping[str, properties.ExtendedMetadata] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=6,
            message=properties.ExtendedMetadata,
        )
    )
    identity: properties.Identity = proto.Field(
        proto.MESSAGE,
        number=7,
        message=properties.Identity,
    )


class DiscoveredService(proto.Message):
    r"""DiscoveredService is a network or API interface that exposes
    some functionality to clients for consumption over the network.
    A discovered service can be registered to a App Hub service.

    Attributes:
        name (str):
            Identifier. The resource name of the discovered service.
            Format:
            ``"projects/{host-project-id}/locations/{location}/discoveredServices/{uuid}"``
        service_reference (google.cloud.apphub_v1.types.ServiceReference):
            Output only. Reference to an underlying
            networking resource that can comprise a Service.
            These are immutable.
        service_properties (google.cloud.apphub_v1.types.ServiceProperties):
            Output only. Properties of an underlying
            compute resource that can comprise a Service.
            These are immutable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_reference: "ServiceReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServiceReference",
    )
    service_properties: "ServiceProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServiceProperties",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
