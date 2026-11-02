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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ai.generativelanguage.v1beta",
    manifest={
        "Type",
        "Modality",
        "Content",
        "Part",
        "FunctionResponsePart",
        "Blob",
        "FunctionResponseBlob",
        "FileData",
        "VideoMetadata",
        "ExecutableCode",
        "CodeExecutionResult",
        "Tool",
        "GoogleMaps",
        "UrlContext",
        "FileSearch",
        "GoogleSearchRetrieval",
        "DynamicRetrievalConfig",
        "CodeExecution",
        "ToolConfig",
        "RetrievalConfig",
        "FunctionCallingConfig",
        "FunctionDeclaration",
        "FunctionCall",
        "FunctionResponse",
        "Schema",
        "GroundingPassage",
        "GroundingPassages",
        "ModalityTokenCount",
    },
)


class Type(proto.Enum):
    r"""Type contains the list of OpenAPI data types as defined by
    https://spec.openapis.org/oas/v3.0.3#data-types

    Values:
        TYPE_UNSPECIFIED (0):
            Not specified, should not be used.
        STRING (1):
            String type.
        NUMBER (2):
            Number type.
        INTEGER (3):
            Integer type.
        BOOLEAN (4):
            Boolean type.
        ARRAY (5):
            Array type.
        OBJECT (6):
            Object type.
        NULL (7):
            Null type.
    """

    TYPE_UNSPECIFIED = 0
    STRING = 1
    NUMBER = 2
    INTEGER = 3
    BOOLEAN = 4
    ARRAY = 5
    OBJECT = 6
    NULL = 7


class Modality(proto.Enum):
    r"""Content Part modality

    Values:
        MODALITY_UNSPECIFIED (0):
            Unspecified modality.
        TEXT (1):
            Plain text.
        IMAGE (2):
            Image.
        VIDEO (3):
            Video.
        AUDIO (4):
            Audio.
        DOCUMENT (5):
            Document, e.g. PDF.
    """

    MODALITY_UNSPECIFIED = 0
    TEXT = 1
    IMAGE = 2
    VIDEO = 3
    AUDIO = 4
    DOCUMENT = 5


class Content(proto.Message):
    r"""The base structured datatype containing multi-part content of a
    message.

    A ``Content`` includes a ``role`` field designating the producer of
    the ``Content`` and a ``parts`` field containing multi-part data
    that contains the content of the message turn.

    Attributes:
        parts (MutableSequence[google.ai.generativelanguage_v1beta.types.Part]):
            Ordered ``Parts`` that constitute a single message. Parts
            may have different MIME types.
        role (str):
            Optional. The producer of the content. Must
            be either 'user' or 'model'.
            Useful to set for multi-turn conversations,
            otherwise can be left blank or unset.
    """

    parts: MutableSequence["Part"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Part",
    )
    role: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Part(proto.Message):
    r"""A datatype containing media that is part of a multi-part ``Content``
    message.

    A ``Part`` consists of data which has an associated datatype. A
    ``Part`` can only contain one of the accepted types in
    ``Part.data``.

    A ``Part`` must have a fixed IANA MIME type identifying the type and
    subtype of the media if the ``inline_data`` field is filled with raw
    bytes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Inline text.

            This field is a member of `oneof`_ ``data``.
        inline_data (google.ai.generativelanguage_v1beta.types.Blob):
            Inline media bytes.

            This field is a member of `oneof`_ ``data``.
        function_call (google.ai.generativelanguage_v1beta.types.FunctionCall):
            A predicted ``FunctionCall`` returned from the model that
            contains a string representing the
            ``FunctionDeclaration.name`` with the arguments and their
            values.

            This field is a member of `oneof`_ ``data``.
        function_response (google.ai.generativelanguage_v1beta.types.FunctionResponse):
            The result output of a ``FunctionCall`` that contains a
            string representing the ``FunctionDeclaration.name`` and a
            structured JSON object containing any output from the
            function is used as context to the model.

            This field is a member of `oneof`_ ``data``.
        file_data (google.ai.generativelanguage_v1beta.types.FileData):
            URI based data.

            This field is a member of `oneof`_ ``data``.
        executable_code (google.ai.generativelanguage_v1beta.types.ExecutableCode):
            Code generated by the model that is meant to
            be executed.

            This field is a member of `oneof`_ ``data``.
        code_execution_result (google.ai.generativelanguage_v1beta.types.CodeExecutionResult):
            Result of executing the ``ExecutableCode``.

            This field is a member of `oneof`_ ``data``.
        video_metadata (google.ai.generativelanguage_v1beta.types.VideoMetadata):
            Optional. Video metadata. The metadata should only be
            specified while the video data is presented in inline_data
            or file_data.

            This field is a member of `oneof`_ ``metadata``.
        thought (bool):
            Optional. Indicates if the part is thought
            from the model.
        thought_signature (bytes):
            Optional. An opaque signature for the thought
            so it can be reused in subsequent requests.
        part_metadata (google.protobuf.struct_pb2.Struct):
            Custom metadata associated with the Part.
            Agents using genai.Part as content
            representation may need to keep track of the
            additional information. For example it can be
            name of a file/source from which the Part
            originates or a way to multiplex multiple Part
            streams.
    """

    text: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="data",
    )
    inline_data: "Blob" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message="Blob",
    )
    function_call: "FunctionCall" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="FunctionCall",
    )
    function_response: "FunctionResponse" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message="FunctionResponse",
    )
    file_data: "FileData" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message="FileData",
    )
    executable_code: "ExecutableCode" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message="ExecutableCode",
    )
    code_execution_result: "CodeExecutionResult" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message="CodeExecutionResult",
    )
    video_metadata: "VideoMetadata" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="metadata",
        message="VideoMetadata",
    )
    thought: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    thought_signature: bytes = proto.Field(
        proto.BYTES,
        number=13,
    )
    part_metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )


