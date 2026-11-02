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

from google.cloud.retail_v2alpha.types import user_event as gcr_user_event

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "WriteUserEventRequest",
        "CollectUserEventRequest",
        "RejoinUserEventsRequest",
        "RejoinUserEventsResponse",
        "RejoinUserEventsMetadata",
    },
)


class WriteUserEventRequest(proto.Message):
    r"""Request message for WriteUserEvent method.

    Attributes:
        parent (str):
            Required. The parent catalog resource name, such as
            ``projects/1234/locations/global/catalogs/default_catalog``.
        user_event (google.cloud.retail_v2alpha.types.UserEvent):
            Required. User event to write.
        write_async (bool):
            If set to true, the user event will be
            written asynchronously after validation, and the
            API will respond without waiting for the write.
            Therefore, silent failures can occur even if the
            API returns success. In case of silent failures,
            error messages can be found in Stackdriver logs.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_event: gcr_user_event.UserEvent = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_user_event.UserEvent,
    )
    write_async: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CollectUserEventRequest(proto.Message):
    r"""Request message for CollectUserEvent method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        prebuilt_rule (str):
            The prebuilt rule name that can convert a specific type of
            raw_json. For example: "ga4_bq" rule for the GA4 user event
            schema.

            This field is a member of `oneof`_ ``conversion_rule``.
        parent (str):
            Required. The parent catalog name, such as
            ``projects/1234/locations/global/catalogs/default_catalog``.
        user_event (str):
            Required. URL encoded UserEvent proto with a
            length limit of 2,000,000 characters.
        uri (str):
            The URL including cgi-parameters but
            excluding the hash fragment with a length limit
            of 5,000 characters. This is often more useful
            than the referer URL, because many browsers only
            send the domain for 3rd party requests.
        ets (int):
            The event timestamp in milliseconds. This
            prevents browser caching of otherwise identical
            get requests. The name is abbreviated to reduce
            the payload bytes.
        raw_json (str):
            An arbitrary serialized JSON string that contains necessary
            information that can comprise a user event. When this field
            is specified, the user_event field will be ignored. Note:
            line-delimited JSON is not supported, a single JSON only.
    """

    prebuilt_rule: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="conversion_rule",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_event: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ets: int = proto.Field(
        proto.INT64,
        number=4,
    )
    raw_json: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RejoinUserEventsRequest(proto.Message):
    r"""Request message for RejoinUserEvents method.

    Attributes:
        parent (str):
            Required. The parent catalog resource name, such as
            ``projects/1234/locations/global/catalogs/default_catalog``.
        user_event_rejoin_scope (google.cloud.retail_v2alpha.types.RejoinUserEventsRequest.UserEventRejoinScope):
            The type of the user event rejoin to define the scope and
            range of the user events to be rejoined with the latest
            product catalog. Defaults to
            ``USER_EVENT_REJOIN_SCOPE_UNSPECIFIED`` if this field is not
            set, or set to an invalid integer value.
    """

    class UserEventRejoinScope(proto.Enum):
        r"""The scope of user events to be rejoined with the latest product
        catalog. If the rejoining aims at reducing number of unjoined
        events, set ``UserEventRejoinScope`` to ``UNJOINED_EVENTS``. If the
        rejoining aims at correcting product catalog information in joined
        events, set ``UserEventRejoinScope`` to ``JOINED_EVENTS``. If all
        events needs to be rejoined, set ``UserEventRejoinScope`` to
        ``USER_EVENT_REJOIN_SCOPE_UNSPECIFIED``.

        Values:
            USER_EVENT_REJOIN_SCOPE_UNSPECIFIED (0):
                Rejoin all events with the latest product
                catalog, including both joined events and
                unjoined events.
            JOINED_EVENTS (1):
                Only rejoin joined events with the latest
                product catalog.
            UNJOINED_EVENTS (2):
                Only rejoin unjoined events with the latest
                product catalog.
        """

        USER_EVENT_REJOIN_SCOPE_UNSPECIFIED = 0
        JOINED_EVENTS = 1
        UNJOINED_EVENTS = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_event_rejoin_scope: UserEventRejoinScope = proto.Field(
        proto.ENUM,
        number=2,
        enum=UserEventRejoinScope,
    )


class RejoinUserEventsResponse(proto.Message):
    r"""Response message for ``RejoinUserEvents`` method.

    Attributes:
        rejoined_user_events_count (int):
            Number of user events that were joined with
            latest product catalog.
    """

    rejoined_user_events_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class RejoinUserEventsMetadata(proto.Message):
    r"""Metadata for ``RejoinUserEvents`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
