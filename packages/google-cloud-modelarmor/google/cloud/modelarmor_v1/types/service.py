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
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.modelarmor.v1",
    manifest={
        "FilterMatchState",
        "FilterExecutionState",
        "RaiFilterType",
        "DetectionConfidenceLevel",
        "SdpFindingLikelihood",
        "InvocationResult",
        "StreamingMode",
        "Modality",
        "FilterVersionAlias",
        "MatchingScope",
        "RuleFilterType",
        "FilterVersionSelector",
        "Template",
        "FloorSetting",
        "McpServerFloorSetting",
        "AiPlatformFloorSetting",
        "ListTemplatesRequest",
        "ListTemplatesResponse",
        "GetTemplateRequest",
        "CreateTemplateRequest",
        "UpdateTemplateRequest",
        "DeleteTemplateRequest",
        "GetFloorSettingRequest",
        "UpdateFloorSettingRequest",
        "FilterConfig",
        "PiAndJailbreakFilterSettings",
        "MaliciousUriFilterSettings",
        "RaiFilterSettings",
        "SdpFilterSettings",
        "SdpBasicConfig",
        "SdpAdvancedConfig",
        "SanitizeUserPromptRequest",
        "SanitizeModelResponseRequest",
        "SanitizeUserPromptResponse",
        "SanitizeModelResponseResponse",
        "FilterVersionConfig",
        "SanitizationResult",
        "MultiLanguageDetectionMetadata",
        "FilterResult",
        "RaiFilterResult",
        "SdpFilterResult",
        "SdpInspectResult",
        "DataItem",
        "ByteDataItem",
        "SdpDeidentifyResult",
        "SdpImageFindingLocation",
        "SdpContentLocation",
        "SdpFinding",
        "SdpRedactResult",
        "WordList",
        "Dictionary",
        "Regex",
        "ExclusionRule",
        "FilterRule",
        "FilterRuleSet",
        "FilterRuleSettings",
        "PiAndJailbreakFilterResult",
        "MaliciousUriFilterResult",
        "VirusScanFilterResult",
        "VirusDetail",
        "CsamFilterResult",
        "MessageItem",
        "RangeInfo",
    },
)


class FilterMatchState(proto.Enum):
    r"""Option to specify filter match state.

    Values:
        FILTER_MATCH_STATE_UNSPECIFIED (0):
            Unused
        NO_MATCH_FOUND (1):
            Matching criteria is not achieved for
            filters.
        MATCH_FOUND (2):
            Matching criteria is achieved for the filter.
    """

    FILTER_MATCH_STATE_UNSPECIFIED = 0
    NO_MATCH_FOUND = 1
    MATCH_FOUND = 2


class FilterExecutionState(proto.Enum):
    r"""Enum which reports whether a specific filter executed
    successfully or not.

    Values:
        FILTER_EXECUTION_STATE_UNSPECIFIED (0):
            Unused
        EXECUTION_SUCCESS (1):
            Filter executed successfully
        EXECUTION_SKIPPED (2):
            Filter execution was skipped. This can happen
            due to server-side error or permission issue.
    """

    FILTER_EXECUTION_STATE_UNSPECIFIED = 0
    EXECUTION_SUCCESS = 1
    EXECUTION_SKIPPED = 2


class RaiFilterType(proto.Enum):
    r"""Options for responsible AI Filter Types.

    Values:
        RAI_FILTER_TYPE_UNSPECIFIED (0):
            Unspecified filter type.
        SEXUALLY_EXPLICIT (2):
            Sexually Explicit.
        HATE_SPEECH (3):
            Hate Speech.
        HARASSMENT (6):
            Harassment.
        DANGEROUS (17):
            Danger
    """

    RAI_FILTER_TYPE_UNSPECIFIED = 0
    SEXUALLY_EXPLICIT = 2
    HATE_SPEECH = 3
    HARASSMENT = 6
    DANGEROUS = 17


class DetectionConfidenceLevel(proto.Enum):
    r"""Confidence levels for detectors.
    Higher value maps to a greater confidence level. To enforce
    stricter level a lower value should be used.

    Values:
        DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED (0):
            Same as LOW_AND_ABOVE.
        LOW_AND_ABOVE (1):
            Highest chance of a false positive.
        MEDIUM_AND_ABOVE (2):
            Some chance of false positives.
        HIGH (3):
            Low chance of false positives.
    """

    DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED = 0
    LOW_AND_ABOVE = 1
    MEDIUM_AND_ABOVE = 2
    HIGH = 3


class SdpFindingLikelihood(proto.Enum):
    r"""For more information about each Sensitive Data Protection
    likelihood level, see
    https://cloud.google.com/sensitive-data-protection/docs/likelihood.

    Values:
        SDP_FINDING_LIKELIHOOD_UNSPECIFIED (0):
            Default value; same as POSSIBLE.
        VERY_UNLIKELY (1):
            Highest chance of a false positive.
        UNLIKELY (2):
            High chance of a false positive.
        POSSIBLE (3):
            Some matching signals. The default value.
        LIKELY (4):
            Low chance of a false positive.
        VERY_LIKELY (5):
            Confidence level is high. Lowest chance of a
            false positive.
    """

    SDP_FINDING_LIKELIHOOD_UNSPECIFIED = 0
    VERY_UNLIKELY = 1
    UNLIKELY = 2
    POSSIBLE = 3
    LIKELY = 4
    VERY_LIKELY = 5


class InvocationResult(proto.Enum):
    r"""A field indicating the outcome of the invocation,
    irrespective of match status.

    Values:
        INVOCATION_RESULT_UNSPECIFIED (0):
            Unused. Default value.
        SUCCESS (1):
            All filters were invoked successfully.
        PARTIAL (2):
            Some filters were skipped or failed.
        FAILURE (3):
            All filters were skipped or failed.
    """

    INVOCATION_RESULT_UNSPECIFIED = 0
    SUCCESS = 1
    PARTIAL = 2
    FAILURE = 3


class StreamingMode(proto.Enum):
    r"""Streaming Mode for Sanitize\* API.

    Values:
        STREAMING_MODE_UNSPECIFIED (0):
            Default value.
        STREAMING_MODE_BUFFERED (1):
            Buffered Streaming mode.
        STREAMING_MODE_REALTIME (2):
            Real Time Streaming mode.
    """

    STREAMING_MODE_UNSPECIFIED = 0
    STREAMING_MODE_BUFFERED = 1
    STREAMING_MODE_REALTIME = 2


class Modality(proto.Enum):
    r"""This enum is used in the TemplateMetadata and
    FloorSettingMetadata messages to indicate the modality supported
    for sanitize API calls.

    Values:
        MODALITY_UNSPECIFIED (0):
            Unspecified modality. If specified, all
            modalities will be sanitized.
        MODALITY_TEXT (1):
            Represents text modality. If specified, it
            will sanitize text fields, and text extracted
            from rich text files (like PDFs, DOCs) and plain
            text files (like TXT).
        MODALITY_IMAGE (2):
            Represents image modality. If specified, it
            will sanitize image files. The visual content
            and the text content in the image will be
            sanitized depending on the filter configuration.
    """

    MODALITY_UNSPECIFIED = 0
    MODALITY_TEXT = 1
    MODALITY_IMAGE = 2