class FunctionResponsePart(proto.Message):
    r"""A datatype containing media that is part of a ``FunctionResponse``
    message.

    A ``FunctionResponsePart`` consists of data which has an associated
    datatype. A ``FunctionResponsePart`` can only contain one of the
    accepted types in ``FunctionResponsePart.data``.

    A ``FunctionResponsePart`` must have a fixed IANA MIME type
    identifying the type and subtype of the media if the ``inline_data``
    field is filled with raw bytes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_data (google.ai.generativelanguage_v1beta.types.FunctionResponseBlob):
            Inline media bytes.

            This field is a member of `oneof`_ ``data``.
    """

    inline_data: "FunctionResponseBlob" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data",
        message="FunctionResponseBlob",
    )


class Blob(proto.Message):
    r"""Raw media bytes.

    Text should not be sent as raw bytes, use the 'text' field.

    Attributes:
        mime_type (str):
            The IANA standard MIME type of the source data. Examples:

            - image/png
            - image/jpeg If an unsupported MIME type is provided, an
              error will be returned. For a complete list of supported
              types, see `Supported file
              formats <https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats>`__.
        data (bytes):
            Raw bytes for media formats.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class FunctionResponseBlob(proto.Message):
    r"""Raw media bytes for function response.

    Text should not be sent as raw bytes, use the
    'FunctionResponse.response' field.

    Attributes:
        mime_type (str):
            The IANA standard MIME type of the source data. Examples:

            - image/png
            - image/jpeg If an unsupported MIME type is provided, an
              error will be returned. For a complete list of supported
              types, see `Supported file
              formats <https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats>`__.
        data (bytes):
            Raw bytes for media formats.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class FileData(proto.Message):
    r"""URI based data.

    Attributes:
        mime_type (str):
            Optional. The IANA standard MIME type of the
            source data.
        file_uri (str):
            Required. URI.
    """

    mime_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VideoMetadata(proto.Message):
    r"""Metadata describes the input video content.

    Attributes:
        start_offset (google.protobuf.duration_pb2.Duration):
            Optional. The start offset of the video.
        end_offset (google.protobuf.duration_pb2.Duration):
            Optional. The end offset of the video.
        fps (float):
            Optional. The frame rate of the video sent to the model. If
            not specified, the default value will be 1.0. The fps range
            is (0.0, 24.0].
    """

    start_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    end_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    fps: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class ExecutableCode(proto.Message):
    r"""Code generated by the model that is meant to be executed, and the
    result returned to the model.

    Only generated when using the ``CodeExecution`` tool, in which the
    code will be automatically executed, and a corresponding
    ``CodeExecutionResult`` will also be generated.

    Attributes:
        language (google.ai.generativelanguage_v1beta.types.ExecutableCode.Language):
            Required. Programming language of the ``code``.
        code (str):
            Required. The code to be executed.
    """

    class Language(proto.Enum):
        r"""Supported programming languages for the generated code.

        Values:
            LANGUAGE_UNSPECIFIED (0):
                Unspecified language. This value should not
                be used.
            PYTHON (1):
                Python >= 3.10, with numpy and simpy
                available.
        """

        LANGUAGE_UNSPECIFIED = 0
        PYTHON = 1

    language: Language = proto.Field(
        proto.ENUM,
        number=1,
        enum=Language,
    )
    code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CodeExecutionResult(proto.Message):
    r"""Result of executing the ``ExecutableCode``.

    Only generated when using the ``CodeExecution``, and always follows
    a ``part`` containing the ``ExecutableCode``.

    Attributes:
        outcome (google.ai.generativelanguage_v1beta.types.CodeExecutionResult.Outcome):
            Required. Outcome of the code execution.
        output (str):
            Optional. Contains stdout when code execution
            is successful, stderr or other description
            otherwise.
    """

    class Outcome(proto.Enum):
        r"""Enumeration of possible outcomes of the code execution.

        Values:
            OUTCOME_UNSPECIFIED (0):
                Unspecified status. This value should not be
                used.
            OUTCOME_OK (1):
                Code execution completed successfully.
            OUTCOME_FAILED (2):
                Code execution finished but with a failure. ``stderr``
                should contain the reason.
            OUTCOME_DEADLINE_EXCEEDED (3):
                Code execution ran for too long, and was
                cancelled. There may or may not be a partial
                output present.
        """

        OUTCOME_UNSPECIFIED = 0
        OUTCOME_OK = 1
        OUTCOME_FAILED = 2
        OUTCOME_DEADLINE_EXCEEDED = 3

    outcome: Outcome = proto.Field(
        proto.ENUM,
        number=1,
        enum=Outcome,
    )
    output: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Tool(proto.Message):
    r"""Tool details that the model may use to generate response.

    A ``Tool`` is a piece of code that enables the system to interact
    with external systems to perform an action, or set of actions,
    outside of knowledge and scope of the model.

    Next ID: 12

    Attributes:
        function_declarations (MutableSequence[google.ai.generativelanguage_v1beta.types.FunctionDeclaration]):
            Optional. A list of ``FunctionDeclarations`` available to
            the model that can be used for function calling.

            The model or system does not execute the function. Instead
            the defined function may be returned as a
            [FunctionCall][google.ai.generativelanguage.v1beta.Part.function_call]
            with arguments to the client side for execution. The model
            may decide to call a subset of these functions by populating
            [FunctionCall][google.ai.generativelanguage.v1beta.Part.function_call]
            in the response. The next conversation turn may contain a
            [FunctionResponse][google.ai.generativelanguage.v1beta.Part.function_response]
            with the
            [Content.role][google.ai.generativelanguage.v1beta.Content.role]
            "function" generation context for the next model turn.
        google_search_retrieval (google.ai.generativelanguage_v1beta.types.GoogleSearchRetrieval):
            Optional. Retrieval tool that is powered by
            Google search.
        code_execution (google.ai.generativelanguage_v1beta.types.CodeExecution):
            Optional. Enables the model to execute code
            as part of generation.
        google_search (google.ai.generativelanguage_v1beta.types.Tool.GoogleSearch):
            Optional. GoogleSearch tool type.
            Tool to support Google Search in Model. Powered
            by Google.
        computer_use (google.ai.generativelanguage_v1beta.types.Tool.ComputerUse):
            Optional. Tool to support the model
            interacting directly with the computer. If
            enabled, it automatically populates computer-use
            specific Function Declarations.
        url_context (google.ai.generativelanguage_v1beta.types.UrlContext):
            Optional. Tool to support URL context
            retrieval.
        file_search (google.ai.generativelanguage_v1beta.types.FileSearch):
            Optional. FileSearch tool type.
            Tool to retrieve knowledge from Semantic
            Retrieval corpora.
        google_maps (google.ai.generativelanguage_v1beta.types.GoogleMaps):
            Optional. Tool that allows grounding the
            model's response with geospatial context related
            to the user's query.
    """

    class GoogleSearch(proto.Message):
        r"""GoogleSearch tool type.
        Tool to support Google Search in Model. Powered by Google.

        Attributes:
            time_range_filter (google.type.interval_pb2.Interval):
                Optional. Filter search results to a specific
                time range. If customers set a start time, they
                must set an end time (and vice versa).
        """

        time_range_filter: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=2,
            message=interval_pb2.Interval,
        )

    class ComputerUse(proto.Message):
        r"""Computer Use tool type.

        Attributes:
            environment (google.ai.generativelanguage_v1beta.types.Tool.ComputerUse.Environment):
                Required. The environment being operated.
            excluded_predefined_functions (MutableSequence[str]):
                Optional. By default, predefined functions
                are included in the final model call. Some of
                them can be explicitly excluded from being
                automatically included. This can serve two
                purposes:

                1. Using a more restricted / different action
                    space.
                2. Improving the definitions / instructions of
                    predefined functions.
        """

        class Environment(proto.Enum):
            r"""Represents the environment being operated, such as a web
            browser.

            Values:
                ENVIRONMENT_UNSPECIFIED (0):
                    Defaults to browser.
                ENVIRONMENT_BROWSER (1):
                    Operates in a web browser.
            """

            ENVIRONMENT_UNSPECIFIED = 0
            ENVIRONMENT_BROWSER = 1

        environment: "Tool.ComputerUse.Environment" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Tool.ComputerUse.Environment",
        )
        excluded_predefined_functions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )

    function_declarations: MutableSequence["FunctionDeclaration"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FunctionDeclaration",
    )
    google_search_retrieval: "GoogleSearchRetrieval" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GoogleSearchRetrieval",
    )
    code_execution: "CodeExecution" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CodeExecution",
    )
    google_search: GoogleSearch = proto.Field(
        proto.MESSAGE,
        number=4,
        message=GoogleSearch,
    )
    computer_use: ComputerUse = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ComputerUse,
    )
    url_context: "UrlContext" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="UrlContext",
    )
    file_search: "FileSearch" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="FileSearch",
    )
    google_maps: "GoogleMaps" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="GoogleMaps",
    )


