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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import trace

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "CreateExampleRequest",
        "DeleteExampleRequest",
        "ListExamplesRequest",
        "ListExamplesResponse",
        "GetExampleRequest",
        "UpdateExampleRequest",
        "Example",
    },
)


class CreateExampleRequest(proto.Message):
    r"""The request message for
    [Examples.CreateExample][google.cloud.dialogflow.cx.v3beta1.Examples.CreateExample].

    Attributes:
        parent (str):
            Required. The playbook to create an example for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        example (google.cloud.dialogflowcx_v3beta1.types.Example):
            Required. The example to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    example: "Example" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Example",
    )


class DeleteExampleRequest(proto.Message):
    r"""The request message for
    [Examples.DeleteExample][google.cloud.dialogflow.cx.v3beta1.Examples.DeleteExample].

    Attributes:
        name (str):
            Required. The name of the example to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/examples/<ExampleID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExamplesRequest(proto.Message):
    r"""The request message for
    [Examples.ListExamples][google.cloud.dialogflow.cx.v3beta1.Examples.ListExamples].

    Attributes:
        parent (str):
            Required. The playbook to list the examples from. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The
            [next_page_token][ListExampleResponse.next_page_token] value
            returned from a previous list request.
        language_code (str):
            Optional. The language to list examples for.
            If not specified, list all examples under the
            playbook. Note: languages must be enabled in the
            agent before they can be used.
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


class ListExamplesResponse(proto.Message):
    r"""The response message for
    [Examples.ListExamples][google.cloud.dialogflow.cx.v3beta1.Examples.ListExamples].

    Attributes:
        examples (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Example]):
            The list of examples. There will be a maximum number of
            items returned based on the
            [page_size][google.cloud.dialogflow.cx.v3beta1.ListExamplesRequest.page_size]
            field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    examples: MutableSequence["Example"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Example",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetExampleRequest(proto.Message):
    r"""The request message for
    [Examples.GetExample][google.cloud.dialogflow.cx.v3beta1.Examples.GetExample].

    Attributes:
        name (str):
            Required. The name of the example. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/examples/<ExampleID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateExampleRequest(proto.Message):
    r"""The request message for
    [Examples.UpdateExample][google.cloud.dialogflow.cx.v3beta1.Examples.UpdateExample].

    Attributes:
        example (google.cloud.dialogflowcx_v3beta1.types.Example):
            Required. The example to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated. If the mask is not present, all
            fields will be updated.
    """

    example: "Example" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Example",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Example(proto.Message):
    r"""Example represents a sample execution of the playbook in the
    conversation.
    An example consists of a list of ordered actions performed by
    end user or Dialogflow agent according the playbook instructions
    to fulfill the task.

    Attributes:
        name (str):
            The unique identifier of the playbook example. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/examples/<ExampleID>``.
        playbook_input (google.cloud.dialogflowcx_v3beta1.types.PlaybookInput):
            Optional. The input to the playbook in the
            example.
        playbook_output (google.cloud.dialogflowcx_v3beta1.types.PlaybookOutput):
            Optional. The output of the playbook in the
            example.
        actions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Action]):
            Required. The ordered list of actions
            performed by the end user and the Dialogflow
            agent.
        display_name (str):
            Required. The display name of the example.
        description (str):
            Optional. The high level concise description
            of the example. The max number of characters is
            200.
        token_count (int):
            Output only. Estimated number of tokes
            current example takes when sent to the LLM.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of initial example
            creation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the example was
            updated.
        conversation_state (google.cloud.dialogflowcx_v3beta1.types.OutputState):
            Required. Example's output state.
        language_code (str):
            Optional. The language code of the example.
            If not specified, the agent's default language
            is used. Note: languages must be enabled in the
            agent before they can be used. Note: example's
            language code is not currently used in
            dialogflow agents.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    playbook_input: trace.PlaybookInput = proto.Field(
        proto.MESSAGE,
        number=3,
        message=trace.PlaybookInput,
    )
    playbook_output: trace.PlaybookOutput = proto.Field(
        proto.MESSAGE,
        number=4,
        message=trace.PlaybookOutput,
    )
    actions: MutableSequence[trace.Action] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=trace.Action,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    token_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    conversation_state: trace.OutputState = proto.Field(
        proto.ENUM,
        number=12,
        enum=trace.OutputState,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
