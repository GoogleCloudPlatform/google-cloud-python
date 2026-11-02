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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1beta.types import python_function as gcc_python_function
from google.cloud.ces_v1beta.types import schema

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "WidgetTool",
    },
)


class WidgetTool(proto.Message):
    r"""Represents a widget tool that the agent can invoke. When the
    tool is chosen by the agent, agent will return the widget to the
    client. The client is responsible for processing the widget and
    generating the next user query to continue the interaction with
    the agent.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parameters (google.cloud.ces_v1beta.types.Schema):
            Optional. The input parameters of the widget
            tool.

            This field is a member of `oneof`_ ``input``.
        name (str):
            Required. The display name of the widget
            tool.
        description (str):
            Optional. The description of the widget tool.
        widget_type (google.cloud.ces_v1beta.types.WidgetTool.WidgetType):
            Optional. The type of the widget tool. If not
            specified, the default type will be CUSTOMIZED.
        ui_config (google.protobuf.struct_pb2.Struct):
            Optional. Configuration for rendering the
            widget.
        data_mapping (google.cloud.ces_v1beta.types.WidgetTool.DataMapping):
            Optional. The mapping that defines how data
            from a source tool is mapped to the widget's
            input parameters.
        text_response_config (google.cloud.ces_v1beta.types.WidgetTool.TextResponseConfig):
            Optional. Configuration for always-included
            text responses.
    """

    class WidgetType(proto.Enum):
        r"""All available widget types.
        New values may be added to this enum in the future.

        Values:
            WIDGET_TYPE_UNSPECIFIED (0):
                Unspecified widget type.
            CUSTOM (1):
                Custom widget type.
            PRODUCT_CAROUSEL (2):
                Product carousel widget.
            PRODUCT_DETAILS (3):
                Product details widget.
            QUICK_ACTIONS (4):
                Quick actions widget.
            PRODUCT_COMPARISON (5):
                Product comparison widget.
            ADVANCED_PRODUCT_DETAILS (6):
                Advanced product details widget.
            SHORT_FORM (7):
                Short form widget.
            OVERALL_SATISFACTION (8):
                Overall satisfaction widget.
            ORDER_SUMMARY (9):
                Order summary widget.
            APPOINTMENT_DETAILS (10):
                Appointment details widget.
            APPOINTMENT_SCHEDULER (11):
                Appointment scheduler widget.
            CONTACT_FORM (12):
                Contact form widget.
        """

        WIDGET_TYPE_UNSPECIFIED = 0
        CUSTOM = 1
        PRODUCT_CAROUSEL = 2
        PRODUCT_DETAILS = 3
        QUICK_ACTIONS = 4
        PRODUCT_COMPARISON = 5
        ADVANCED_PRODUCT_DETAILS = 6
        SHORT_FORM = 7
        OVERALL_SATISFACTION = 8
        ORDER_SUMMARY = 9
        APPOINTMENT_DETAILS = 10
        APPOINTMENT_SCHEDULER = 11
        CONTACT_FORM = 12

    class TextResponseConfig(proto.Message):
        r"""Configuration for the text response returned with the widget.

        Attributes:
            type_ (google.cloud.ces_v1beta.types.WidgetTool.TextResponseConfig.Type):
                Optional. The strategy for providing the text
                response.
            static_text (str):
                Optional. The static text response to return
                when type is STATIC.
            text_response_instruction (str):
                Optional. Instruction for the LLM on how to generate the
                text response. Used as the description for the text response
                parameter if type is LLM_GENERATED.
        """

        class Type(proto.Enum):
            r"""Defines how the text response is produced.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                NONE (1):
                    The LLM dynamically decides whether to
                    generate a text response alongside the widget
                    based on the conversation context.
                LLM_GENERATED (2):
                    The LLM is explicitly required to generate a
                    text response.
                STATIC (3):
                    A pre-defined static text response is always
                    used.
            """

            TYPE_UNSPECIFIED = 0
            NONE = 1
            LLM_GENERATED = 2
            STATIC = 3

        type_: "WidgetTool.TextResponseConfig.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WidgetTool.TextResponseConfig.Type",
        )
        static_text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        text_response_instruction: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class DataMapping(proto.Message):
        r"""Configuration for mapping data from a source tool to the
        widget's input parameters.

        Attributes:
            source_tool_name (str):
                Optional. The resource name of the tool that provides the
                data for the widget (e.g., a search tool or a custom
                function). Format:
                ``projects/{project}/locations/{location}/agents/{agent}/tools/{tool}``
            field_mappings (MutableMapping[str, str]):
                Optional. A map of widget input parameter
                fields to the corresponding output fields of the
                source tool.
            python_function (google.cloud.ces_v1beta.types.PythonFunction):
                Optional. Configuration for a Python function
                used to transform the source tool's output into
                the widget's input format.
            mode (google.cloud.ces_v1beta.types.WidgetTool.DataMapping.Mode):
                Optional. The mode of the data mapping.
            python_script (str):
                Deprecated: Use ``python_function`` instead.
        """

        class Mode(proto.Enum):
            r"""The strategy used to map data from the source tool to the
            widget.

            Values:
                MODE_UNSPECIFIED (0):
                    Unspecified mode.
                FIELD_MAPPING (1):
                    Use the ``field_mappings`` map for data transformation.
                PYTHON_SCRIPT (2):
                    Use the ``python_script`` for data transformation.
            """

            MODE_UNSPECIFIED = 0
            FIELD_MAPPING = 1
            PYTHON_SCRIPT = 2

        source_tool_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        field_mappings: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        python_function: gcc_python_function.PythonFunction = proto.Field(
            proto.MESSAGE,
            number=5,
            message=gcc_python_function.PythonFunction,
        )
        mode: "WidgetTool.DataMapping.Mode" = proto.Field(
            proto.ENUM,
            number=4,
            enum="WidgetTool.DataMapping.Mode",
        )
        python_script: str = proto.Field(
            proto.STRING,
            number=3,
        )

    parameters: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="input",
        message=schema.Schema,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    widget_type: WidgetType = proto.Field(
        proto.ENUM,
        number=3,
        enum=WidgetType,
    )
    ui_config: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    data_mapping: DataMapping = proto.Field(
        proto.MESSAGE,
        number=6,
        message=DataMapping,
    )
    text_response_config: TextResponseConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=TextResponseConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