class GoogleMaps(proto.Message):
    r"""The GoogleMaps Tool that provides geospatial context for the
    user's query.

    Attributes:
        enable_widget (bool):
            Optional. Whether to return a widget context
            token in the GroundingMetadata of the response.
            Developers can use the widget context token to
            render a Google Maps widget with geospatial
            context related to the places that the model
            references in the response.
    """

    enable_widget: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class UrlContext(proto.Message):
    r"""Tool to support URL context retrieval."""


class FileSearch(proto.Message):
    r"""The FileSearch tool that retrieves knowledge from Semantic
    Retrieval corpora. Files are imported to Semantic Retrieval
    corpora using the ImportFile API.

    Attributes:
        retrieval_resources (MutableSequence[google.ai.generativelanguage_v1beta.types.FileSearch.RetrievalResource]):
            Required. Semantic retrieval resources to
            retrieve from. Currently only supports one
            corpus. In the future we may open up multiple
            corpora support.
        retrieval_config (google.ai.generativelanguage_v1beta.types.FileSearch.RetrievalConfig):
            Optional. The configuration for the
            retrieval.
    """

    class RetrievalResource(proto.Message):
        r"""The semantic retrieval resource to retrieve from.

        Attributes:
            rag_store_name (str):
                Required. The name of the semantic retrieval resource to
                retrieve from. Example: ``ragStores/my-rag-store-123``
        """

        rag_store_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RetrievalConfig(proto.Message):
        r"""Semantic retrieval configuration.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            top_k (int):
                Optional. The number of semantic retrieval
                chunks to retrieve.

                This field is a member of `oneof`_ ``_top_k``.
            metadata_filter (str):
                Optional. Metadata filter to apply to the
                semantic retrieval documents and chunks.
        """

        top_k: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        metadata_filter: str = proto.Field(
            proto.STRING,
            number=3,
        )

    retrieval_resources: MutableSequence[RetrievalResource] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RetrievalResource,
    )
    retrieval_config: RetrievalConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RetrievalConfig,
    )


