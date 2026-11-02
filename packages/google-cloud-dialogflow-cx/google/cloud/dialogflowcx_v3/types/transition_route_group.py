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

from google.cloud.dialogflowcx_v3.types import page

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "TransitionRouteGroup",
        "ListTransitionRouteGroupsRequest",
        "ListTransitionRouteGroupsResponse",
        "GetTransitionRouteGroupRequest",
        "CreateTransitionRouteGroupRequest",
        "UpdateTransitionRouteGroupRequest",
        "DeleteTransitionRouteGroupRequest",
    },
)


class TransitionRouteGroup(proto.Message):
    r"""A TransitionRouteGroup represents a group of
    [``TransitionRoutes``][google.cloud.dialogflow.cx.v3.TransitionRoute]
    to be used by a [Page][google.cloud.dialogflow.cx.v3.Page].

    Attributes:
        name (str):
            The unique identifier of the transition route group.
            [TransitionRouteGroups.CreateTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup]
            populates the name automatically. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>``
            .
        display_name (str):
            Required. The human-readable name of the
            transition route group, unique within the flow.
            The display name can be no longer than 30
            characters.
        transition_routes (MutableSequence[google.cloud.dialogflowcx_v3.types.TransitionRoute]):
            Transition routes associated with the
            [TransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroup].
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transition_routes: MutableSequence[page.TransitionRoute] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=page.TransitionRoute,
    )


class ListTransitionRouteGroupsRequest(proto.Message):
    r"""The request message for
    [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups].

    Attributes:
        parent (str):
            Required. The flow to list all transition route groups for.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``
            or \`projects//locations//agents/.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        language_code (str):
            The language to list transition route groups for. The
            following fields are language dependent:

            - ``TransitionRouteGroup.transition_routes.trigger_fulfillment.messages``
            -

            ``TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListTransitionRouteGroupsResponse(proto.Message):
    r"""The response message for
    [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups].

    Attributes:
        transition_route_groups (MutableSequence[google.cloud.dialogflowcx_v3.types.TransitionRouteGroup]):
            The list of transition route groups. There will be a maximum
            number of items returned based on the page_size field in the
            request. The list may in some cases be empty or contain
            fewer entries than page_size even if this isn't the last
            page.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    transition_route_groups: MutableSequence["TransitionRouteGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TransitionRouteGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTransitionRouteGroupRequest(proto.Message):
    r"""The request message for
    [TransitionRouteGroups.GetTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.GetTransitionRouteGroup].

    Attributes:
        name (str):
            Required. The name of the
            [TransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroup].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>``.
        language_code (str):
            The language to retrieve the transition route group for. The
            following fields are language dependent:

            - ``TransitionRouteGroup.transition_routes.trigger_fulfillment.messages``
            -

            ``TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateTransitionRouteGroupRequest(proto.Message):
    r"""The request message for
    [TransitionRouteGroups.CreateTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup].

    Attributes:
        parent (str):
            Required. The flow to create an
            [TransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroup]
            for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``
            for agent-level groups.
        transition_route_group (google.cloud.dialogflowcx_v3.types.TransitionRouteGroup):
            Required. The transition route group to
            create.
        language_code (str):
            The language of the following fields in
            ``TransitionRouteGroup``:

            - ``TransitionRouteGroup.transition_routes.trigger_fulfillment.messages``
            -

            ``TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    transition_route_group: "TransitionRouteGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TransitionRouteGroup",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateTransitionRouteGroupRequest(proto.Message):
    r"""The request message for
    [TransitionRouteGroups.UpdateTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.UpdateTransitionRouteGroup].

    Attributes:
        transition_route_group (google.cloud.dialogflowcx_v3.types.TransitionRouteGroup):
            Required. The transition route group to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
        language_code (str):
            The language of the following fields in
            ``TransitionRouteGroup``:

            - ``TransitionRouteGroup.transition_routes.trigger_fulfillment.messages``
            -

            ``TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    transition_route_group: "TransitionRouteGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TransitionRouteGroup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTransitionRouteGroupRequest(proto.Message):
    r"""The request message for
    [TransitionRouteGroups.DeleteTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.DeleteTransitionRouteGroup].

    Attributes:
        name (str):
            Required. The name of the
            [TransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroup]
            to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>``.
        force (bool):
            This field has no effect for transition route group that no
            page is using. If the transition route group is referenced
            by any page:

            - If ``force`` is set to false, an error will be returned
              with message indicating pages that reference the
              transition route group.
            - If ``force`` is set to true, Dialogflow will remove the
              transition route group, as well as any reference to it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
