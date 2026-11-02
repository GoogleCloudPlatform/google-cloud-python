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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.securitycenter_v1beta1.types import (
    security_marks as gcs_security_marks,
)

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1beta1",
    manifest={
        "Finding",
    },
)


class Finding(proto.Message):
    r"""Security Command Center finding.

    A finding is a record of assessment data (security, risk, health
    or privacy) ingested into Security Command Center for
    presentation, notification, analysis, policy testing, and
    enforcement. For example, an XSS vulnerability in an App Engine
    application is a finding.

    Attributes:
        name (str):
            The relative resource name of this finding. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}".
        parent (str):
            Immutable. The relative resource name of the source the
            finding belongs to. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            This field is immutable after creation time. For example:
            "organizations/{organization_id}/sources/{source_id}".
        resource_name (str):
            For findings on Google Cloud resources, the full resource
            name of the Google Cloud resource this finding is for. See:
            https://cloud.google.com/apis/design/resource_names#full_resource_name
            When the finding is for a non-Google Cloud resource, the
            resourceName can be a customer or partner defined string.
            This field is immutable after creation time.
        state (google.cloud.securitycenter_v1beta1.types.Finding.State):
            The state of the finding.
        category (str):
            The additional taxonomy group within findings from a given
            source. This field is immutable after creation time.
            Example: "XSS_FLASH_INJECTION".
        external_uri (str):
            The URI that, if available, points to a web
            page outside of Security Command Center where
            additional information about the finding can be
            found. This field is guaranteed to be either
            empty or a well formed URL.
        source_properties (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Source specific properties. These properties are managed by
            the source that writes the finding. The key names in the
            source_properties map must be between 1 and 255 characters,
            and must start with a letter and contain alphanumeric
            characters or underscores only.
        security_marks (google.cloud.securitycenter_v1beta1.types.SecurityMarks):
            Output only. User specified security marks.
            These marks are entirely managed by the user and
            come from the SecurityMarks resource that
            belongs to the finding.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the event took place, or
            when an update to the finding occurred. For
            example, if the finding represents an open
            firewall it would capture the time the detector
            believes the firewall became open. The accuracy
            is determined by the detector. If the finding
            were to be resolved afterward, this time would
            reflect when the finding was resolved.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the finding was created in
            Security Command Center.
    """

    class State(proto.Enum):
        r"""The state of the finding.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                The finding requires attention and has not
                been addressed yet.
            INACTIVE (2):
                The finding has been fixed, triaged as a
                non-issue or otherwise addressed and is no
                longer active.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    category: str = proto.Field(
        proto.STRING,
        number=5,
    )
    external_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_properties: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Value,
    )
    security_marks: gcs_security_marks.SecurityMarks = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcs_security_marks.SecurityMarks,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
