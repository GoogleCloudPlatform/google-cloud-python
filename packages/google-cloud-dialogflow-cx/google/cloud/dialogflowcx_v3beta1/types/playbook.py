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

from google.cloud.dialogflowcx_v3beta1.types import (
    advanced_settings,
    example,
    generative_settings,
    parameter_definition,
)
from google.cloud.dialogflowcx_v3beta1.types import code_block as gcdc_code_block
from google.cloud.dialogflowcx_v3beta1.types import fulfillment as gcdc_fulfillment
from google.cloud.dialogflowcx_v3beta1.types import (
    import_strategy as gcdc_import_strategy,
)

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "CreatePlaybookRequest",
        "DeletePlaybookRequest",
        "ListPlaybooksRequest",
        "ListPlaybooksResponse",
        "GetPlaybookRequest",
        "UpdatePlaybookRequest",
        "Playbook",
        "CreatePlaybookVersionRequest",
        "PlaybookVersion",
        "GetPlaybookVersionRequest",
        "RestorePlaybookVersionRequest",
        "RestorePlaybookVersionResponse",
        "ListPlaybookVersionsRequest",
        "ListPlaybookVersionsResponse",
        "DeletePlaybookVersionRequest",
        "ExportPlaybookRequest",
        "ImportPlaybookRequest",
        "PlaybookImportStrategy",
        "ImportPlaybookResponse",
        "ExportPlaybookResponse",
        "Handler",
    },
)


class CreatePlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.CreatePlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybook].

    Attributes:
        parent (str):
            Required. The agent to create a playbook for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        playbook (google.cloud.dialogflowcx_v3beta1.types.Playbook):
            Required. The playbook to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    playbook: "Playbook" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Playbook",
    )


class DeletePlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.DeletePlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.DeletePlaybook].

    Attributes:
        name (str):
            Required. The name of the playbook to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPlaybooksRequest(proto.Message):
    r"""The request message for
    [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybooks].

    Attributes:
        parent (str):
            Required. The agent to list playbooks from. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
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
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListPlaybooksResponse(proto.Message):
    r"""The response message for
    [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybooks].

    Attributes:
        playbooks (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Playbook]):
            The list of playbooks. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    playbooks: MutableSequence["Playbook"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Playbook",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.GetPlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.GetPlaybook].

    Attributes:
        name (str):
            Required. The name of the playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.UpdatePlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.UpdatePlaybook].

    Attributes:
        playbook (google.cloud.dialogflowcx_v3beta1.types.Playbook):
            Required. The playbook to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    playbook: "Playbook" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Playbook",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Playbook(proto.Message):
    r"""Playbook is the basic building block to instruct the LLM how
    to execute a certain task.

    A playbook consists of a goal to accomplish, an optional list of
    step by step instructions (the step instruction may refers to
    name of the custom or default plugin tools to use) to perform
    the task,
    a list of contextual input data to be passed in at the beginning
    of the invoked, and a list of output parameters to store the
    playbook result.

    Attributes:
        name (str):
            The unique identifier of the playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        display_name (str):
            Required. The human-readable name of the
            playbook, unique within an agent.
        goal (str):
            Required. High level description of the goal
            the playbook intend to accomplish. A goal should
            be concise since it's visible to other playbooks
            that may reference this playbook.
        input_parameter_definitions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ParameterDefinition]):
            Optional. Defined structured input parameters
            for this playbook.
        output_parameter_definitions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ParameterDefinition]):
            Optional. Defined structured output
            parameters for this playbook.
        instruction (google.cloud.dialogflowcx_v3beta1.types.Playbook.Instruction):
            Instruction to accomplish target goal.
        token_count (int):
            Output only. Estimated number of tokes
            current playbook takes when sent to the LLM.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of initial
            playbook creation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the playbook version
            was updated.
        referenced_playbooks (MutableSequence[str]):
            Output only. The resource name of other
            playbooks referenced by the current playbook in
            the instructions.
        referenced_flows (MutableSequence[str]):
            Output only. The resource name of flows
            referenced by the current playbook in the
            instructions.
        referenced_tools (MutableSequence[str]):
            Optional. The resource name of tools
            referenced by the current playbook in the
            instructions. If not provided explicitly, they
            are will be implied using the tool being
            referenced in goal and steps.
        inline_actions (MutableSequence[str]):
            Optional. Output only. Names of inline
            actions scoped to this playbook. These actions
            are in addition to those belonging to referenced
            tools, child playbooks, and flows, e.g. actions
            that are defined in the playbook's code block.
        code_block (google.cloud.dialogflowcx_v3beta1.types.CodeBlock):
            Optional. The playbook's scoped code block,
            which may implement handlers and actions.
        llm_model_settings (google.cloud.dialogflowcx_v3beta1.types.LlmModelSettings):
            Optional. Llm model settings for the
            playbook.
        speech_settings (google.cloud.dialogflowcx_v3beta1.types.AdvancedSettings.SpeechSettings):
            Optional. Playbook level Settings for speech
            to text detection.
        handlers (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Handler]):
            Optional. A list of registered handlers to
            execute based on the specified triggers.
        playbook_type (google.cloud.dialogflowcx_v3beta1.types.Playbook.PlaybookType):
            Optional. Type of the playbook.
    """

    class PlaybookType(proto.Enum):
        r"""Type of the playbook.

        Values:
            PLAYBOOK_TYPE_UNSPECIFIED (0):
                Unspecified type. Default to TASK.
            TASK (1):
                Task playbook.
            ROUTINE (3):
                Routine playbook.
        """

        PLAYBOOK_TYPE_UNSPECIFIED = 0
        TASK = 1
        ROUTINE = 3

    class Step(proto.Message):
        r"""Message of single step execution.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text (str):
                Step instruction in text format.

                This field is a member of `oneof`_ ``instruction``.
            steps (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Playbook.Step]):
                Sub-processing needed to execute the current
                step.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="instruction",
        )
        steps: MutableSequence["Playbook.Step"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Playbook.Step",
        )

    class Instruction(proto.Message):
        r"""Message of the Instruction of the playbook.

        Attributes:
            guidelines (str):
                General guidelines for the playbook. These
                are unstructured instructions that are not
                directly part of the goal, e.g. "Always be
                polite". It's valid for this text to be long and
                used instead of steps altogether.
            steps (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Playbook.Step]):
                Ordered list of step by step execution
                instructions to accomplish target goal.
        """

        guidelines: str = proto.Field(
            proto.STRING,
            number=1,
        )
        steps: MutableSequence["Playbook.Step"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Playbook.Step",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    goal: str = proto.Field(
        proto.STRING,
        number=3,
    )
    input_parameter_definitions: MutableSequence[
        parameter_definition.ParameterDefinition
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=parameter_definition.ParameterDefinition,
    )
    output_parameter_definitions: MutableSequence[
        parameter_definition.ParameterDefinition
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=parameter_definition.ParameterDefinition,
    )
    instruction: Instruction = proto.Field(
        proto.MESSAGE,
        number=17,
        message=Instruction,
    )
    token_count: int = proto.Field(
        proto.INT64,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    referenced_playbooks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    referenced_flows: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    referenced_tools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    inline_actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    code_block: gcdc_code_block.CodeBlock = proto.Field(
        proto.MESSAGE,
        number=21,
        message=gcdc_code_block.CodeBlock,
    )
    llm_model_settings: generative_settings.LlmModelSettings = proto.Field(
        proto.MESSAGE,
        number=14,
        message=generative_settings.LlmModelSettings,
    )
    speech_settings: advanced_settings.AdvancedSettings.SpeechSettings = proto.Field(
        proto.MESSAGE,
        number=20,
        message=advanced_settings.AdvancedSettings.SpeechSettings,
    )
    handlers: MutableSequence["Handler"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="Handler",
    )
    playbook_type: PlaybookType = proto.Field(
        proto.ENUM,
        number=19,
        enum=PlaybookType,
    )


class CreatePlaybookVersionRequest(proto.Message):
    r"""The request message for
    [Playbooks.CreatePlaybookVersion][google.cloud.dialogflow.cx.v3beta1.Playbooks.CreatePlaybookVersion].

    Attributes:
        parent (str):
            Required. The playbook to create a version for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        playbook_version (google.cloud.dialogflowcx_v3beta1.types.PlaybookVersion):
            Required. The playbook version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    playbook_version: "PlaybookVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PlaybookVersion",
    )


