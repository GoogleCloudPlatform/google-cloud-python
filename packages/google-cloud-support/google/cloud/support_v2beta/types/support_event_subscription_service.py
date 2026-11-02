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
import proto  # type: ignore

from google.cloud.support_v2beta.types import (
    support_event_subscription as gcs_support_event_subscription,
)

__protobuf__ = proto.module(
    package="google.cloud.support.v2beta",
    manifest={
        "CreateSupportEventSubscriptionRequest",
        "GetSupportEventSubscriptionRequest",
        "ListSupportEventSubscriptionsRequest",
        "ListSupportEventSubscriptionsResponse",
        "UpdateSupportEventSubscriptionRequest",
        "DeleteSupportEventSubscriptionRequest",
        "UndeleteSupportEventSubscriptionRequest",
        "ExpungeSupportEventSubscriptionRequest",
    },
)


class CreateSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for CreateSupportEventSubscription.

    Attributes:
        parent (str):
            Required. The parent resource name where the support event
            subscription will be created. Format:
            organizations/{organization_id}
        support_event_subscription (google.cloud.support_v2beta.types.SupportEventSubscription):
            Required. The Pub/Sub configuration to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    support_event_subscription: gcs_support_event_subscription.SupportEventSubscription = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_support_event_subscription.SupportEventSubscription,
    )


class GetSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for GetSupportEventSubscription.

    Attributes:
        name (str):
            Required. The name of the support event subscription to
            retrieve. Format:
            organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSupportEventSubscriptionsRequest(proto.Message):
    r"""Request message for ListSupportEventSubscriptions.

    Attributes:
        parent (str):
            Required. The fully qualified name of the Cloud resource to
            list support event subscriptions under. Format:
            organizations/{organization_id}
        filter (str):
            Optional. Filter expression based on AIP-160. Supported
            fields:

            - pub_sub_topic
            - state

            Examples:

            - ``pub_sub_topic="projects/example-project/topics/example-topic"``
            - ``state=WORKING``
            - ``pub_sub_topic="projects/example-project/topics/example-topic" AND state=WORKING``
        show_deleted (bool):
            Optional. Whether to show deleted
            subscriptions. By default, deleted subscriptions
            are not returned.
        page_size (int):
            Optional. The maximum number of support event
            subscriptions to return.
        page_token (str):
            Optional. A token identifying the page of results to return.
            If unspecified, the first page is retrieved.

            When paginating, all other parameters provided to
            ``ListSupportEventSubscriptions`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSupportEventSubscriptionsResponse(proto.Message):
    r"""Response message for ListSupportEventSubscriptions.

    Attributes:
        support_event_subscriptions (MutableSequence[google.cloud.support_v2beta.types.SupportEventSubscription]):
            The support event subscriptions.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    support_event_subscriptions: MutableSequence[
        gcs_support_event_subscription.SupportEventSubscription
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_support_event_subscription.SupportEventSubscription,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for UpdateSupportEventSubscription.

    Attributes:
        support_event_subscription (google.cloud.support_v2beta.types.SupportEventSubscription):
            Required. The support event subscription to update. The
            ``name`` field is used to identify the configuration to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. The only supported
            value is pub_sub_topic.
    """

    support_event_subscription: gcs_support_event_subscription.SupportEventSubscription = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_support_event_subscription.SupportEventSubscription,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for DeleteSupportEventSubscription.

    Attributes:
        name (str):
            Required. The name of the support event subscription to
            delete. Format:
            organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeleteSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for UndeleteSupportEventSubscription.

    Attributes:
        name (str):
            Required. The name of the support event subscription to
            undelete. Format:
            organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExpungeSupportEventSubscriptionRequest(proto.Message):
    r"""Request message for ExpungeSupportEventSubscription.

    Attributes:
        name (str):
            Required. The name of the support event subscription to
            expunge. Format:
            organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
