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

from google.cloud.network_security_v1alpha1.types import (
    security_profile_group_intercept,
    security_profile_group_mirroring,
    security_profile_group_threatprevention,
    security_profile_group_urlfiltering,
)

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "SecurityProfileGroup",
        "SecurityProfile",
    },
)


class SecurityProfileGroup(proto.Message):
    r"""SecurityProfileGroup is a resource that defines the behavior
    for various ProfileTypes.

    Attributes:
        name (str):
            Immutable. Identifier. Name of the SecurityProfileGroup
            resource. It matches pattern
            ``projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}``.
        description (str):
            Optional. An optional description of the
            profile group. Max length 2048 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Resource creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last resource update timestamp.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        data_path_id (int):
            Output only. Identifier used by the
            data-path. Unique within {container, location}.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        threat_prevention_profile (str):
            Optional. Reference to a SecurityProfile with
            the ThreatPrevention configuration.
        custom_mirroring_profile (str):
            Optional. Reference to a SecurityProfile with
            the CustomMirroring configuration.
        custom_intercept_profile (str):
            Optional. Reference to a SecurityProfile with
            the CustomIntercept configuration.
        url_filtering_profile (str):
            Optional. Reference to a SecurityProfile with
            the UrlFiltering configuration.
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
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    data_path_id: int = proto.Field(
        proto.UINT64,
        number=12,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    threat_prevention_profile: str = proto.Field(
        proto.STRING,
        number=6,
    )
    custom_mirroring_profile: str = proto.Field(
        proto.STRING,
        number=8,
    )
    custom_intercept_profile: str = proto.Field(
        proto.STRING,
        number=9,
    )
    url_filtering_profile: str = proto.Field(
        proto.STRING,
        number=11,
    )


class SecurityProfile(proto.Message):
    r"""SecurityProfile is a resource that defines the behavior for
    one of many ProfileTypes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        threat_prevention_profile (google.cloud.network_security_v1alpha1.types.ThreatPreventionProfile):
            The threat prevention configuration for the
            SecurityProfile.

            This field is a member of `oneof`_ ``profile``.
        custom_mirroring_profile (google.cloud.network_security_v1alpha1.types.CustomMirroringProfile):
            The custom Packet Mirroring v2 configuration
            for the SecurityProfile.

            This field is a member of `oneof`_ ``profile``.
        custom_intercept_profile (google.cloud.network_security_v1alpha1.types.CustomInterceptProfile):
            The custom TPPI configuration for the
            SecurityProfile.

            This field is a member of `oneof`_ ``profile``.
        url_filtering_profile (google.cloud.network_security_v1alpha1.types.UrlFilteringProfile):
            The URL filtering configuration for the
            SecurityProfile.

            This field is a member of `oneof`_ ``profile``.
        name (str):
            Immutable. Identifier. Name of the SecurityProfile resource.
            It matches pattern
            ``projects|organizations/*/locations/{location}/securityProfiles/{security_profile}``.
        description (str):
            Optional. An optional description of the
            profile. Max length 512 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Resource creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last resource update timestamp.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        type_ (google.cloud.network_security_v1alpha1.types.SecurityProfile.ProfileType):
            Immutable. The single ProfileType that the
            SecurityProfile resource configures.
    """

    class ProfileType(proto.Enum):
        r"""The possible types that the SecurityProfile resource can
        configure.

        Values:
            PROFILE_TYPE_UNSPECIFIED (0):
                Profile type not specified.
            THREAT_PREVENTION (1):
                Profile type for threat prevention.
            CUSTOM_MIRRORING (2):
                Profile type for packet mirroring v2
            CUSTOM_INTERCEPT (3):
                Profile type for TPPI.
            URL_FILTERING (5):
                Profile type for URL filtering.
        """

        PROFILE_TYPE_UNSPECIFIED = 0
        THREAT_PREVENTION = 1
        CUSTOM_MIRRORING = 2
        CUSTOM_INTERCEPT = 3
        URL_FILTERING = 5

    threat_prevention_profile: security_profile_group_threatprevention.ThreatPreventionProfile = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="profile",
        message=security_profile_group_threatprevention.ThreatPreventionProfile,
    )
    custom_mirroring_profile: security_profile_group_mirroring.CustomMirroringProfile = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="profile",
        message=security_profile_group_mirroring.CustomMirroringProfile,
    )
    custom_intercept_profile: security_profile_group_intercept.CustomInterceptProfile = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="profile",
        message=security_profile_group_intercept.CustomInterceptProfile,
    )
    url_filtering_profile: security_profile_group_urlfiltering.UrlFilteringProfile = (
        proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="profile",
            message=security_profile_group_urlfiltering.UrlFilteringProfile,
        )
    )
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
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    type_: ProfileType = proto.Field(
        proto.ENUM,
        number=6,
        enum=ProfileType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