class FilterVersionAlias(proto.Enum):
    r"""Enum for Filter Version Aliases.
    These aliases provide a way to always point to a specific track
    without needing to update the version in templates.

    Values:
        FILTER_VERSION_ALIAS_UNSPECIFIED (0):
            The default value. If used, it will resolve to the
            ``STABLE`` alias.
        FILTER_VERSION_ALIAS_STABLE (1):
            ``STABLE`` alias points to the most recent stable model
            version. Using this alias means no code changes are required
            when a new model becomes the stable version.
        FILTER_VERSION_ALIAS_LATEST (2):
            ``LATEST`` alias points to the newest model version
            available. This version is subject to frequent revisions and
            offers SLO guarantees but does not assure stability,
            providing the most current security protections.
        FILTER_VERSION_ALIAS_LEGACY (3):
            ``LEGACY`` alias could be used for sanitization operations
            for a transition period. New templates cannot be created
            with this version.
        FILTER_VERSION_ALIAS_RETIRED (4):
            ``RETIRED`` alias could be used for versions that are no
            longer available to be used. While new templates cannot be
            created with this alias, any existing template or request
            using ``RETIRED`` version will fall back to the current
            ``STABLE`` version for sanitization operations.
    """

    FILTER_VERSION_ALIAS_UNSPECIFIED = 0
    FILTER_VERSION_ALIAS_STABLE = 1
    FILTER_VERSION_ALIAS_LATEST = 2
    FILTER_VERSION_ALIAS_LEGACY = 3
    FILTER_VERSION_ALIAS_RETIRED = 4


class MatchingScope(proto.Enum):
    r"""Defines the scope of the match for a rule.

    Additional values may be added to this enum in the future.

    Values:
        MATCHING_SCOPE_UNSPECIFIED (0):
            Unspecified matching scope.
        MATCHING_SCOPE_FULL_MATCH (1):
            Full match.

            - Dictionary: the dictionary match covers the
              entire input content
            - Regular expression: the regular expression
              pattern matches the entire input content
        MATCHING_SCOPE_PARTIAL_MATCH (2):
            Partial match.

            - Dictionary: at least one of the tokens in the
              input content matches
            - Regular expression: substring of the input
              content matches the regular expression pattern
    """

    MATCHING_SCOPE_UNSPECIFIED = 0
    MATCHING_SCOPE_FULL_MATCH = 1
    MATCHING_SCOPE_PARTIAL_MATCH = 2


class RuleFilterType(proto.Enum):
    r"""Model Armor Filter types supported for rules.

    Values:
        RULE_FILTER_TYPE_UNSPECIFIED (0):
            Unspecified filter type.
        PROMPT_INJECTION_AND_JAILBREAK (1):
            Prompt injection and jailbreak filter.
        RESPONSIBLE_AI (2):
            Responsible AI filter.
    """

    RULE_FILTER_TYPE_UNSPECIFIED = 0
    PROMPT_INJECTION_AND_JAILBREAK = 1
    RESPONSIBLE_AI = 2