class PlaybookVersion(proto.Message):
    r"""Playbook version is a snapshot of the playbook at certain
    timestamp.

    Attributes:
        name (str):
            The unique identifier of the playbook version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>``.
        description (str):
            Optional. The description of the playbook
            version.
        playbook (google.cloud.dialogflowcx_v3beta1.types.Playbook):
            Output only. Snapshot of the playbook when
            the playbook version is created.
        examples (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Example]):
            Output only. Snapshot of the examples
            belonging to the playbook when the playbook
            version is created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last time the playbook version
            was created or modified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    playbook: "Playbook" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Playbook",
    )
    examples: MutableSequence[example.Example] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=example.Example,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class GetPlaybookVersionRequest(proto.Message):
    r"""The request message for
    [Playbooks.GetPlaybookVersion][google.cloud.dialogflow.cx.v3beta1.Playbooks.GetPlaybookVersion].

    Attributes:
        name (str):
            Required. The name of the playbook version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestorePlaybookVersionRequest(proto.Message):
    r"""The request message for
    [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3beta1.Playbooks.RestorePlaybookVersion].

    Attributes:
        name (str):
            Required. The name of the playbook version. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestorePlaybookVersionResponse(proto.Message):
    r"""The response message for
    [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3beta1.Playbooks.RestorePlaybookVersion].

    Attributes:
        playbook (google.cloud.dialogflowcx_v3beta1.types.Playbook):
            The updated playbook.
    """

    playbook: "Playbook" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Playbook",
    )


class ListPlaybookVersionsRequest(proto.Message):
    r"""The request message for
    [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybookVersions].

    Attributes:
        parent (str):
            Required. The playbook to list versions for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
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


class ListPlaybookVersionsResponse(proto.Message):
    r"""The response message for
    [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3beta1.Playbooks.ListPlaybookVersions].

    Attributes:
        playbook_versions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.PlaybookVersion]):
            The list of playbook version. There will be a maximum number
            of items returned based on the page_size field in the
            request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    playbook_versions: MutableSequence["PlaybookVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PlaybookVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeletePlaybookVersionRequest(proto.Message):
    r"""The request message for
    [Playbooks.DeletePlaybookVersion][google.cloud.dialogflow.cx.v3beta1.Playbooks.DeletePlaybookVersion].

    Attributes:
        name (str):
            Required. The name of the playbook version to delete.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportPlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.ExportPlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.ExportPlaybook].

    Attributes:
        name (str):
            Required. The name of the playbook to export. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        playbook_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the playbook to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. If left unspecified,
            the serialized playbook is returned inline.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.
        data_format (google.cloud.dialogflowcx_v3beta1.types.ExportPlaybookRequest.DataFormat):
            Optional. The data format of the exported agent. If not
            specified, ``BLOB`` is assumed.
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported playbook.

        Values:
            DATA_FORMAT_UNSPECIFIED (0):
                Unspecified format.
            BLOB (1):
                Flow content will be exported as raw bytes.
            JSON (2):
                Flow content will be exported in JSON format.
        """

        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1
        JSON = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    playbook_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_format: DataFormat = proto.Field(
        proto.ENUM,
        number=3,
        enum=DataFormat,
    )


class ImportPlaybookRequest(proto.Message):
    r"""The request message for
    [Playbooks.ImportPlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.ImportPlaybook].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to import the playbook into. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        playbook_uri (str):
            [Dialogflow access control]
            (https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).

            This field is a member of `oneof`_ ``playbook``.
        playbook_content (bytes):
            Uncompressed raw byte content for playbook.

            This field is a member of `oneof`_ ``playbook``.
        import_strategy (google.cloud.dialogflowcx_v3beta1.types.PlaybookImportStrategy):
            Optional. Specifies the import strategy used
            when resolving resource conflicts.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    playbook_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="playbook",
    )
    playbook_content: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="playbook",
    )
    import_strategy: "PlaybookImportStrategy" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PlaybookImportStrategy",
    )


class PlaybookImportStrategy(proto.Message):
    r"""The playbook import strategy used for resource conflict resolution
    associated with an
    [ImportPlaybookRequest][google.cloud.dialogflow.cx.v3beta1.ImportPlaybookRequest].

    Attributes:
        main_playbook_import_strategy (google.cloud.dialogflowcx_v3beta1.types.ImportStrategy):
            Optional. Specifies the import strategy used when resolving
            conflicts with the main playbook. If not specified,
            'CREATE_NEW' is assumed.
        nested_resource_import_strategy (google.cloud.dialogflowcx_v3beta1.types.ImportStrategy):
            Optional. Specifies the import strategy used when resolving
            referenced playbook/flow conflicts. If not specified,
            'CREATE_NEW' is assumed.
        tool_import_strategy (google.cloud.dialogflowcx_v3beta1.types.ImportStrategy):
            Optional. Specifies the import strategy used when resolving
            tool conflicts. If not specified, 'CREATE_NEW' is assumed.
            This will be applied after the main playbook and nested
            resource import strategies, meaning if the playbook that
            references the tool is skipped, the tool will also be
            skipped.
    """

    main_playbook_import_strategy: gcdc_import_strategy.ImportStrategy = proto.Field(
        proto.ENUM,
        number=4,
        enum=gcdc_import_strategy.ImportStrategy,
    )
    nested_resource_import_strategy: gcdc_import_strategy.ImportStrategy = proto.Field(
        proto.ENUM,
        number=5,
        enum=gcdc_import_strategy.ImportStrategy,
    )
    tool_import_strategy: gcdc_import_strategy.ImportStrategy = proto.Field(
        proto.ENUM,
        number=6,
        enum=gcdc_import_strategy.ImportStrategy,
    )