class GoogleSearchRetrieval(proto.Message):
    r"""Tool to retrieve public web data for grounding, powered by
    Google.

    Attributes:
        dynamic_retrieval_config (google.ai.generativelanguage_v1beta.types.DynamicRetrievalConfig):
            Specifies the dynamic retrieval configuration
            for the given source.
    """

    dynamic_retrieval_config: "DynamicRetrievalConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DynamicRetrievalConfig",
    )


class DynamicRetrievalConfig(proto.Message):
    r"""Describes the options to customize dynamic retrieval.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        mode (google.ai.generativelanguage_v1beta.types.DynamicRetrievalConfig.Mode):
            The mode of the predictor to be used in
            dynamic retrieval.
        dynamic_threshold (float):
            The threshold to be used in dynamic
            retrieval. If not set, a system default value is
            used.

            This field is a member of `oneof`_ ``_dynamic_threshold``.
    """

    class Mode(proto.Enum):
        r"""The mode of the predictor to be used in dynamic retrieval.

        Values:
            MODE_UNSPECIFIED (0):
                Always trigger retrieval.
            MODE_DYNAMIC (1):
                Run retrieval only when system decides it is
                necessary.
        """

        MODE_UNSPECIFIED = 0
        MODE_DYNAMIC = 1

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    dynamic_threshold: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )


class CodeExecution(proto.Message):
    r"""Tool that executes code generated by the model, and automatically
    returns the result to the model.

    See also ``ExecutableCode`` and ``CodeExecutionResult`` which are
    only generated when using this tool.

    """


class ToolConfig(proto.Message):
    r"""The Tool configuration containing parameters for specifying ``Tool``
    use in the request.

    Attributes:
        function_calling_config (google.ai.generativelanguage_v1beta.types.FunctionCallingConfig):
            Optional. Function calling config.
        retrieval_config (google.ai.generativelanguage_v1beta.types.RetrievalConfig):
            Optional. Retrieval config.
    """

    function_calling_config: "FunctionCallingConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FunctionCallingConfig",
    )
    retrieval_config: "RetrievalConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RetrievalConfig",
    )


class RetrievalConfig(proto.Message):
    r"""Retrieval config.

    Attributes:
        lat_lng (google.type.latlng_pb2.LatLng):
            Optional. The location of the user.
        language_code (str):
            Optional. The language code of the user. Language code for
            content. Use language tags defined by
            `BCP47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__.
    """

    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FunctionCallingConfig(proto.Message):
    r"""Configuration for specifying function calling behavior.

    Attributes:
        mode (google.ai.generativelanguage_v1beta.types.FunctionCallingConfig.Mode):
            Optional. Specifies the mode in which
            function calling should execute. If unspecified,
            the default value will be set to AUTO.
        allowed_function_names (MutableSequence[str]):
            Optional. A set of function names that, when provided,
            limits the functions the model will call.

            This should only be set when the Mode is ANY or VALIDATED.
            Function names should match [FunctionDeclaration.name]. When
            set, model will predict a function call from only allowed
            function names.
    """

    class Mode(proto.Enum):
        r"""Defines the execution behavior for function calling by
        defining the execution mode.

        Values:
            MODE_UNSPECIFIED (0):
                Unspecified function calling mode. This value
                should not be used.
            AUTO (1):
                Default model behavior, model decides to
                predict either a function call or a natural
                language response.
            ANY (2):
                Model is constrained to always predicting a function call
                only. If "allowed_function_names" are set, the predicted
                function call will be limited to any one of
                "allowed_function_names", else the predicted function call
                will be any one of the provided "function_declarations".
            NONE (3):
                Model will not predict any function call.
                Model behavior is same as when not passing any
                function declarations.
            VALIDATED (4):
                Model decides to predict either a function call or a natural
                language response, but will validate function calls with
                constrained decoding. If "allowed_function_names" are set,
                the predicted function call will be limited to any one of
                "allowed_function_names", else the predicted function call
                will be any one of the provided "function_declarations".
        """

        MODE_UNSPECIFIED = 0
        AUTO = 1
        ANY = 2
        NONE = 3
        VALIDATED = 4

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    allowed_function_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class FunctionDeclaration(proto.Message):
    r"""Structured representation of a function declaration as defined by
    the `OpenAPI 3.03
    specification <https://spec.openapis.org/oas/v3.0.3>`__. Included in
    this declaration are the function name and parameters. This
    FunctionDeclaration is a representation of a block of code that can
    be used as a ``Tool`` by the model and executed by the client.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the function.
            Must be a-z, A-Z, 0-9, or contain underscores,
            colons, dots, and dashes, with a maximum length
            of 64.
        description (str):
            Required. A brief description of the
            function.
        parameters (google.ai.generativelanguage_v1beta.types.Schema):
            Optional. Describes the parameters to this
            function. Reflects the Open API 3.03 Parameter
            Object string Key: the name of the parameter.
            Parameter names are case sensitive. Schema
            Value: the Schema defining the type used for the
            parameter.

            This field is a member of `oneof`_ ``_parameters``.
        parameters_json_schema (google.protobuf.struct_pb2.Value):
            Optional. Describes the parameters to the function in JSON
            Schema format. The schema must describe an object where the
            properties are the parameters to the function. For example:

            ::

               {
                 "type": "object",
                 "properties": {
                   "name": { "type": "string" },
                   "age": { "type": "integer" }
                 },
                 "additionalProperties": false,
                 "required": ["name", "age"],
                 "propertyOrdering": ["name", "age"]
               }

            This field is mutually exclusive with ``parameters``.

            This field is a member of `oneof`_ ``_parameters_json_schema``.
        response (google.ai.generativelanguage_v1beta.types.Schema):
            Optional. Describes the output from this
            function in JSON Schema format. Reflects the
            Open API 3.03 Response Object. The Schema
            defines the type used for the response value of
            the function.

            This field is a member of `oneof`_ ``_response``.
        response_json_schema (google.protobuf.struct_pb2.Value):
            Optional. Describes the output from this function in JSON
            Schema format. The value specified by the schema is the
            response value of the function.

            This field is mutually exclusive with ``response``.

            This field is a member of `oneof`_ ``_response_json_schema``.
        behavior (google.ai.generativelanguage_v1beta.types.FunctionDeclaration.Behavior):
            Optional. Specifies the function Behavior.
            Currently only supported by the
            BidiGenerateContent method.
    """

    class Behavior(proto.Enum):
        r"""Defines the function behavior. Defaults to ``BLOCKING``.

        Values:
            UNSPECIFIED (0):
                This value is unused.
            BLOCKING (1):
                If set, the system will wait to receive the
                function response before continuing the
                conversation.
            NON_BLOCKING (2):
                If set, the system will not wait to receive
                the function response. Instead, it will attempt
                to handle function responses as they become
                available while maintaining the conversation
                between the user and the model.
        """

        UNSPECIFIED = 0
        BLOCKING = 1
        NON_BLOCKING = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: "Schema" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="Schema",
    )
    parameters_json_schema: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=struct_pb2.Value,
    )
    response: "Schema" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="Schema",
    )
    response_json_schema: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=struct_pb2.Value,
    )
    behavior: Behavior = proto.Field(
        proto.ENUM,
        number=5,
        enum=Behavior,
    )