class FilterVersionSelector(proto.Message):
    r"""Represents the configuration for selecting a Filter Version.
    Allows customers to choose to use either a specific version or a
    predefined alias.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        version (str):
            Allows customers to pin to a specific, immutable Filter
            Version. This provides stability, as this will not change
            after a version upgrade. Expected format is a case-sensitive
            string, e.g., "v1", "v2". Requests providing an invalid or
            non-existent version string will be rejected with an
            ``INVALID_ARGUMENT`` error.

            This field is a member of `oneof`_ ``version_spec``.
        alias (google.cloud.modelarmor_v1.types.FilterVersionAlias):
            Allows customers to use a predefined alias
            that dynamically points to a specific version
            based on internal upgrades. This offers
            flexibility and reduces the need for template
            updates.

            This field is a member of `oneof`_ ``version_spec``.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="version_spec",
    )
    alias: "FilterVersionAlias" = proto.Field(
        proto.ENUM,
        number=2,
        oneof="version_spec",
        enum="FilterVersionAlias",
    )


class Template(proto.Message):
    r"""Message describing Template resource

    Attributes:
        name (str):
            Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        filter_config (google.cloud.modelarmor_v1.types.FilterConfig):
            Required. filter configuration for this
            template
        template_metadata (google.cloud.modelarmor_v1.types.Template.TemplateMetadata):
            Optional. metadata for this template
    """

    class TemplateMetadata(proto.Message):
        r"""Message describing TemplateMetadata

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            ignore_partial_invocation_failures (bool):
                Optional. If true, partial detector failures
                should be ignored.
            custom_prompt_safety_error_code (int):
                Optional. Indicates the custom error code set
                by the user to be returned to the end user by
                the service extension if the prompt trips Model
                Armor filters.
            custom_prompt_safety_error_message (str):
                Optional. Indicates the custom error message
                set by the user to be returned to the end user
                if the prompt trips Model Armor filters.
            custom_llm_response_safety_error_code (int):
                Optional. Indicates the custom error code set
                by the user to be returned to the end user if
                the LLM response trips Model Armor filters.
            custom_llm_response_safety_error_message (str):
                Optional. Indicates the custom error message
                set by the user to be returned to the end user
                if the LLM response trips Model Armor filters.
            log_template_operations (bool):
                Optional. If true, log template crud
                operations.
            log_sanitize_operations (bool):
                Optional. If true, log sanitize operations.
            enforcement_type (google.cloud.modelarmor_v1.types.Template.TemplateMetadata.EnforcementType):
                Optional. Enforcement type for Model Armor
                filters.
            multi_language_detection (google.cloud.modelarmor_v1.types.Template.TemplateMetadata.MultiLanguageDetection):
                Optional. Metadata for multi language
                detection.
            filter_version_selector (google.cloud.modelarmor_v1.types.FilterVersionSelector):
                Optional. Specifies the configuration for the Filter version
                to be used. If this field is populated, it takes precedence
                over any values set in the deprecated ``filter_version``
                fields within ``RaiFilterSettings``,
                ``PiAndJailbreakFilterSettings``.

                This field is a member of `oneof`_ ``_filter_version_selector``.
            modalities (MutableSequence[google.cloud.modelarmor_v1.types.Modality]):
                Optional. Specifies the modalities to scan.
                If not specified or empty, only text modality
                will be scanned.
            data_residency_compliant (bool):
                Optional. Indicates whether the template is
                subject to data residency compliance. If true
                (default for new templates), the template is
                subject to data residency compliance. If false,
                the template bypasses data residency compliance
                checks.

                This field is a member of `oneof`_ ``_data_residency_compliant``.
        """

        class EnforcementType(proto.Enum):
            r"""Enforcement type for Model Armor filters.

            Values:
                ENFORCEMENT_TYPE_UNSPECIFIED (0):
                    Default value. Same as INSPECT_AND_BLOCK.
                INSPECT_ONLY (1):
                    Model Armor filters will run in inspect only
                    mode. No action will be taken on the request.
                INSPECT_AND_BLOCK (2):
                    Model Armor filters will run in inspect and
                    block mode. Requests that trip Model Armor
                    filters will be blocked.
            """

            ENFORCEMENT_TYPE_UNSPECIFIED = 0
            INSPECT_ONLY = 1
            INSPECT_AND_BLOCK = 2

        class MultiLanguageDetection(proto.Message):
            r"""Metadata to enable multi language detection via template.

            Attributes:
                enable_multi_language_detection (bool):
                    Required. If true, multi language detection
                    will be enabled.
            """

            enable_multi_language_detection: bool = proto.Field(
                proto.BOOL,
                number=1,
            )

        ignore_partial_invocation_failures: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        custom_prompt_safety_error_code: int = proto.Field(
            proto.INT32,
            number=2,
        )
        custom_prompt_safety_error_message: str = proto.Field(
            proto.STRING,
            number=3,
        )
        custom_llm_response_safety_error_code: int = proto.Field(
            proto.INT32,
            number=4,
        )
        custom_llm_response_safety_error_message: str = proto.Field(
            proto.STRING,
            number=5,
        )
        log_template_operations: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        log_sanitize_operations: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        enforcement_type: "Template.TemplateMetadata.EnforcementType" = proto.Field(
            proto.ENUM,
            number=8,
            enum="Template.TemplateMetadata.EnforcementType",
        )
        multi_language_detection: "Template.TemplateMetadata.MultiLanguageDetection" = (
            proto.Field(
                proto.MESSAGE,
                number=9,
                message="Template.TemplateMetadata.MultiLanguageDetection",
            )
        )
        filter_version_selector: "FilterVersionSelector" = proto.Field(
            proto.MESSAGE,
            number=10,
            optional=True,
            message="FilterVersionSelector",
        )
        modalities: MutableSequence["Modality"] = proto.RepeatedField(
            proto.ENUM,
            number=11,
            enum="Modality",
        )
        data_residency_compliant: bool = proto.Field(
            proto.BOOL,
            number=12,
            optional=True,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    filter_config: "FilterConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FilterConfig",
    )
    template_metadata: TemplateMetadata = proto.Field(
        proto.MESSAGE,
        number=6,
        message=TemplateMetadata,
    )


class FloorSetting(proto.Message):
    r"""Message describing FloorSetting resource

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create timestamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update timestamp
        filter_config (google.cloud.modelarmor_v1.types.FilterConfig):
            Required. ModelArmor filter configuration.
        enable_floor_setting_enforcement (bool):
            Optional. Floor Settings enforcement status.

            This field is a member of `oneof`_ ``_enable_floor_setting_enforcement``.
        integrated_services (MutableSequence[google.cloud.modelarmor_v1.types.FloorSetting.IntegratedService]):
            Optional. List of integrated services for
            which the floor setting is applicable.
        ai_platform_floor_setting (google.cloud.modelarmor_v1.types.AiPlatformFloorSetting):
            Optional. AI Platform floor setting.

            This field is a member of `oneof`_ ``_ai_platform_floor_setting``.
        floor_setting_metadata (google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata):
            Optional. Metadata for FloorSetting
        google_mcp_server_floor_setting (google.cloud.modelarmor_v1.types.McpServerFloorSetting):
            Optional. Google MCP Server floor setting.

            This field is a member of `oneof`_ ``_google_mcp_server_floor_setting``.
    """

    class IntegratedService(proto.Enum):
        r"""Integrated service for which the floor setting is applicable.

        Values:
            INTEGRATED_SERVICE_UNSPECIFIED (0):
                Unspecified integrated service.
            AI_PLATFORM (1):
                AI Platform.
            GOOGLE_MCP_SERVER (2):
                Google MCP Server (via Shim Service
                Extension)
        """

        INTEGRATED_SERVICE_UNSPECIFIED = 0
        AI_PLATFORM = 1
        GOOGLE_MCP_SERVER = 2

    class FloorSettingMetadata(proto.Message):
        r"""message describing FloorSetting Metadata

        Attributes:
            multi_language_detection (google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata.MultiLanguageDetection):
                Optional. Metadata for multi language
                detection.
        """

        class MultiLanguageDetection(proto.Message):
            r"""Metadata to enable multi language detection via floor
            setting.

            Attributes:
                enable_multi_language_detection (bool):
                    Required. If true, multi language detection
                    will be enabled.
            """

            enable_multi_language_detection: bool = proto.Field(
                proto.BOOL,
                number=1,
            )

        multi_language_detection: "FloorSetting.FloorSettingMetadata.MultiLanguageDetection" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="FloorSetting.FloorSettingMetadata.MultiLanguageDetection",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    filter_config: "FilterConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="FilterConfig",
    )
    enable_floor_setting_enforcement: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    integrated_services: MutableSequence[IntegratedService] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=IntegratedService,
    )
    ai_platform_floor_setting: "AiPlatformFloorSetting" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="AiPlatformFloorSetting",
    )
    floor_setting_metadata: FloorSettingMetadata = proto.Field(
        proto.MESSAGE,
        number=8,
        message=FloorSettingMetadata,
    )
    google_mcp_server_floor_setting: "McpServerFloorSetting" = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message="McpServerFloorSetting",
    )


class McpServerFloorSetting(proto.Message):
    r"""Message describing MCP Server Floor Setting.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inspect_only (bool):
            Optional. If true, Model Armor filters will
            be run in inspect only mode. No action will be
            taken on the request.

            This field is a member of `oneof`_ ``enforcement_type``.
        inspect_and_block (bool):
            Optional. If true, Model Armor filters will
            be run in inspect and block mode. Requests that
            trip Model Armor filters will be blocked.

            This field is a member of `oneof`_ ``enforcement_type``.
        enable_cloud_logging (bool):
            Optional. If true, log Model Armor filter
            results to Cloud Logging.
    """

    inspect_only: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="enforcement_type",
    )
    inspect_and_block: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="enforcement_type",
    )
    enable_cloud_logging: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class AiPlatformFloorSetting(proto.Message):
    r"""message describing AiPlatformFloorSetting

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inspect_only (bool):
            Optional. If true, Model Armor filters will
            be run in inspect only mode. No action will be
            taken on the request.

            This field is a member of `oneof`_ ``enforcement_type``.
        inspect_and_block (bool):
            Optional. If true, Model Armor filters will
            be run in inspect and block mode. Requests that
            trip Model Armor filters will be blocked.

            This field is a member of `oneof`_ ``enforcement_type``.
        enable_cloud_logging (bool):
            Optional. If true, log Model Armor filter
            results to Cloud Logging.
    """

    inspect_only: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="enforcement_type",
    )
    inspect_and_block: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="enforcement_type",
    )
    enable_cloud_logging: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListTemplatesRequest(proto.Message):
    r"""Message for requesting list of Templates

    Attributes:
        parent (str):
            Required. Parent value for
            ListTemplatesRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListTemplatesResponse(proto.Message):
    r"""Message for response to listing Templates

    Attributes:
        templates (MutableSequence[google.cloud.modelarmor_v1.types.Template]):
            The list of Template
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    templates: MutableSequence["Template"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Template",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTemplateRequest(proto.Message):
    r"""Message for getting a Template

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTemplateRequest(proto.Message):
    r"""Message for creating a Template

    Attributes:
        parent (str):
            Required. Value for parent.
        template_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and template_id from the
            method_signature of Create RPC
        template (google.cloud.modelarmor_v1.types.Template):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server stores the request ID
            for 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    template: "Template" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Template",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateTemplateRequest(proto.Message):
    r"""Message for updating a Template

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Template resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        template (google.cloud.modelarmor_v1.types.Template):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server stores the request ID
            for 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    template: "Template" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Template",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTemplateRequest(proto.Message):
    r"""Message for deleting a Template

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server stores the request ID
            for 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFloorSettingRequest(proto.Message):
    r"""Message for getting a Floor Setting

    Attributes:
        name (str):
            Required. The name of the floor setting to
            get, example projects/123/floorsetting.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFloorSettingRequest(proto.Message):
    r"""Message for Updating a Floor Setting

    Attributes:
        floor_setting (google.cloud.modelarmor_v1.types.FloorSetting):
            Required. The floor setting being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the FloorSetting resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
    """

    floor_setting: "FloorSetting" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FloorSetting",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class FilterConfig(proto.Message):
    r"""Filters configuration.

    Attributes:
        rai_settings (google.cloud.modelarmor_v1.types.RaiFilterSettings):
            Optional. Responsible AI settings.
        sdp_settings (google.cloud.modelarmor_v1.types.SdpFilterSettings):
            Optional. Sensitive Data Protection settings.
        pi_and_jailbreak_filter_settings (google.cloud.modelarmor_v1.types.PiAndJailbreakFilterSettings):
            Optional. Prompt injection and Jailbreak
            filter settings.
        malicious_uri_filter_settings (google.cloud.modelarmor_v1.types.MaliciousUriFilterSettings):
            Optional. Malicious URI filter settings.
        filter_rule_settings (google.cloud.modelarmor_v1.types.FilterRuleSettings):
            Optional. Settings for customizing filter
            rules. Note: This field is not supported in
            FloorSetting and Streaming Sanitization APIs.
    """

    rai_settings: "RaiFilterSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RaiFilterSettings",
    )
    sdp_settings: "SdpFilterSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SdpFilterSettings",
    )
    pi_and_jailbreak_filter_settings: "PiAndJailbreakFilterSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PiAndJailbreakFilterSettings",
    )
    malicious_uri_filter_settings: "MaliciousUriFilterSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="MaliciousUriFilterSettings",
    )
    filter_rule_settings: "FilterRuleSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="FilterRuleSettings",
    )


