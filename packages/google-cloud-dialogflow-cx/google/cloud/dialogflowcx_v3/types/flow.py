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

from google.cloud.dialogflowcx_v3.types import (
    advanced_settings as gcdc_advanced_settings,
)
from google.cloud.dialogflowcx_v3.types import (
    import_strategy,
    page,
    parameter_definition,
    validation_message,
)

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "NluSettings",
        "Flow",
        "CreateFlowRequest",
        "DeleteFlowRequest",
        "ListFlowsRequest",
        "ListFlowsResponse",
        "GetFlowRequest",
        "UpdateFlowRequest",
        "TrainFlowRequest",
        "ValidateFlowRequest",
        "GetFlowValidationResultRequest",
        "FlowValidationResult",
        "ImportFlowRequest",
        "FlowImportStrategy",
        "ImportFlowResponse",
        "ExportFlowRequest",
        "ExportFlowResponse",
    },
)


class NluSettings(proto.Message):
    r"""Settings related to NLU.

    Attributes:
        model_type (google.cloud.dialogflowcx_v3.types.NluSettings.ModelType):
            Indicates the type of NLU model.
        classification_threshold (float):
            To filter out false positive results and
            still get variety in matched natural language
            inputs for your agent, you can tune the machine
            learning classification threshold. If the
            returned score value is less than the threshold
            value, then a no-match event will be triggered.
            The score values range from 0.0 (completely
            uncertain) to 1.0 (completely certain). If set
            to 0.0, the default of 0.3 is used. You can set
            a separate classification threshold for the flow
            in each language enabled for the agent.
        model_training_mode (google.cloud.dialogflowcx_v3.types.NluSettings.ModelTrainingMode):
            Indicates NLU model training mode.
    """

    class ModelType(proto.Enum):
        r"""NLU model type.

        Values:
            MODEL_TYPE_UNSPECIFIED (0):
                Not specified. ``MODEL_TYPE_STANDARD`` will be used.
            MODEL_TYPE_STANDARD (1):
                Use standard NLU model.
            MODEL_TYPE_ADVANCED (3):
                Use advanced NLU model.
        """

        MODEL_TYPE_UNSPECIFIED = 0
        MODEL_TYPE_STANDARD = 1
        MODEL_TYPE_ADVANCED = 3

    class ModelTrainingMode(proto.Enum):
        r"""NLU model training mode.

        Values:
            MODEL_TRAINING_MODE_UNSPECIFIED (0):
                Not specified. ``MODEL_TRAINING_MODE_AUTOMATIC`` will be
                used.
            MODEL_TRAINING_MODE_AUTOMATIC (1):
                NLU model training is automatically triggered
                when a flow gets modified. User can also
                manually trigger model training in this mode.
            MODEL_TRAINING_MODE_MANUAL (2):
                User needs to manually trigger NLU model
                training. Best for large flows whose models take
                long time to train.
        """

        MODEL_TRAINING_MODE_UNSPECIFIED = 0
        MODEL_TRAINING_MODE_AUTOMATIC = 1
        MODEL_TRAINING_MODE_MANUAL = 2

    model_type: ModelType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ModelType,
    )
    classification_threshold: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    model_training_mode: ModelTrainingMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=ModelTrainingMode,
    )