class FunctionCall(proto.Message):
    r"""A predicted ``FunctionCall`` returned from the model that contains a
    string representing the ``FunctionDeclaration.name`` with the
    arguments and their values.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Optional. The unique id of the function call. If populated,
            the client to execute the ``function_call`` and return the
            response with the matching ``id``.
        name (str):
            Required. The name of the function to call.
            Must be a-z, A-Z, 0-9, or contain underscores
            and dashes, with a maximum length of 64.
        args (google.protobuf.struct_pb2.Struct):
            Optional. The function parameters and values
            in JSON object format.

            This field is a member of `oneof`_ ``_args``.
    """

    id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    args: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=struct_pb2.Struct,
    )


class FunctionResponse(proto.Message):
    r"""The result output from a ``FunctionCall`` that contains a string
    representing the ``FunctionDeclaration.name`` and a structured JSON
    object containing any output from the function is used as context to
    the model. This should contain the result of a\ ``FunctionCall``
    made based on model prediction.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Optional. The id of the function call this response is for.
            Populated by the client to match the corresponding function
            call ``id``.
        name (str):
            Required. The name of the function to call.
            Must be a-z, A-Z, 0-9, or contain underscores
            and dashes, with a maximum length of 64.
        response (google.protobuf.struct_pb2.Struct):
            Required. The function response in JSON
            object format. Callers can use any keys of their
            choice that fit the function's syntax to return
            the function output, e.g. "output", "result",
            etc. In particular, if the function call failed
            to execute, the response can have an "error" key
            to return error details to the model.
        parts (MutableSequence[google.ai.generativelanguage_v1beta.types.FunctionResponsePart]):
            Optional. Ordered ``Parts`` that constitute a function
            response. Parts may have different IANA MIME types.
        will_continue (bool):
            Optional. Signals that function call continues, and more
            responses will be returned, turning the function call into a
            generator. Is only applicable to NON_BLOCKING function
            calls, is ignored otherwise. If set to false, future
            responses will not be considered. It is allowed to return
            empty ``response`` with ``will_continue=False`` to signal
            that the function call is finished. This may still trigger
            the model generation. To avoid triggering the generation and
            finish the function call, additionally set ``scheduling`` to
            ``SILENT``.
        scheduling (google.ai.generativelanguage_v1beta.types.FunctionResponse.Scheduling):
            Optional. Specifies how the response should be scheduled in
            the conversation. Only applicable to NON_BLOCKING function
            calls, is ignored otherwise. Defaults to WHEN_IDLE.

            This field is a member of `oneof`_ ``_scheduling``.
    """

    class Scheduling(proto.Enum):
        r"""Specifies how the response should be scheduled in the
        conversation.

        Values:
            SCHEDULING_UNSPECIFIED (0):
                This value is unused.
            SILENT (1):
                Only add the result to the conversation
                context, do not interrupt or trigger generation.
            WHEN_IDLE (2):
                Add the result to the conversation context,
                and prompt to generate output without
                interrupting ongoing generation.
            INTERRUPT (3):
                Add the result to the conversation context,
                interrupt ongoing generation and prompt to
                generate output.
        """

        SCHEDULING_UNSPECIFIED = 0
        SILENT = 1
        WHEN_IDLE = 2
        INTERRUPT = 3

    id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    parts: MutableSequence["FunctionResponsePart"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="FunctionResponsePart",
    )
    will_continue: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    scheduling: Scheduling = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=Scheduling,
    )