class PiAndJailbreakFilterSettings(proto.Message):
    r"""Prompt injection and Jailbreak Filter settings.

    Attributes:
        filter_enforcement (google.cloud.modelarmor_v1.types.PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement):
            Optional. Tells whether Prompt injection and
            Jailbreak filter is enabled or disabled.
        confidence_level (google.cloud.modelarmor_v1.types.DetectionConfidenceLevel):
            Optional. Confidence level for this filter.
            Confidence level is used to determine the
            threshold for the filter. If detection
            confidence is equal to or greater than the
            specified level, a positive match is reported.
            Confidence level will only be used if the filter
            is enabled.
    """

    class PiAndJailbreakFilterEnforcement(proto.Enum):
        r"""Option to specify the state of Prompt Injection and Jailbreak
        filter (ENABLED/DISABLED).

        Values:
            PI_AND_JAILBREAK_FILTER_ENFORCEMENT_UNSPECIFIED (0):
                Same as Disabled
            ENABLED (1):
                Enabled
            DISABLED (2):
                Disabled
        """

        PI_AND_JAILBREAK_FILTER_ENFORCEMENT_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    filter_enforcement: PiAndJailbreakFilterEnforcement = proto.Field(
        proto.ENUM,
        number=1,
        enum=PiAndJailbreakFilterEnforcement,
    )
    confidence_level: "DetectionConfidenceLevel" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DetectionConfidenceLevel",
    )


class MaliciousUriFilterSettings(proto.Message):
    r"""Malicious URI filter settings.

    Attributes:
        filter_enforcement (google.cloud.modelarmor_v1.types.MaliciousUriFilterSettings.MaliciousUriFilterEnforcement):
            Optional. Tells whether the Malicious URI
            filter is enabled or disabled.
    """

    class MaliciousUriFilterEnforcement(proto.Enum):
        r"""Option to specify the state of Malicious URI filter
        (ENABLED/DISABLED).

        Values:
            MALICIOUS_URI_FILTER_ENFORCEMENT_UNSPECIFIED (0):
                Same as Disabled
            ENABLED (1):
                Enabled
            DISABLED (2):
                Disabled
        """

        MALICIOUS_URI_FILTER_ENFORCEMENT_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    filter_enforcement: MaliciousUriFilterEnforcement = proto.Field(
        proto.ENUM,
        number=1,
        enum=MaliciousUriFilterEnforcement,
    )


class RaiFilterSettings(proto.Message):
    r"""Responsible AI Filter settings.

    Attributes:
        rai_filters (MutableSequence[google.cloud.modelarmor_v1.types.RaiFilterSettings.RaiFilter]):
            Required. List of Responsible AI filters
            enabled for template.
    """

    class RaiFilter(proto.Message):
        r"""Responsible AI filter.

        Attributes:
            filter_type (google.cloud.modelarmor_v1.types.RaiFilterType):
                Required. Type of responsible AI filter.
            confidence_level (google.cloud.modelarmor_v1.types.DetectionConfidenceLevel):
                Optional. Confidence level for this RAI filter. During data
                sanitization, if data is classified under this filter with a
                confidence level equal to or greater than the specified
                level, a positive match is reported. If the confidence level
                is unspecified (i.e., 0), the system will use a reasonable
                default level based on the ``filter_type``.
        """

        filter_type: "RaiFilterType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RaiFilterType",
        )
        confidence_level: "DetectionConfidenceLevel" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DetectionConfidenceLevel",
        )

    rai_filters: MutableSequence[RaiFilter] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RaiFilter,
    )


class SdpFilterSettings(proto.Message):
    r"""Sensitive Data Protection settings.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        basic_config (google.cloud.modelarmor_v1.types.SdpBasicConfig):
            Optional. Basic Sensitive Data Protection
            configuration inspects the content for sensitive
            data using a fixed set of six info-types.
            Sensitive Data Protection templates cannot be
            used with basic configuration. Only Sensitive
            Data Protection inspection operation is
            supported with basic configuration.

            This field is a member of `oneof`_ ``sdp_configuration``.
        advanced_config (google.cloud.modelarmor_v1.types.SdpAdvancedConfig):
            Optional. Advanced Sensitive Data Protection
            configuration which enables use of Sensitive
            Data Protection templates. Supports both
            Sensitive Data Protection inspection and
            de-identification operations.

            This field is a member of `oneof`_ ``sdp_configuration``.
    """

    basic_config: "SdpBasicConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="sdp_configuration",
        message="SdpBasicConfig",
    )
    advanced_config: "SdpAdvancedConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="sdp_configuration",
        message="SdpAdvancedConfig",
    )


class SdpBasicConfig(proto.Message):
    r"""Sensitive Data Protection basic configuration.

    Attributes:
        filter_enforcement (google.cloud.modelarmor_v1.types.SdpBasicConfig.SdpBasicConfigEnforcement):
            Optional. Tells whether the Sensitive Data
            Protection basic config is enabled or disabled.
    """

    class SdpBasicConfigEnforcement(proto.Enum):
        r"""Option to specify the state of Sensitive Data Protection
        basic config (ENABLED/DISABLED).

        Values:
            SDP_BASIC_CONFIG_ENFORCEMENT_UNSPECIFIED (0):
                Same as Disabled
            ENABLED (1):
                Enabled
            DISABLED (2):
                Disabled
        """

        SDP_BASIC_CONFIG_ENFORCEMENT_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    filter_enforcement: SdpBasicConfigEnforcement = proto.Field(
        proto.ENUM,
        number=3,
        enum=SdpBasicConfigEnforcement,
    )


