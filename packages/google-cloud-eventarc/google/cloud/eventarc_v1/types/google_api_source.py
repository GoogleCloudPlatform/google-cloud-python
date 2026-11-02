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

from google.cloud.eventarc_v1.types import logging_config as gce_logging_config

__protobuf__ = proto.module(
    package="google.cloud.eventarc.v1",
    manifest={
        "GoogleApiSource",
    },
)


class GoogleApiSource(proto.Message):
    r"""A GoogleApiSource represents a subscription of 1P events from
    a MessageBus.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/googleApiSources/{google_api_source}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        destination (str):
            Required. Destination is the message bus that the
            GoogleApiSource is delivering to. It must be point to the
            full resource name of a MessageBus. Format:
            "projects/{PROJECT_ID}/locations/{region}/messagesBuses/{MESSAGE_BUS_ID)
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        logging_config (google.cloud.eventarc_v1.types.LoggingConfig):
            Optional. Config to control Platform logging
            for the GoogleApiSource.
        organization_subscription (google.cloud.eventarc_v1.types.GoogleApiSource.OrganizationSubscription):
            Optional. Config to enable subscribing to
            events from all projects in the
            GoogleApiSource's org.

            This field is a member of `oneof`_ ``wide_scope_subscription``.
        project_subscriptions (google.cloud.eventarc_v1.types.GoogleApiSource.ProjectSubscriptions):
            Optional. Config to enable subscribing to all
            events from a list of projects.

            All the projects must be in the same org as the
            GoogleApiSource.

            This field is a member of `oneof`_ ``wide_scope_subscription``.
    """

    class ProjectSubscriptions(proto.Message):
        r"""Config to enable subscribing to all events from a list of
        projects.

        Attributes:
            list_ (MutableSequence[str]):
                Required. A list of projects to receive
                events from.
                All the projects must be in the same org. The
                listed projects should have the format
                project/{identifier} where identifier can be
                either the project id for project number. A
                single list may contain both formats. At most
                100 projects can be listed.
        """

        list_: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class OrganizationSubscription(proto.Message):
        r"""Config to enabled subscribing to events from other projects
        in the org.

        Attributes:
            enabled (bool):
                Required. Enable org level subscription.
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=9,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    logging_config: gce_logging_config.LoggingConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=gce_logging_config.LoggingConfig,
    )
    organization_subscription: OrganizationSubscription = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="wide_scope_subscription",
        message=OrganizationSubscription,
    )
    project_subscriptions: ProjectSubscriptions = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="wide_scope_subscription",
        message=ProjectSubscriptions,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