class Flow(proto.Message):
    r"""Flows represents the conversation flows when you build your
    chatbot agent.
    A flow consists of many pages connected by the transition
    routes. Conversations always start with the built-in Start Flow
    (with an all-0 ID). Transition routes can direct the
    conversation session from the current flow (parent flow) to
    another flow (sub flow). When the sub flow is finished,
    Dialogflow will bring the session back to the parent flow, where
    the sub flow is started.

    Usually, when a transition route is followed by a matched
    intent, the intent will be "consumed". This means the intent
    won't activate more transition routes. However, when the
    followed transition route moves the conversation session into a
    different flow, the matched intent can be carried over and to be
    consumed in the target flow.

    Attributes:
        name (str):
            The unique identifier of the flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        display_name (str):
            Required. The human-readable name of the
            flow.
        description (str):
            The description of the flow. The maximum
            length is 500 characters. If exceeded, the
            request is rejected.
        transition_routes (MutableSequence[google.cloud.dialogflowcx_v3.types.TransitionRoute]):
            A flow's transition routes serve two purposes:

            - They are responsible for matching the user's first
              utterances in the flow.
            - They are inherited by every page's [transition
              routes][Page.transition_routes] and can support use cases
              such as the user saying "help" or "can I talk to a
              human?", which can be handled in a common way regardless
              of the current page. Transition routes defined in the page
              have higher priority than those defined in the flow.

            TransitionRoutes are evaluated in the following order:

            - TransitionRoutes with intent specified.
            - TransitionRoutes with only condition specified.

            TransitionRoutes with intent specified are inherited by
            pages in the flow.
        event_handlers (MutableSequence[google.cloud.dialogflowcx_v3.types.EventHandler]):
            A flow's event handlers serve two purposes:

            - They are responsible for handling events (e.g. no match,
              webhook errors) in the flow.
            - They are inherited by every page's [event
              handlers][Page.event_handlers], which can be used to
              handle common events regardless of the current page. Event
              handlers defined in the page have higher priority than
              those defined in the flow.

            Unlike
            [transition_routes][google.cloud.dialogflow.cx.v3.Flow.transition_routes],
            these handlers are evaluated on a first-match basis. The
            first one that matches the event get executed, with the rest
            being ignored.
        transition_route_groups (MutableSequence[str]):
            A flow's transition route group serve two purposes:

            - They are responsible for matching the user's first
              utterances in the flow.
            - They are inherited by every page's [transition route
              groups][Page.transition_route_groups]. Transition route
              groups defined in the page have higher priority than those
              defined in the flow.

            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>``
            for agent-level groups.
        nlu_settings (google.cloud.dialogflowcx_v3.types.NluSettings):
            NLU related settings of the flow.
        advanced_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings):
            Hierarchical advanced settings for this flow.
            The settings exposed at the lower level
            overrides the settings exposed at the higher
            level.
        knowledge_connector_settings (google.cloud.dialogflowcx_v3.types.KnowledgeConnectorSettings):
            Optional. Knowledge connector configuration.
        input_parameter_definitions (MutableSequence[google.cloud.dialogflowcx_v3.types.ParameterDefinition]):
            Optional. Defined structured input parameters
            for this flow.
        output_parameter_definitions (MutableSequence[google.cloud.dialogflowcx_v3.types.ParameterDefinition]):
            Optional. Defined structured output
            parameters for this flow.
        multi_language_settings (google.cloud.dialogflowcx_v3.types.Flow.MultiLanguageSettings):
            Optional. Multi-lingual agent settings for
            this flow.
        locked (bool):
            Indicates whether the flow is locked for
            changes. If the flow is locked, modifications to
            the flow will be rejected.
    """

    class MultiLanguageSettings(proto.Message):
        r"""Settings for multi-lingual agents.

        Attributes:
            enable_multi_language_detection (bool):
                Optional. Enable multi-language detection for this flow.
                This can be set only if [agent level multi language
                setting][Agent.enable_multi_language_training] is enabled.
            supported_response_language_codes (MutableSequence[str]):
                Optional. Agent will respond in the detected language if the
                detected language code is in the supported resolved
                languages for this flow. This will be used only if
                multi-language training is enabled in the
                [agent][google.cloud.dialogflow.cx.v3.Agent.enable_multi_language_training]
                and multi-language detection is enabled in the
                [flow][google.cloud.dialogflow.cx.v3.Flow.MultiLanguageSettings.enable_multi_language_detection].
                The supported languages must be a subset of the languages
                supported by the agent.
        """

        enable_multi_language_detection: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        supported_response_language_codes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    transition_routes: MutableSequence[page.TransitionRoute] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=page.TransitionRoute,
    )
    event_handlers: MutableSequence[page.EventHandler] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=page.EventHandler,
    )
    transition_route_groups: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    nlu_settings: "NluSettings" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="NluSettings",
    )
    advanced_settings: gcdc_advanced_settings.AdvancedSettings = proto.Field(
        proto.MESSAGE,
        number=14,
        message=gcdc_advanced_settings.AdvancedSettings,
    )
    knowledge_connector_settings: page.KnowledgeConnectorSettings = proto.Field(
        proto.MESSAGE,
        number=18,
        message=page.KnowledgeConnectorSettings,
    )
    input_parameter_definitions: MutableSequence[
        parameter_definition.ParameterDefinition
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message=parameter_definition.ParameterDefinition,
    )
    output_parameter_definitions: MutableSequence[
        parameter_definition.ParameterDefinition
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message=parameter_definition.ParameterDefinition,
    )
    multi_language_settings: MultiLanguageSettings = proto.Field(
        proto.MESSAGE,
        number=28,
        message=MultiLanguageSettings,
    )
    locked: bool = proto.Field(
        proto.BOOL,
        number=30,
    )