class SdpAdvancedConfig(proto.Message):
    r"""Sensitive Data Protection Advanced configuration.

    Attributes:
        inspect_template (str):
            Optional. Sensitive Data Protection inspect template
            resource name

            If only inspect template is provided (de-identify template
            not provided), then Sensitive Data Protection InspectContent
            action is performed during Sanitization. All Sensitive Data
            Protection findings identified during inspection will be
            returned as SdpFinding in SdpInsepctionResult.

            e.g.
            ``projects/{project}/locations/{location}/inspectTemplates/{inspect_template}``
        deidentify_template (str):
            Optional. Optional Sensitive Data Protection Deidentify
            template resource name.

            If provided then DeidentifyContent action is performed
            during Sanitization using this template and inspect
            template. The De-identified data will be returned in
            SdpDeidentifyResult. Note that all info-types present in the
            deidentify template must be present in inspect template.

            e.g.
            ``projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}``
    """

    inspect_template: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deidentify_template: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SanitizeUserPromptRequest(proto.Message):
    r"""Sanitize User Prompt request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Represents resource name of
            template e.g.
            name=projects/sample-project/locations/us-central1/templates/templ01
        user_prompt_data (google.cloud.modelarmor_v1.types.DataItem):
            Required. User prompt data to sanitize.
        multi_language_detection_metadata (google.cloud.modelarmor_v1.types.MultiLanguageDetectionMetadata):
            Optional. Metadata related to Multi Language
            Detection.
        streaming_mode (google.cloud.modelarmor_v1.types.StreamingMode):
            Optional. Streaming Mode for StreamSanitize\* API.

            This field is a member of `oneof`_ ``_streaming_mode``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_prompt_data: "DataItem" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataItem",
    )
    multi_language_detection_metadata: "MultiLanguageDetectionMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="MultiLanguageDetectionMetadata",
    )
    streaming_mode: "StreamingMode" = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum="StreamingMode",
    )


class SanitizeModelResponseRequest(proto.Message):
    r"""Sanitize Model Response request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Represents resource name of
            template e.g.
            name=projects/sample-project/locations/us-central1/templates/templ01
        model_response_data (google.cloud.modelarmor_v1.types.DataItem):
            Required. Model response data to sanitize.
        user_prompt (str):
            Optional. User Prompt associated with Model
            response.
        multi_language_detection_metadata (google.cloud.modelarmor_v1.types.MultiLanguageDetectionMetadata):
            Optional. Metadata related for multi language
            detection.
        streaming_mode (google.cloud.modelarmor_v1.types.StreamingMode):
            Optional. Streaming Mode for StreamSanitize\* API.

            This field is a member of `oneof`_ ``_streaming_mode``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model_response_data: "DataItem" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataItem",
    )
    user_prompt: str = proto.Field(
        proto.STRING,
        number=4,
    )
    multi_language_detection_metadata: "MultiLanguageDetectionMetadata" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MultiLanguageDetectionMetadata",
    )
    streaming_mode: "StreamingMode" = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum="StreamingMode",
    )


class SanitizeUserPromptResponse(proto.Message):
    r"""Sanitized User Prompt Response.

    Attributes:
        sanitization_result (google.cloud.modelarmor_v1.types.SanitizationResult):
            Output only. Sanitization Result.
    """

    sanitization_result: "SanitizationResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SanitizationResult",
    )


class SanitizeModelResponseResponse(proto.Message):
    r"""Sanitized Model Response Response.

    Attributes:
        sanitization_result (google.cloud.modelarmor_v1.types.SanitizationResult):
            Output only. Sanitization Result.
    """

    sanitization_result: "SanitizationResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SanitizationResult",
    )


class FilterVersionConfig(proto.Message):
    r"""Message describing a Filter Version Configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter_version (str):
            Output only. The identifier for this specific
            version.
        filter_version_alias (google.cloud.modelarmor_v1.types.FilterVersionAlias):
            Output only. The alias associated with this
            version, if any (e.g., "STABLE", "LATEST"). This
            will be populated if this version is currently
            mapped to an alias.

            This field is a member of `oneof`_ ``_filter_version_alias``.
        release_date (google.type.date_pb2.Date):
            Output only. The date when this version was
            released.

            This field is a member of `oneof`_ ``_release_date``.
        projected_deprecation_date (google.type.date_pb2.Date):
            Output only. The estimated date when this
            version is projected to be deprecated.

            This field is a member of `oneof`_ ``_projected_deprecation_date``.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Output only. Extra information regarding this
            filter version
    """

    filter_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter_version_alias: "FilterVersionAlias" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="FilterVersionAlias",
    )
    release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=date_pb2.Date,
    )
    projected_deprecation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=date_pb2.Date,
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="MessageItem",
    )


class SanitizationResult(proto.Message):
    r"""Sanitization result after applying all the filters on input
    content.

    Attributes:
        filter_match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Overall filter match state for Sanitization.
            The state can have below two values.

            1) NO_MATCH_FOUND: No filters in configuration satisfy
               matching criteria. In other words, input passed all
               filters.

            2) MATCH_FOUND: At least one filter in configuration
               satisfies matching. In other words, input did not pass
               one or more filters.
        filter_results (MutableMapping[str, google.cloud.modelarmor_v1.types.FilterResult]):
            Output only. Results for all filters where the key is the
            filter name - either of "csam", "malicious_uris", "rai",
            "pi_and_jailbreak", "sdp".
        invocation_result (google.cloud.modelarmor_v1.types.InvocationResult):
            Output only. A field indicating the outcome
            of the invocation, irrespective of match status.
            It can have the following three values: SUCCESS:
            All filters were executed successfully. PARTIAL:
            Some filters were skipped or failed execution.
            FAILURE: All filters were skipped or failed
            execution.
        sanitization_metadata (google.cloud.modelarmor_v1.types.SanitizationResult.SanitizationMetadata):
            Output only. Metadata related to
            Sanitization.
    """

    class SanitizationMetadata(proto.Message):
        r"""Message describing Sanitization metadata.

        Attributes:
            error_code (int):
                Error code if any.
            error_message (str):
                Error message if any.
            ignore_partial_invocation_failures (bool):
                Passthrough field defined in TemplateMetadata
                to indicate whether to ignore partial invocation
                failures.
            stream_chunk_processed (google.cloud.modelarmor_v1.types.DataItem):
                Output only. The stream chunk processed by
                the Sanitization service.
            filter_version_config (google.cloud.modelarmor_v1.types.FilterVersionConfig):
                Output only. Provides details about the
                Filter Version configuration used to sanitize
                this request.
        """

        error_code: int = proto.Field(
            proto.INT64,
            number=1,
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ignore_partial_invocation_failures: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        stream_chunk_processed: "DataItem" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DataItem",
        )
        filter_version_config: "FilterVersionConfig" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="FilterVersionConfig",
        )

    filter_match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterMatchState",
    )
    filter_results: MutableMapping[str, "FilterResult"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="FilterResult",
    )
    invocation_result: "InvocationResult" = proto.Field(
        proto.ENUM,
        number=4,
        enum="InvocationResult",
    )
    sanitization_metadata: SanitizationMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SanitizationMetadata,
    )


