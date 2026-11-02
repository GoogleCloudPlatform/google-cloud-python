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

import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.eventarc.v1',
    manifest={
        'Provider',
        'EventType',
        'FilteringAttribute',
    },
)


class Provider(proto.Message):
    r"""A representation of the Provider resource.

    Attributes:
        name (str):
            Output only. In
            ``projects/{project}/locations/{location}/providers/{provider_id}``
            format.
        display_name (str):
            Output only. Human friendly name for the
            Provider. For example "Cloud Storage".
        event_types (MutableSequence[google.cloud.eventarc_v1.types.EventType]):
            Output only. Event types for this provider.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_types: MutableSequence['EventType'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='EventType',
    )


class EventType(proto.Message):
    r"""A representation of the event type resource.

    Attributes:
        type_ (str):
            Output only. The full name of the event type
            (for example,
            "google.cloud.storage.object.v1.finalized"). In
            the form of
            {provider-specific-prefix}.{resource}.{version}.{verb}.
            Types MUST be versioned and event schemas are
            guaranteed to remain backward compatible within
            one version. Note that event type versions and
            API versions do not need to match.
        description (str):
            Output only. Human friendly description of
            what the event type is about. For example
            "Bucket created in Cloud Storage".
        filtering_attributes (MutableSequence[google.cloud.eventarc_v1.types.FilteringAttribute]):
            Output only. Filtering attributes for the
            event type.
        event_schema_uri (str):
            Output only. URI for the event schema.
            For example
            "https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/storage/v1/events.proto".
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filtering_attributes: MutableSequence['FilteringAttribute'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='FilteringAttribute',
    )
    event_schema_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FilteringAttribute(proto.Message):
    r"""A representation of the FilteringAttribute resource.
    Filtering attributes are per event type.

    Attributes:
        attribute (str):
            Output only. Attribute used for filtering the
            event type.
        description (str):
            Output only. Description of the purpose of
            the attribute.
        required (bool):
            Output only. If true, the triggers for this
            provider should always specify a filter on these
            attributes. Trigger creation will fail
            otherwise.
        path_pattern_supported (bool):
            Output only. If true, the attribute accepts
            matching expressions in the Eventarc PathPattern
            format.
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    path_pattern_supported: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