class CreateFlowRequest(proto.Message):
    r"""The request message for
    [Flows.CreateFlow][google.cloud.dialogflow.cx.v3.Flows.CreateFlow].

    Attributes:
        parent (str):
            Required. The agent to create a flow for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        flow (google.cloud.dialogflowcx_v3.types.Flow):
            Required. The flow to create.
        language_code (str):
            The language of the following fields in ``flow``:

            - ``Flow.event_handlers.trigger_fulfillment.messages``
            - ``Flow.event_handlers.trigger_fulfillment.conditional_cases``
            - ``Flow.transition_routes.trigger_fulfillment.messages``
            - ``Flow.transition_routes.trigger_fulfillment.conditional_cases``

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
    flow: "Flow" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Flow",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteFlowRequest(proto.Message):
    r"""The request message for
    [Flows.DeleteFlow][google.cloud.dialogflow.cx.v3.Flows.DeleteFlow].

    Attributes:
        name (str):
            Required. The name of the flow to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        force (bool):
            This field has no effect for flows with no incoming
            transitions. For flows with incoming transitions:

            - If ``force`` is set to false, an error will be returned
              with message indicating the incoming transitions.
            - If ``force`` is set to true, Dialogflow will remove the
              flow, as well as any transitions to the flow (i.e. [Target
              flow][EventHandler.target_flow] in event handlers or
              [Target flow][TransitionRoute.target_flow] in transition
              routes that point to this flow will be cleared).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListFlowsRequest(proto.Message):
    r"""The request message for
    [Flows.ListFlows][google.cloud.dialogflow.cx.v3.Flows.ListFlows].

    Attributes:
        parent (str):
            Required. The agent containing the flows. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
        language_code (str):
            The language to list flows for. The following fields are
            language dependent:

            - ``Flow.event_handlers.trigger_fulfillment.messages``
            - ``Flow.event_handlers.trigger_fulfillment.conditional_cases``
            - ``Flow.transition_routes.trigger_fulfillment.messages``
            - ``Flow.transition_routes.trigger_fulfillment.conditional_cases``

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


class ListFlowsResponse(proto.Message):
    r"""The response message for
    [Flows.ListFlows][google.cloud.dialogflow.cx.v3.Flows.ListFlows].

    Attributes:
        flows (MutableSequence[google.cloud.dialogflowcx_v3.types.Flow]):
            The list of flows. There will be a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    flows: MutableSequence["Flow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Flow",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFlowRequest(proto.Message):
    r"""The response message for
    [Flows.GetFlow][google.cloud.dialogflow.cx.v3.Flows.GetFlow].

    Attributes:
        name (str):
            Required. The name of the flow to get. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        language_code (str):
            The language to retrieve the flow for. The following fields
            are language dependent:

            - ``Flow.event_handlers.trigger_fulfillment.messages``
            - ``Flow.event_handlers.trigger_fulfillment.conditional_cases``
            - ``Flow.transition_routes.trigger_fulfillment.messages``
            - ``Flow.transition_routes.trigger_fulfillment.conditional_cases``

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


class UpdateFlowRequest(proto.Message):
    r"""The request message for
    [Flows.UpdateFlow][google.cloud.dialogflow.cx.v3.Flows.UpdateFlow].

    Attributes:
        flow (google.cloud.dialogflowcx_v3.types.Flow):
            Required. The flow to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
        language_code (str):
            The language of the following fields in ``flow``:

            - ``Flow.event_handlers.trigger_fulfillment.messages``
            - ``Flow.event_handlers.trigger_fulfillment.conditional_cases``
            - ``Flow.transition_routes.trigger_fulfillment.messages``
            - ``Flow.transition_routes.trigger_fulfillment.conditional_cases``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    flow: "Flow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Flow",
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


class TrainFlowRequest(proto.Message):
    r"""The request message for
    [Flows.TrainFlow][google.cloud.dialogflow.cx.v3.Flows.TrainFlow].

    Attributes:
        name (str):
            Required. The flow to train. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ValidateFlowRequest(proto.Message):
    r"""The request message for
    [Flows.ValidateFlow][google.cloud.dialogflow.cx.v3.Flows.ValidateFlow].

    Attributes:
        name (str):
            Required. The flow to validate. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        language_code (str):
            If not specified, the agent's default
            language is used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFlowValidationResultRequest(proto.Message):
    r"""The request message for
    [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult].

    Attributes:
        name (str):
            Required. The flow name. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/validationResult``.
        language_code (str):
            If not specified, the agent's default
            language is used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FlowValidationResult(proto.Message):
    r"""The response message for
    [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult].

    Attributes:
        name (str):
            The unique identifier of the flow validation result. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/validationResult``.
        validation_messages (MutableSequence[google.cloud.dialogflowcx_v3.types.ValidationMessage]):
            Contains all validation messages.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the flow was validated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validation_messages: MutableSequence[validation_message.ValidationMessage] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=validation_message.ValidationMessage,
        )
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ImportFlowRequest(proto.Message):
    r"""The request message for
    [Flows.ImportFlow][google.cloud.dialogflow.cx.v3.Flows.ImportFlow].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to import the flow into. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        flow_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            import flow from. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a read operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have read permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``flow``.
        flow_content (bytes):
            Uncompressed raw byte content for flow.

            This field is a member of `oneof`_ ``flow``.
        import_option (google.cloud.dialogflowcx_v3.types.ImportFlowRequest.ImportOption):
            Flow import mode. If not specified, ``KEEP`` is assumed.
        flow_import_strategy (google.cloud.dialogflowcx_v3.types.FlowImportStrategy):
            Optional. Specifies the import strategy used
            when resolving resource conflicts.
    """

    class ImportOption(proto.Enum):
        r"""Import option.

        Values:
            IMPORT_OPTION_UNSPECIFIED (0):
                Unspecified. Treated as ``KEEP``.
            KEEP (1):
                Always respect settings in exported flow
                content. It may cause a import failure if some
                settings (e.g. custom NLU) are not supported in
                the agent to import into.
            FALLBACK (2):
                Fallback to default settings if some settings
                are not supported in the agent to import into.
                E.g. Standard NLU will be used if custom NLU is
                not available.
        """

        IMPORT_OPTION_UNSPECIFIED = 0
        KEEP = 1
        FALLBACK = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flow_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="flow",
    )
    flow_content: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="flow",
    )
    import_option: ImportOption = proto.Field(
        proto.ENUM,
        number=4,
        enum=ImportOption,
    )
    flow_import_strategy: "FlowImportStrategy" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FlowImportStrategy",
    )