class MultiLanguageDetectionMetadata(proto.Message):
    r"""Message for Enabling Multi Language Detection.

    Attributes:
        source_language (str):
            Optional. Optional Source language of the user prompt.

            If multi-language detection is enabled and this field is not
            set, the source language will be automatically detected.
            When a source language is provided, Model Armor uses it to
            sanitize the input. In that case the system does not perform
            auto-detection and relies solely on the specified language.

            This string field accepts a language code from the ISO-639
            standard. For a list of languages supported by Model Armor,
            see [Model Armor supported languages]
            (https://cloud.google.com/security-command-center/docs/model-armor-overview#languages-supported).
            For a comprehensive list of language codes, see
            `ISO-639 <https://cloud.google.com/translate/docs/languages#nmt>`__.
        enable_multi_language_detection (bool):
            Optional. Enable detection of multi-language
            prompts and responses.
    """

    source_language: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_multi_language_detection: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class FilterResult(proto.Message):
    r"""Filter Result obtained after Sanitization operations.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rai_filter_result (google.cloud.modelarmor_v1.types.RaiFilterResult):
            Responsible AI filter results.

            This field is a member of `oneof`_ ``filter_result``.
        sdp_filter_result (google.cloud.modelarmor_v1.types.SdpFilterResult):
            Sensitive Data Protection results.

            This field is a member of `oneof`_ ``filter_result``.
        pi_and_jailbreak_filter_result (google.cloud.modelarmor_v1.types.PiAndJailbreakFilterResult):
            Prompt injection and Jailbreak filter
            results.

            This field is a member of `oneof`_ ``filter_result``.
        malicious_uri_filter_result (google.cloud.modelarmor_v1.types.MaliciousUriFilterResult):
            Malicious URI filter results.

            This field is a member of `oneof`_ ``filter_result``.
        csam_filter_filter_result (google.cloud.modelarmor_v1.types.CsamFilterResult):
            CSAM filter results.

            This field is a member of `oneof`_ ``filter_result``.
        virus_scan_filter_result (google.cloud.modelarmor_v1.types.VirusScanFilterResult):
            Virus scan results.

            This field is a member of `oneof`_ ``filter_result``.
    """

    rai_filter_result: "RaiFilterResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter_result",
        message="RaiFilterResult",
    )
    sdp_filter_result: "SdpFilterResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter_result",
        message="SdpFilterResult",
    )
    pi_and_jailbreak_filter_result: "PiAndJailbreakFilterResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="filter_result",
        message="PiAndJailbreakFilterResult",
    )
    malicious_uri_filter_result: "MaliciousUriFilterResult" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="filter_result",
        message="MaliciousUriFilterResult",
    )
    csam_filter_filter_result: "CsamFilterResult" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="filter_result",
        message="CsamFilterResult",
    )
    virus_scan_filter_result: "VirusScanFilterResult" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="filter_result",
        message="VirusScanFilterResult",
    )


class RaiFilterResult(proto.Message):
    r"""Responsible AI Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether the RAI filter
            was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Overall filter match state for RAI. Value is
            MATCH_FOUND if at least one RAI filter confidence level is
            equal to or higher than the confidence level defined in
            configuration.
        rai_filter_type_results (MutableMapping[str, google.cloud.modelarmor_v1.types.RaiFilterResult.RaiFilterTypeResult]):
            The map of RAI filter results where the key is the RAI
            filter type and the value is the RAI filter's result.
            Allowed keys are "sexually_explicit", "hate_speech",
            "harassment", and "dangerous".
    """

    class RaiFilterTypeResult(proto.Message):
        r"""Detailed Filter result for each of the responsible AI Filter
        Types.

        Attributes:
            filter_type (google.cloud.modelarmor_v1.types.RaiFilterType):
                Type of responsible AI filter.
            confidence_level (google.cloud.modelarmor_v1.types.DetectionConfidenceLevel):
                Confidence level identified for this RAI
                filter.
            match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
                Output only. Match state for this RAI filter.
        """

        filter_type: "RaiFilterType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RaiFilterType",
        )
        confidence_level: "DetectionConfidenceLevel" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DetectionConfidenceLevel",
        )
        match_state: "FilterMatchState" = proto.Field(
            proto.ENUM,
            number=3,
            enum="FilterMatchState",
        )

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    rai_filter_type_results: MutableMapping[str, RaiFilterTypeResult] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=RaiFilterTypeResult,
    )


class SdpFilterResult(proto.Message):
    r"""Sensitive Data Protection filter result.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inspect_result (google.cloud.modelarmor_v1.types.SdpInspectResult):
            Sensitive Data Protection Inspection result
            if inspection is performed.

            This field is a member of `oneof`_ ``result``.
        deidentify_result (google.cloud.modelarmor_v1.types.SdpDeidentifyResult):
            Sensitive Data Protection Deidentification
            result if deidentification is performed.

            This field is a member of `oneof`_ ``result``.
        redact_result (google.cloud.modelarmor_v1.types.SdpRedactResult):
            Sensitive Data Protection Redaction result if
            redaction is performed. This is primarily used
            for image redaction.

            This field is a member of `oneof`_ ``result``.
    """

    inspect_result: "SdpInspectResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message="SdpInspectResult",
    )
    deidentify_result: "SdpDeidentifyResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="result",
        message="SdpDeidentifyResult",
    )
    redact_result: "SdpRedactResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message="SdpRedactResult",
    )


class SdpInspectResult(proto.Message):
    r"""Sensitive Data Protection Inspection Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Sensitive Data
            Protection inspection was successfully executed
            or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for SDP Inspection. Value is
            MATCH_FOUND if at least one Sensitive Data Protection
            finding is identified.
        findings (MutableSequence[google.cloud.modelarmor_v1.types.SdpFinding]):
            List of Sensitive Data Protection findings.
        findings_truncated (bool):
            If true, then there is possibility that more
            findings were identified and the findings
            returned are a subset of all findings. The
            findings list might be truncated because the
            input items were too large, or because the
            server reached the maximum amount of resources
            allowed for a single API call.
        extracted_image_text (str):
            Contains text extracted from the image, if
            applicable.
    """

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    findings: MutableSequence["SdpFinding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SdpFinding",
    )
    findings_truncated: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    extracted_image_text: str = proto.Field(
        proto.STRING,
        number=6,
    )


