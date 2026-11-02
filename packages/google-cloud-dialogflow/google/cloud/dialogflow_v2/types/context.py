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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "Context",
        "ListContextsRequest",
        "ListContextsResponse",
        "GetContextRequest",
        "CreateContextRequest",
        "UpdateContextRequest",
        "DeleteContextRequest",
        "DeleteAllContextsRequest",
    },
)


class Context(proto.Message):
    r"""Dialogflow contexts are similar to natural language context. If a
    person says to you "they are orange", you need context in order to
    understand what "they" is referring to. Similarly, for Dialogflow to
    handle an end-user expression like that, it needs to be provided
    with context in order to correctly match an intent.

    Using contexts, you can control the flow of a conversation. You can
    configure contexts for an intent by setting input and output
    contexts, which are identified by string names. When an intent is
    matched, any configured output contexts for that intent become
    active. While any contexts are active, Dialogflow is more likely to
    match intents that are configured with input contexts that
    correspond to the currently active contexts.

    For more information about context, see the `Contexts
    guide <https://cloud.google.com/dialogflow/docs/contexts-overview>`__.

    Attributes:
        name (str):
            Required. The unique identifier of the context. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>``,
            or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context ID>``.

            The ``Context ID`` is always converted to lowercase, may
            only contain characters in ``a-zA-Z0-9_-%`` and may be at
            most 250 bytes long.

            If ``Environment ID`` is not specified, we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.

            The following context names are reserved for internal use by
            Dialogflow. You should not use these contexts or create
            contexts with these names:

            - ``__system_counters__``
            - ``*_id_dialog_context``
            - ``*_dialog_params_size``
        lifespan_count (int):
            Optional. The number of conversational query requests after
            which the context expires. The default is ``0``. If set to
            ``0``, the context expires immediately. Contexts expire
            automatically after 20 minutes if there are no matching
            queries.
        parameters (google.protobuf.struct_pb2.Struct):
            Optional. The collection of parameters associated with this
            context.

            Depending on your protocol or client library language, this
            is a map, associative array, symbol table, dictionary, or
            JSON object composed of a collection of (MapKey, MapValue)
            pairs:

            - MapKey type: string
            - MapKey value: parameter name
            - MapValue type: If parameter's entity type is a composite
              entity then use map, otherwise, depending on the parameter
              value type, it could be one of string, number, boolean,
              null, list or map.
            - MapValue value: If parameter's entity type is a composite
              entity then use map from composite entity property names
              to property values, otherwise, use parameter value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lifespan_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class ListContextsRequest(proto.Message):
    r"""The request message for
    [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].

    Attributes:
        parent (str):
            Required. The session to list all contexts from. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>`` or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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


class ListContextsResponse(proto.Message):
    r"""The response message for
    [Contexts.ListContexts][google.cloud.dialogflow.v2.Contexts.ListContexts].

    Attributes:
        contexts (MutableSequence[google.cloud.dialogflow_v2.types.Context]):
            The list of contexts. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    contexts: MutableSequence["Context"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Context",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetContextRequest(proto.Message):
    r"""The request message for
    [Contexts.GetContext][google.cloud.dialogflow.v2.Contexts.GetContext].

    Attributes:
        name (str):
            Required. The name of the context. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>``
            or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context ID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateContextRequest(proto.Message):
    r"""The request message for
    [Contexts.CreateContext][google.cloud.dialogflow.v2.Contexts.CreateContext].

    Attributes:
        parent (str):
            Required. The session to create a context for. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>`` or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.
        context (google.cloud.dialogflow_v2.types.Context):
            Required. The context to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context: "Context" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Context",
    )


class UpdateContextRequest(proto.Message):
    r"""The request message for
    [Contexts.UpdateContext][google.cloud.dialogflow.v2.Contexts.UpdateContext].

    Attributes:
        context (google.cloud.dialogflow_v2.types.Context):
            Required. The context to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
    """

    context: "Context" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Context",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteContextRequest(proto.Message):
    r"""The request message for
    [Contexts.DeleteContext][google.cloud.dialogflow.v2.Contexts.DeleteContext].

    Attributes:
        name (str):
            Required. The name of the context to delete. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>/contexts/<Context ID>``
            or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/contexts/<Context ID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAllContextsRequest(proto.Message):
    r"""The request message for
    [Contexts.DeleteAllContexts][google.cloud.dialogflow.v2.Contexts.DeleteAllContexts].

    Attributes:
        parent (str):
            Required. The name of the session to delete all contexts
            from. Format:
            ``projects/<Project ID>/agent/sessions/<Session ID>`` or
            ``projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>``.
            If ``Environment ID`` is not specified we assume default
            'draft' environment. If ``User ID`` is not specified, we
            assume default '-' user.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