class Schema(proto.Message):
    r"""The ``Schema`` object allows the definition of input and output data
    types. These types can be objects, but also primitives and arrays.
    Represents a select subset of an `OpenAPI 3.0 schema
    object <https://spec.openapis.org/oas/v3.0.3#schema>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.ai.generativelanguage_v1beta.types.Type):
            Required. Data type.
        format_ (str):
            Optional. The format of the data. Any value
            is allowed, but most do not trigger any special
            functionality.
        title (str):
            Optional. The title of the schema.
        description (str):
            Optional. A brief description of the
            parameter. This could contain examples of use.
            Parameter description may be formatted as
            Markdown.
        nullable (bool):
            Optional. Indicates if the value may be null.
        enum (MutableSequence[str]):
            Optional. Possible values of the element of Type.STRING with
            enum format. For example we can define an Enum Direction as
            : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH",
            "WEST"]}
        items (google.ai.generativelanguage_v1beta.types.Schema):
            Optional. Schema of the elements of
            Type.ARRAY.

            This field is a member of `oneof`_ ``_items``.
        max_items (int):
            Optional. Maximum number of the elements for
            Type.ARRAY.
        min_items (int):
            Optional. Minimum number of the elements for
            Type.ARRAY.
        properties (MutableMapping[str, google.ai.generativelanguage_v1beta.types.Schema]):
            Optional. Properties of Type.OBJECT.
        required (MutableSequence[str]):
            Optional. Required properties of Type.OBJECT.
        min_properties (int):
            Optional. Minimum number of the properties
            for Type.OBJECT.
        max_properties (int):
            Optional. Maximum number of the properties
            for Type.OBJECT.
        minimum (float):
            Optional. SCHEMA FIELDS FOR TYPE INTEGER and
            NUMBER Minimum value of the Type.INTEGER and
            Type.NUMBER

            This field is a member of `oneof`_ ``_minimum``.
        maximum (float):
            Optional. Maximum value of the Type.INTEGER
            and Type.NUMBER

            This field is a member of `oneof`_ ``_maximum``.
        min_length (int):
            Optional. SCHEMA FIELDS FOR TYPE STRING
            Minimum length of the Type.STRING
        max_length (int):
            Optional. Maximum length of the Type.STRING
        pattern (str):
            Optional. Pattern of the Type.STRING to
            restrict a string to a regular expression.
        example (google.protobuf.struct_pb2.Value):
            Optional. Example of the object. Will only
            populated when the object is the root.
        any_of (MutableSequence[google.ai.generativelanguage_v1beta.types.Schema]):
            Optional. The value should be validated
            against any (one or more) of the subschemas in
            the list.
        property_ordering (MutableSequence[str]):
            Optional. The order of the properties.
            Not a standard field in open api spec. Used to
            determine the order of the properties in the
            response.
        default (google.protobuf.struct_pb2.Value):
            Optional. Default value of the field. Per JSON Schema, this
            field is intended for documentation generators and doesn't
            affect validation. Thus it's included here and ignored so
            that developers who send schemas with a ``default`` field
            don't get unknown-field errors.
    """

    type_: "Type" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Type",
    )
    format_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    title: str = proto.Field(
        proto.STRING,
        number=24,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    enum: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    items: "Schema" = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message="Schema",
    )
    max_items: int = proto.Field(
        proto.INT64,
        number=21,
    )
    min_items: int = proto.Field(
        proto.INT64,
        number=22,
    )
    properties: MutableMapping[str, "Schema"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message="Schema",
    )
    required: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    min_properties: int = proto.Field(
        proto.INT64,
        number=9,
    )
    max_properties: int = proto.Field(
        proto.INT64,
        number=10,
    )
    minimum: float = proto.Field(
        proto.DOUBLE,
        number=11,
        optional=True,
    )
    maximum: float = proto.Field(
        proto.DOUBLE,
        number=12,
        optional=True,
    )
    min_length: int = proto.Field(
        proto.INT64,
        number=13,
    )
    max_length: int = proto.Field(
        proto.INT64,
        number=14,
    )
    pattern: str = proto.Field(
        proto.STRING,
        number=15,
    )
    example: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=16,
        message=struct_pb2.Value,
    )
    any_of: MutableSequence["Schema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message="Schema",
    )
    property_ordering: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )
    default: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=25,
        message=struct_pb2.Value,
    )


class GroundingPassage(proto.Message):
    r"""Passage included inline with a grounding configuration.

    Attributes:
        id (str):
            Identifier for the passage for attributing
            this passage in grounded answers.
        content (google.ai.generativelanguage_v1beta.types.Content):
            Content of the passage.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: "Content" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Content",
    )


class GroundingPassages(proto.Message):
    r"""A repeated list of passages.

    Attributes:
        passages (MutableSequence[google.ai.generativelanguage_v1beta.types.GroundingPassage]):
            List of passages.
    """

    passages: MutableSequence["GroundingPassage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GroundingPassage",
    )


class ModalityTokenCount(proto.Message):
    r"""Represents token counting info for a single modality.

    Attributes:
        modality (google.ai.generativelanguage_v1beta.types.Modality):
            The modality associated with this token
            count.
        token_count (int):
            Number of tokens.
    """

    modality: "Modality" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Modality",
    )
    token_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