class DataItem(proto.Message):
    r"""Represents Data item

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Plaintext string data for sanitization.

            This field is a member of `oneof`_ ``data_item``.
        byte_item (google.cloud.modelarmor_v1.types.ByteDataItem):
            Data provided in the form of bytes.

            This field is a member of `oneof`_ ``data_item``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="data_item",
    )
    byte_item: "ByteDataItem" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data_item",
        message="ByteDataItem",
    )


class ByteDataItem(proto.Message):
    r"""Represents Byte Data item.

    Attributes:
        byte_data_type (google.cloud.modelarmor_v1.types.ByteDataItem.ByteItemType):
            Required. The type of byte data
        byte_data (bytes):
            Required. Bytes Data
        file_label (str):
            Optional. Label of the file. This is used to
            identify the file in the response.
    """

    class ByteItemType(proto.Enum):
        r"""Option to specify the type of byte data.

        Values:
            BYTE_ITEM_TYPE_UNSPECIFIED (0):
                Unused
            PLAINTEXT_UTF8 (1):
                plain text
            PDF (2):
                PDF
            WORD_DOCUMENT (3):
                DOCX, DOCM, DOTX, DOTM
            EXCEL_DOCUMENT (4):
                XLSX, XLSM, XLTX, XLYM
            POWERPOINT_DOCUMENT (5):
                PPTX, PPTM, POTX, POTM, POT
            TXT (6):
                TXT
            CSV (7):
                CSV
            IMAGE (8):
                IMAGE
        """

        BYTE_ITEM_TYPE_UNSPECIFIED = 0
        PLAINTEXT_UTF8 = 1
        PDF = 2
        WORD_DOCUMENT = 3
        EXCEL_DOCUMENT = 4
        POWERPOINT_DOCUMENT = 5
        TXT = 6
        CSV = 7
        IMAGE = 8

    byte_data_type: ByteItemType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ByteItemType,
    )
    byte_data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    file_label: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SdpDeidentifyResult(proto.Message):
    r"""Sensitive Data Protection Deidentification Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Sensitive Data
            Protection deidentification was successfully
            executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for Sensitive Data Protection
            Deidentification. Value is MATCH_FOUND if content is
            de-identified.
        data (google.cloud.modelarmor_v1.types.DataItem):
            De-identified data.
        transformed_bytes (int):
            Total size in bytes that were transformed
            during deidentification.
        info_types (MutableSequence[str]):
            List of Sensitive Data Protection info-types
            that were de-identified.
    """

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    data: "DataItem" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DataItem",
    )
    transformed_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    info_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class SdpImageFindingLocation(proto.Message):
    r"""Location of the finding within an image.

    Attributes:
        bounding_boxes (MutableSequence[google.cloud.modelarmor_v1.types.SdpImageFindingLocation.SdpBoundingBox]):
            Bounding boxes locating the pixels within the
            image containing the finding.
    """

    class SdpBoundingBox(proto.Message):
        r"""Bounding box encompassing a finding within an image.

        Attributes:
            top (int):
                Top coordinate of the bounding box. (0,0) is
                upper left.
            left (int):
                Left coordinate of the bounding box. (0,0) is
                upper left.
            width (int):
                Width of the bounding box in pixels.
            height (int):
                Height of the bounding box in pixels.
        """

        top: int = proto.Field(
            proto.INT32,
            number=1,
        )
        left: int = proto.Field(
            proto.INT32,
            number=2,
        )
        width: int = proto.Field(
            proto.INT32,
            number=3,
        )
        height: int = proto.Field(
            proto.INT32,
            number=4,
        )

    bounding_boxes: MutableSequence[SdpBoundingBox] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=SdpBoundingBox,
    )


class SdpContentLocation(proto.Message):
    r"""Precise location of the finding within a document, record,
    image, or metadata container.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_finding_location (google.cloud.modelarmor_v1.types.SdpImageFindingLocation):
            Location within an image's pixels.

            This field is a member of `oneof`_ ``location``.
        container_name (str):
            Name of the container where the finding is
            located. The top level name is the source file
            name or table name.

            Nested names could be absent if the embedded
            object has no string identifier (for example, an
            image contained within a document).
    """

    image_finding_location: "SdpImageFindingLocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="location",
        message="SdpImageFindingLocation",
    )
    container_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SdpFinding(proto.Message):
    r"""Finding corresponding to Sensitive Data Protection filter.

    Attributes:
        info_type (str):
            Name of Sensitive Data Protection info type
            for this finding.
        likelihood (google.cloud.modelarmor_v1.types.SdpFindingLikelihood):
            Identified confidence likelihood for ``info_type``.
        location (google.cloud.modelarmor_v1.types.SdpFinding.SdpFindingLocation):
            Location for this finding.
    """

    class SdpFindingLocation(proto.Message):
        r"""Location of this Sensitive Data Protection Finding within
        input content.

        Attributes:
            byte_range (google.cloud.modelarmor_v1.types.RangeInfo):
                Zero-based byte offsets delimiting the
                finding. These are relative to the finding's
                containing element. Note that when the content
                is not textual, this references the UTF-8
                encoded textual representation of the content.
                Note: Omitted if content is an image.
            codepoint_range (google.cloud.modelarmor_v1.types.RangeInfo):
                Unicode character offsets delimiting the
                finding. These are relative to the finding's
                containing element. Provided when the content is
                text.
                Note: Omitted if content is an image.
            content_locations (MutableSequence[google.cloud.modelarmor_v1.types.SdpContentLocation]):
                List of nested objects pointing to the precise location of
                the finding within an image, file or record.

                For example, a single finding might be detected in two
                separate bounding boxes within an image (e.g., if it wraps
                across a line or is partially obscured). In such cases,
                content_locations would contain two SdpContentLocation
                entries, each with an image_finding_location pointing to a
                different bounding box.
        """

        byte_range: "RangeInfo" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="RangeInfo",
        )
        codepoint_range: "RangeInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="RangeInfo",
        )
        content_locations: MutableSequence["SdpContentLocation"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SdpContentLocation",
        )

    info_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    likelihood: "SdpFindingLikelihood" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SdpFindingLikelihood",
    )
    location: SdpFindingLocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SdpFindingLocation,
    )


class SdpRedactResult(proto.Message):
    r"""Sensitive Data Protection Redaction Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Sensitive Data
            Protection redaction was successfully executed
            or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Output only. Optional messages corresponding
            to the result. A message can provide warnings or
            error details. For example, if execution state
            is skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for Sensitive Data Protection
            Redaction. Value is MATCH_FOUND if content is redacted.
        redacted_image (bytes):
            Output only. The redacted image. The type
            will be the same as the original image.
        findings (MutableSequence[google.cloud.modelarmor_v1.types.SdpFinding]):
            Output only. The findings. This field is populated in the
            response only when include_findings in the SDP template is
            set to true.
        extracted_image_text (str):
            The extracted text from the image.
    """

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    redacted_image: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    findings: MutableSequence["SdpFinding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="SdpFinding",
    )
    extracted_image_text: str = proto.Field(
        proto.STRING,
        number=6,
    )


class WordList(proto.Message):
    r"""Message defining a list of words or phrases.

    Attributes:
        words (MutableSequence[str]):
            Required. Words or phrases defining the
            dictionary. The dictionary must contain at least
            one phrase and every phrase must contain at
            least two characters that are letters or digits.
    """

    words: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Dictionary(proto.Message):
    r"""Message defining a custom dictionary of words or phrases for
    syntactic match.

    Dictionary words are case-insensitive and all characters other than
    letters and digits in the unicode `Basic Multilingual
    Plane <https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Basic_Multilingual_Plane>`__
    will be replaced with whitespace when scanning for matches. For
    example, the dictionary phrase ``Sam Johnson`` will match all three
    phrases ``sam johnson``, ``Sam, Johnson``, and ``Sam (Johnson)``.
    Additionally, the characters surrounding any match must be of a
    different type than the adjacent characters within the word, so
    letters must be next to non-letters and digits must be next to
    non-digits. For example, the dictionary word ``jen`` will match the
    first three letters of the text ``jen123`` but will return no
    matches for ``jennifer``.

    Dictionary words containing a large number of characters that are
    not letters or digits may result in unexpected matches because such
    characters are treated as whitespace. For details about the size
    limits of dictionaries, see `Quotas and
    limits <https://docs.cloud.google.com/model-armor/quotas>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        word_list (google.cloud.modelarmor_v1.types.WordList):
            Message defining a list of words or phrases.

            This field is a member of `oneof`_ ``source``.
    """

    word_list: "WordList" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="WordList",
    )


class Regex(proto.Message):
    r"""Message defining a custom regular expression.

    Attributes:
        pattern (str):
            Required. The regular expression pattern.
    """

    pattern: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExclusionRule(proto.Message):
    r"""The rule that specifies conditions when filter detections are
    excluded from results.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dictionary (google.cloud.modelarmor_v1.types.Dictionary):
            Dictionary which defines the rule.

            This field is a member of `oneof`_ ``type``.
        regex (google.cloud.modelarmor_v1.types.Regex):
            Regular expression which defines the rule.

            This field is a member of `oneof`_ ``type``.
        matching_scope (google.cloud.modelarmor_v1.types.MatchingScope):
            Optional. Specifies the scope of the input that should be
            matched against the exclusion rule. If unspecified, defaults
            to MATCHING_SCOPE_PARTIAL_MATCH.

            This field is a member of `oneof`_ ``_matching_scope``.
    """

    dictionary: "Dictionary" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message="Dictionary",
    )
    regex: "Regex" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="Regex",
    )
    matching_scope: "MatchingScope" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="MatchingScope",
    )


class FilterRule(proto.Message):
    r"""A single rule to be applied to filters, specified in
    ``FilterRuleSet``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        exclusion_rule (google.cloud.modelarmor_v1.types.ExclusionRule):
            Exclusion rule.

            This field is a member of `oneof`_ ``type``.
    """

    exclusion_rule: "ExclusionRule" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message="ExclusionRule",
    )


class FilterRuleSet(proto.Message):
    r"""A set of rules that modifies the behavior of specific filters
    based on the rules defined within the set.

    Attributes:
        filter_types (MutableSequence[google.cloud.modelarmor_v1.types.RuleFilterType]):
            Required. List of filters this rule set is
            applied to.
        rules (MutableSequence[google.cloud.modelarmor_v1.types.FilterRule]):
            Required. Set of rules to be applied to
            filterTypes.
    """

    filter_types: MutableSequence["RuleFilterType"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="RuleFilterType",
    )
    rules: MutableSequence["FilterRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FilterRule",
    )


class FilterRuleSettings(proto.Message):
    r"""Settings for customizing filter rules.

    Attributes:
        rule_sets (MutableSequence[google.cloud.modelarmor_v1.types.FilterRuleSet]):
            Optional. List of rule sets to be applied to
            filters.
    """

    rule_sets: MutableSequence["FilterRuleSet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FilterRuleSet",
    )


class PiAndJailbreakFilterResult(proto.Message):
    r"""Prompt injection and Jailbreak Filter Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Prompt injection
            and Jailbreak filter was successfully executed
            or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for Prompt injection
            and Jailbreak.
        confidence_level (google.cloud.modelarmor_v1.types.DetectionConfidenceLevel):
            Confidence level identified for Prompt
            injection and Jailbreak.
    """

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    confidence_level: "DetectionConfidenceLevel" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DetectionConfidenceLevel",
    )


class MaliciousUriFilterResult(proto.Message):
    r"""Malicious URI Filter Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Malicious URI
            filter was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for this Malicious URI. Value is
            MATCH_FOUND if at least one Malicious URI is found.
        malicious_uri_matched_items (MutableSequence[google.cloud.modelarmor_v1.types.MaliciousUriFilterResult.MaliciousUriMatchedItem]):
            List of Malicious URIs found in data.
    """

    class MaliciousUriMatchedItem(proto.Message):
        r"""Information regarding malicious URI and its location within
        the input content.

        Attributes:
            uri (str):
                Malicious URI.
            locations (MutableSequence[google.cloud.modelarmor_v1.types.RangeInfo]):
                List of locations where Malicious URI is identified. The
                ``locations`` field is supported only for plaintext content
                i.e. ByteItemType.PLAINTEXT_UTF8
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        locations: MutableSequence["RangeInfo"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="RangeInfo",
        )

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    malicious_uri_matched_items: MutableSequence[MaliciousUriMatchedItem] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=MaliciousUriMatchedItem,
        )
    )


class VirusScanFilterResult(proto.Message):
    r"""Virus scan results.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether Virus Scan was
            successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution status is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match status for Virus. Value is MATCH_FOUND if
            the data is infected with a virus.
        scanned_content_type (google.cloud.modelarmor_v1.types.VirusScanFilterResult.ScannedContentType):
            Type of content scanned.
        scanned_size (int):
            Size of scanned content in bytes.

            This field is a member of `oneof`_ ``_scanned_size``.
        virus_details (MutableSequence[google.cloud.modelarmor_v1.types.VirusDetail]):
            List of Viruses identified.
            This field will be empty if no virus was
            detected.
    """

    class ScannedContentType(proto.Enum):
        r"""Type of content scanned.

        Values:
            SCANNED_CONTENT_TYPE_UNSPECIFIED (0):
                Unused
            UNKNOWN (1):
                Unknown content
            PLAINTEXT (2):
                Plaintext
            PDF (3):
                PDF
                Scanning for only PDF is supported.
        """

        SCANNED_CONTENT_TYPE_UNSPECIFIED = 0
        UNKNOWN = 1
        PLAINTEXT = 2
        PDF = 3

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )
    scanned_content_type: ScannedContentType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ScannedContentType,
    )
    scanned_size: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    virus_details: MutableSequence["VirusDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="VirusDetail",
    )


class VirusDetail(proto.Message):
    r"""Details of an identified virus

    Attributes:
        vendor (str):
            Name of vendor that produced this virus
            identification.
        names (MutableSequence[str]):
            Names of this Virus.
        threat_type (google.cloud.modelarmor_v1.types.VirusDetail.ThreatType):
            Threat type of the identified virus
    """

    class ThreatType(proto.Enum):
        r"""Defines all the threat types of a virus

        Values:
            THREAT_TYPE_UNSPECIFIED (0):
                Unused
            UNKNOWN (1):
                Unable to categorize threat
            VIRUS_OR_WORM (2):
                Virus or Worm threat.
            MALICIOUS_PROGRAM (3):
                Malicious program. E.g. Spyware, Trojan.
            POTENTIALLY_HARMFUL_CONTENT (4):
                Potentially harmful content. E.g. Injected
                code, Macro
            POTENTIALLY_UNWANTED_CONTENT (5):
                Potentially unwanted content. E.g. Adware.
        """

        THREAT_TYPE_UNSPECIFIED = 0
        UNKNOWN = 1
        VIRUS_OR_WORM = 2
        MALICIOUS_PROGRAM = 3
        POTENTIALLY_HARMFUL_CONTENT = 4
        POTENTIALLY_UNWANTED_CONTENT = 5

    vendor: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    threat_type: ThreatType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ThreatType,
    )


class CsamFilterResult(proto.Message):
    r"""CSAM (Child Safety Abuse Material) Filter Result

    Attributes:
        execution_state (google.cloud.modelarmor_v1.types.FilterExecutionState):
            Output only. Reports whether the CSAM filter
            was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1.types.FilterMatchState):
            Output only. Match state for CSAM.
    """

    execution_state: "FilterExecutionState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="FilterExecutionState",
    )
    message_items: MutableSequence["MessageItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MessageItem",
    )
    match_state: "FilterMatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FilterMatchState",
    )


class MessageItem(proto.Message):
    r"""Message item to report information, warning or error
    messages.

    Attributes:
        message_type (google.cloud.modelarmor_v1.types.MessageItem.MessageType):
            Type of message.
        message (str):
            The message content.
    """

    class MessageType(proto.Enum):
        r"""Option to specify the type of message.

        Values:
            MESSAGE_TYPE_UNSPECIFIED (0):
                Unused
            INFO (1):
                Information related message.
            WARNING (2):
                Warning related message.
            ERROR (3):
                Error message.
        """

        MESSAGE_TYPE_UNSPECIFIED = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    message_type: MessageType = proto.Field(
        proto.ENUM,
        number=1,
        enum=MessageType,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RangeInfo(proto.Message):
    r"""Half-open range interval [start, end)

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start (int):
            For proto3, value cannot be set to 0 unless
            the field is optional. Ref:
            https://protobuf.dev/programming-guides/proto3/#default
            Index of first character (inclusive).

            This field is a member of `oneof`_ ``_start``.
        end (int):
            Index of last character (exclusive).

            This field is a member of `oneof`_ ``_end``.
    """

    start: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    end: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
