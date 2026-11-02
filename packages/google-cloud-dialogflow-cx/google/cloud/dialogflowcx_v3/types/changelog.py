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
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "ListChangelogsRequest",
        "ListChangelogsResponse",
        "GetChangelogRequest",
        "Changelog",
    },
)


class ListChangelogsRequest(proto.Message):
    r"""The request message for
    [Changelogs.ListChangelogs][google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs].

    Attributes:
        parent (str):
            Required. The agent containing the changelogs. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        filter (str):
            The filter string. Supports filter by user_email, resource,
            type and create_time. Some examples:

            1. By user email: user_email = "someone@google.com"
            2. By resource name: resource =
               "projects/123/locations/global/agents/456/flows/789"
            3. By resource display name: display_name = "my agent"
            4. By action: action = "Create"
            5. By type: type = "flows"
            6. By create time. Currently predicates on ``create_time``
               and ``create_time_epoch_seconds`` are supported:
               create_time_epoch_seconds > 1551790877 AND create_time <=
               2017-01-15T01:30:15.01Z
            7. Combination of above filters: resource =
               "projects/123/locations/global/agents/456/flows/789" AND
               user_email = "someone@google.com" AND create_time <=
               2017-01-15T01:30:15.01Z
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListChangelogsResponse(proto.Message):
    r"""The response message for
    [Changelogs.ListChangelogs][google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs].

    Attributes:
        changelogs (MutableSequence[google.cloud.dialogflowcx_v3.types.Changelog]):
            The list of changelogs. There will be a maximum number of
            items returned based on the page_size field in the request.
            The changelogs will be ordered by timestamp.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    changelogs: MutableSequence["Changelog"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Changelog",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetChangelogRequest(proto.Message):
    r"""The request message for
    [Changelogs.GetChangelog][google.cloud.dialogflow.cx.v3.Changelogs.GetChangelog].

    Attributes:
        name (str):
            Required. The name of the changelog to get. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Changelog(proto.Message):
    r"""Changelogs represents a change made to a given agent.

    Attributes:
        name (str):
            The unique identifier of the changelog. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>``.
        user_email (str):
            Email address of the authenticated user.
        display_name (str):
            The affected resource display name of the
            change.
        action (str):
            The action of the change.
        type_ (str):
            The affected resource type.
        resource (str):
            The affected resource name of the change.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp of the change.
        language_code (str):
            The affected language code of the change.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    action: str = proto.Field(
        proto.STRING,
        number=11,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=8,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=14,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
