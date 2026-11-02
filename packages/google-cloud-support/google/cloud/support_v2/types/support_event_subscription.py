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

__protobuf__ = proto.module(
    package="google.cloud.support.v2",
    manifest={
        "SupportEventSubscription",
    },
)


class SupportEventSubscription(proto.Message):
    r"""A support event subscription.

    You can also manage support event subscriptions using other tools:

    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
      (or
      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
      for beta)
    - `Terraform
      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
      (or `google-beta
      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
      for beta)

    Attributes:
        name (str):
            Identifier. The resource name of the support
            event subscription.
        pub_sub_topic (str):
            Required. The name of the Pub/Sub topic to
            publish notifications to. Format:
            projects/{project}/topics/{topic}
        state (google.cloud.support_v2.types.SupportEventSubscription.State):
            Output only. The state of the subscription.
        failure_reason (google.cloud.support_v2.types.SupportEventSubscription.FailureReason):
            Output only. Reason why subscription is
            failing. State of subscription must be FAILING
            in order for this to have a value.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            subscription was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            subscription was last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            subscription was deleted.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            subscription will be purged.
    """

    class State(proto.Enum):
        r"""The state of the subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            WORKING (1):
                Subscription is active and working.
            FAILING (2):
                Subscription is failing. Notifications cannot
                be published for some reason.
            DELETED (3):
                Subscription has been deleted and is pending purge.
                Notifications are not sent for deleted subscriptions.
                Deleted subscriptions are purged after their ``purge_time``
                has passed.
        """

        STATE_UNSPECIFIED = 0
        WORKING = 1
        FAILING = 2
        DELETED = 3

    class FailureReason(proto.Enum):
        r"""The reason why the subscription is failing.

        Values:
            FAILURE_REASON_UNSPECIFIED (0):
                Unspecified failure reason.
            PERMISSION_DENIED (1):
                The service account (i.e.
                cloud-support-apievents@system.gserviceaccount.com)
                lacks the permission to publish to the
                customer's Pub/Sub topic.
            TOPIC_NOT_FOUND (2):
                The specified Pub/Sub topic does not exist.
            OTHER (3):
                Message failed to publish due to a
                system-side error.
        """

        FAILURE_REASON_UNSPECIFIED = 0
        PERMISSION_DENIED = 1
        TOPIC_NOT_FOUND = 2
        OTHER = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pub_sub_topic: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    failure_reason: FailureReason = proto.Field(
        proto.ENUM,
        number=4,
        enum=FailureReason,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