class ImportPlaybookResponse(proto.Message):
    r"""The response message for
    [Playbooks.ImportPlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.ImportPlaybook].

    Attributes:
        playbook (str):
            The unique identifier of the new playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        conflicting_resources (google.cloud.dialogflowcx_v3beta1.types.ImportPlaybookResponse.ConflictingResources):
            Info which resources have conflicts when
            [REPORT_CONFLICTS][ImportPlaybookResponse.REPORT_CONFLICTS]
            import strategy is set for all resources in
            ImportPlaybookRequest.
    """

    class ConflictingResources(proto.Message):
        r"""Conflicting resources detected during the import process. Only
        filled when
        [REPORT_CONFLICTS][ImportPlaybookResponse.REPORT_CONFLICTS] is set
        in the request and there are conflicts in the display names.

        Attributes:
            main_playbook_display_name (str):
                Display name of conflicting main playbook.
            nested_playbook_display_names (MutableSequence[str]):
                Display names of conflicting nested
                playbooks.
            tool_display_names (MutableSequence[str]):
                Display names of conflicting tools.
        """

        main_playbook_display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        nested_playbook_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        tool_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    playbook: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conflicting_resources: ConflictingResources = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ConflictingResources,
    )


class ExportPlaybookResponse(proto.Message):
    r"""The response message for
    [Playbooks.ExportPlaybook][google.cloud.dialogflow.cx.v3beta1.Playbooks.ExportPlaybook].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        playbook_uri (str):
            The URI to a file containing the exported playbook. This
            field is populated only if ``playbook_uri`` is specified in
            [ExportPlaybookRequest][google.cloud.dialogflow.cx.v3beta1.ExportPlaybookRequest].

            This field is a member of `oneof`_ ``playbook``.
        playbook_content (bytes):
            Uncompressed raw byte content for playbook.

            This field is a member of `oneof`_ ``playbook``.
    """

    playbook_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="playbook",
    )
    playbook_content: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="playbook",
    )


class Handler(proto.Message):
    r"""Handler can be used to define custom logic to be executed
    based on the user-specified triggers.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_handler (google.cloud.dialogflowcx_v3beta1.types.Handler.EventHandler):
            A handler triggered by event.

            This field is a member of `oneof`_ ``handler``.
        lifecycle_handler (google.cloud.dialogflowcx_v3beta1.types.Handler.LifecycleHandler):
            A handler triggered during specific lifecycle
            of the playbook execution.

            This field is a member of `oneof`_ ``handler``.
    """

    class EventHandler(proto.Message):
        r"""A handler that is triggered by the specified
        [event][google.cloud.dialogflow.cx.v3beta1.Handler.EventHandler.event].

        Attributes:
            event (str):
                Required. The name of the event that triggers
                this handler.
            condition (str):
                Optional. The condition that must be
                satisfied to trigger this handler.
            fulfillment (google.cloud.dialogflowcx_v3beta1.types.Fulfillment):
                Required. The fulfillment to call when the
                event occurs.
        """

        event: str = proto.Field(
            proto.STRING,
            number=1,
        )
        condition: str = proto.Field(
            proto.STRING,
            number=3,
        )
        fulfillment: gcdc_fulfillment.Fulfillment = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcdc_fulfillment.Fulfillment,
        )

    class LifecycleHandler(proto.Message):
        r"""A handler that is triggered on the specific
        [lifecycle_stage][google.cloud.dialogflow.cx.v3beta1.Handler.LifecycleHandler.lifecycle_stage]
        of the playbook execution.

        Attributes:
            lifecycle_stage (str):
                Required. The name of the lifecycle stage that triggers this
                handler. Supported values:

                - ``playbook-start``
                - ``pre-action-selection``
                - ``pre-action-execution``
            condition (str):
                Optional. The condition that must be
                satisfied to trigger this handler.
            fulfillment (google.cloud.dialogflowcx_v3beta1.types.Fulfillment):
                Required. The fulfillment to call when this
                handler is triggered.
        """

        lifecycle_stage: str = proto.Field(
            proto.STRING,
            number=1,
        )
        condition: str = proto.Field(
            proto.STRING,
            number=2,
        )
        fulfillment: gcdc_fulfillment.Fulfillment = proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcdc_fulfillment.Fulfillment,
        )

    event_handler: EventHandler = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="handler",
        message=EventHandler,
    )
    lifecycle_handler: LifecycleHandler = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="handler",
        message=LifecycleHandler,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