class FlowImportStrategy(proto.Message):
    r"""The flow import strategy used for resource conflict resolution
    associated with an
    [ImportFlowRequest][google.cloud.dialogflow.cx.v3.ImportFlowRequest].

    Attributes:
        global_import_strategy (google.cloud.dialogflowcx_v3.types.ImportStrategy):
            Optional. Import strategy for resource conflict resolution,
            applied globally throughout the flow. It will be applied for
            all display name conflicts in the imported content. If not
            specified, 'CREATE_NEW' is assumed.
    """

    global_import_strategy: import_strategy.ImportStrategy = proto.Field(
        proto.ENUM,
        number=1,
        enum=import_strategy.ImportStrategy,
    )


class ImportFlowResponse(proto.Message):
    r"""The response message for
    [Flows.ImportFlow][google.cloud.dialogflow.cx.v3.Flows.ImportFlow].

    Attributes:
        flow (str):
            The unique identifier of the new flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
    """

    flow: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportFlowRequest(proto.Message):
    r"""The request message for
    [Flows.ExportFlow][google.cloud.dialogflow.cx.v3.Flows.ExportFlow].

    Attributes:
        name (str):
            Required. The name of the flow to export. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        flow_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the flow to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. If left unspecified,
            the serialized flow is returned inline.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.
        include_referenced_flows (bool):
            Optional. Whether to export flows referenced
            by the specified flow.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flow_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    include_referenced_flows: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ExportFlowResponse(proto.Message):
    r"""The response message for
    [Flows.ExportFlow][google.cloud.dialogflow.cx.v3.Flows.ExportFlow].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        flow_uri (str):
            The URI to a file containing the exported flow. This field
            is populated only if ``flow_uri`` is specified in
            [ExportFlowRequest][google.cloud.dialogflow.cx.v3.ExportFlowRequest].

            This field is a member of `oneof`_ ``flow``.
        flow_content (bytes):
            Uncompressed raw byte content for flow.

            This field is a member of `oneof`_ ``flow``.
    """

    flow_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="flow",
    )
    flow_content: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="flow",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
