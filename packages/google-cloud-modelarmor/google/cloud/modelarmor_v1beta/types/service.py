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

__protobuf__ = proto.module(
    package="google.cloud.modelarmor.v1beta",
    manifest={
        "FilterMatchState",
        "FilterExecutionState",
        "RaiFilterType",
        "DetectionConfidenceLevel",
        "SdpFindingLikelihood",
        "InvocationResult",
        "StreamingMode",
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
        "SanitizationResult",
        "MultiLanguageDetectionMetadata",
        "FilterResult",
        "RaiFilterResult",
        "SdpFilterResult",
        "SdpInspectResult",
        "DataItem",
        "ByteDataItem",
        "SdpDeidentifyResult",
        "SdpFinding",
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
        filter_config (google.cloud.modelarmor_v1beta.types.FilterConfig):
            Required. filter configuration for this
            template
        template_metadata (google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata):
            Optional. metadata for this template
    """

    class TemplateMetadata(proto.Message):
        r"""Message describing TemplateMetadata

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
            enforcement_type (google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata.EnforcementType):
                Optional. Enforcement type for Model Armor
                filters.
            multi_language_detection (google.cloud.modelarmor_v1beta.types.Template.TemplateMetadata.MultiLanguageDetection):
                Optional. Metadata for multi language
                detection.
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
        filter_config (google.cloud.modelarmor_v1beta.types.FilterConfig):
            Required. ModelArmor filter configuration.
        enable_floor_setting_enforcement (bool):
            Optional. Floor Settings enforcement status.

            This field is a member of `oneof`_ ``_enable_floor_setting_enforcement``.
        integrated_services (MutableSequence[google.cloud.modelarmor_v1beta.types.FloorSetting.IntegratedService]):
            Optional. List of integrated services for
            which the floor setting is applicable.
        ai_platform_floor_setting (google.cloud.modelarmor_v1beta.types.AiPlatformFloorSetting):
            Optional. AI Platform floor setting.

            This field is a member of `oneof`_ ``_ai_platform_floor_setting``.
        floor_setting_metadata (google.cloud.modelarmor_v1beta.types.FloorSetting.FloorSettingMetadata):
            Optional. Metadata for FloorSetting
        google_mcp_server_floor_setting (google.cloud.modelarmor_v1beta.types.McpServerFloorSetting):
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
            multi_language_detection (google.cloud.modelarmor_v1beta.types.FloorSetting.FloorSettingMetadata.MultiLanguageDetection):
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
        apis (MutableSequence[str]):
            Optional. List of MCP servers for which the
            MCP floor setting is applicable. Examples:
            "bigquery.googleapis.com/mcp",
            "run.googleapis.com/mcp" Empty list denotes that
            the floor setting is applicable to all MCP
            servers.
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
    apis: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
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
        templates (MutableSequence[google.cloud.modelarmor_v1beta.types.Template]):
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
        template (google.cloud.modelarmor_v1beta.types.Template):
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
        template (google.cloud.modelarmor_v1beta.types.Template):
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
        floor_setting (google.cloud.modelarmor_v1beta.types.FloorSetting):
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
        rai_settings (google.cloud.modelarmor_v1beta.types.RaiFilterSettings):
            Optional. Responsible AI settings.
        sdp_settings (google.cloud.modelarmor_v1beta.types.SdpFilterSettings):
            Optional. Sensitive Data Protection settings.
        pi_and_jailbreak_filter_settings (google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterSettings):
            Optional. Prompt injection and Jailbreak
            filter settings.
        malicious_uri_filter_settings (google.cloud.modelarmor_v1beta.types.MaliciousUriFilterSettings):
            Optional. Malicious URI filter settings.
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


class PiAndJailbreakFilterSettings(proto.Message):
    r"""Prompt injection and Jailbreak Filter settings.

    Attributes:
        filter_enforcement (google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement):
            Optional. Tells whether Prompt injection and
            Jailbreak filter is enabled or disabled.
        confidence_level (google.cloud.modelarmor_v1beta.types.DetectionConfidenceLevel):
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
        filter_enforcement (google.cloud.modelarmor_v1beta.types.MaliciousUriFilterSettings.MaliciousUriFilterEnforcement):
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
        rai_filters (MutableSequence[google.cloud.modelarmor_v1beta.types.RaiFilterSettings.RaiFilter]):
            Required. List of Responsible AI filters
            enabled for template.
    """

    class RaiFilter(proto.Message):
        r"""Responsible AI filter.

        Attributes:
            filter_type (google.cloud.modelarmor_v1beta.types.RaiFilterType):
                Required. Type of responsible AI filter.
            confidence_level (google.cloud.modelarmor_v1beta.types.DetectionConfidenceLevel):
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
        basic_config (google.cloud.modelarmor_v1beta.types.SdpBasicConfig):
            Optional. Basic Sensitive Data Protection
            configuration inspects the content for sensitive
            data using a fixed set of six info-types.
            Sensitive Data Protection templates cannot be
            used with basic configuration. Only Sensitive
            Data Protection inspection operation is
            supported with basic configuration.

            This field is a member of `oneof`_ ``sdp_configuration``.
        advanced_config (google.cloud.modelarmor_v1beta.types.SdpAdvancedConfig):
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
        filter_enforcement (google.cloud.modelarmor_v1beta.types.SdpBasicConfig.SdpBasicConfigEnforcement):
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
        user_prompt_data (google.cloud.modelarmor_v1beta.types.DataItem):
            Required. User prompt data to sanitize.
        multi_language_detection_metadata (google.cloud.modelarmor_v1beta.types.MultiLanguageDetectionMetadata):
            Optional. Metadata related to Multi Language
            Detection.
        streaming_mode (google.cloud.modelarmor_v1beta.types.StreamingMode):
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
        model_response_data (google.cloud.modelarmor_v1beta.types.DataItem):
            Required. Model response data to sanitize.
        user_prompt (str):
            Optional. User Prompt associated with Model
            response.
        multi_language_detection_metadata (google.cloud.modelarmor_v1beta.types.MultiLanguageDetectionMetadata):
            Optional. Metadata related for multi language
            detection.
        streaming_mode (google.cloud.modelarmor_v1beta.types.StreamingMode):
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
        sanitization_result (google.cloud.modelarmor_v1beta.types.SanitizationResult):
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
        sanitization_result (google.cloud.modelarmor_v1beta.types.SanitizationResult):
            Output only. Sanitization Result.
    """

    sanitization_result: "SanitizationResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SanitizationResult",
    )


class SanitizationResult(proto.Message):
    r"""Sanitization result after applying all the filters on input
    content.

    Attributes:
        filter_match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Overall filter match state for Sanitization.
            The state can have below two values.

            1) NO_MATCH_FOUND: No filters in configuration satisfy
               matching criteria. In other words, input passed all
               filters.

            2) MATCH_FOUND: At least one filter in configuration
               satisfies matching. In other words, input did not pass
               one or more filters.
        filter_results (MutableMapping[str, google.cloud.modelarmor_v1beta.types.FilterResult]):
            Output only. Results for all filters where the key is the
            filter name - either of "csam", "malicious_uris", "rai",
            "pi_and_jailbreak" ,"sdp".
        invocation_result (google.cloud.modelarmor_v1beta.types.InvocationResult):
            Output only. A field indicating the outcome
            of the invocation, irrespective of match status.
            It can have the following three values: SUCCESS:
            All filters were executed successfully. PARTIAL:
            Some filters were skipped or failed execution.
            FAILURE: All filters were skipped or failed
            execution.
        sanitization_metadata (google.cloud.modelarmor_v1beta.types.SanitizationResult.SanitizationMetadata):
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
        rai_filter_result (google.cloud.modelarmor_v1beta.types.RaiFilterResult):
            Responsible AI filter results.

            This field is a member of `oneof`_ ``filter_result``.
        sdp_filter_result (google.cloud.modelarmor_v1beta.types.SdpFilterResult):
            Sensitive Data Protection results.

            This field is a member of `oneof`_ ``filter_result``.
        pi_and_jailbreak_filter_result (google.cloud.modelarmor_v1beta.types.PiAndJailbreakFilterResult):
            Prompt injection and Jailbreak filter
            results.

            This field is a member of `oneof`_ ``filter_result``.
        malicious_uri_filter_result (google.cloud.modelarmor_v1beta.types.MaliciousUriFilterResult):
            Malicious URI filter results.

            This field is a member of `oneof`_ ``filter_result``.
        csam_filter_filter_result (google.cloud.modelarmor_v1beta.types.CsamFilterResult):
            CSAM filter results.

            This field is a member of `oneof`_ ``filter_result``.
        virus_scan_filter_result (google.cloud.modelarmor_v1beta.types.VirusScanFilterResult):
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
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether the RAI filter
            was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Overall filter match state for RAI. Value is
            MATCH_FOUND if at least one RAI filter confidence level is
            equal to or higher than the confidence level defined in
            configuration.
        rai_filter_type_results (MutableMapping[str, google.cloud.modelarmor_v1beta.types.RaiFilterResult.RaiFilterTypeResult]):
            The map of RAI filter results where key is RAI filter type -
            either of "sexually_explicit", "hate_speech", "harassment",
            "dangerous", "violence", "sexually_suggestive".
    """

    class RaiFilterTypeResult(proto.Message):
        r"""Detailed Filter result for each of the responsible AI Filter
        Types.

        Attributes:
            filter_type (google.cloud.modelarmor_v1beta.types.RaiFilterType):
                Type of responsible AI filter.
            confidence_level (google.cloud.modelarmor_v1beta.types.DetectionConfidenceLevel):
                Confidence level identified for this RAI
                filter.
            match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
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
        inspect_result (google.cloud.modelarmor_v1beta.types.SdpInspectResult):
            Sensitive Data Protection Inspection result
            if inspection is performed.

            This field is a member of `oneof`_ ``result``.
        deidentify_result (google.cloud.modelarmor_v1beta.types.SdpDeidentifyResult):
            Sensitive Data Protection Deidentification
            result if deidentification is performed.

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


class SdpInspectResult(proto.Message):
    r"""Sensitive Data Protection Inspection Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether Sensitive Data
            Protection inspection was successfully executed
            or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Match state for SDP Inspection. Value is
            MATCH_FOUND if at least one Sensitive Data Protection
            finding is identified.
        findings (MutableSequence[google.cloud.modelarmor_v1beta.types.SdpFinding]):
            List of Sensitive Data Protection findings.
        findings_truncated (bool):
            If true, then there is possibility that more
            findings were identified and the findings
            returned are a subset of all findings. The
            findings list might be truncated because the
            input items were too large, or because the
            server reached the maximum amount of resources
            allowed for a single API call.
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
        byte_item (google.cloud.modelarmor_v1beta.types.ByteDataItem):
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
        byte_data_type (google.cloud.modelarmor_v1beta.types.ByteDataItem.ByteItemType):
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
            ZIP (9):
                ZIP
        """

        BYTE_ITEM_TYPE_UNSPECIFIED = 0
        PLAINTEXT_UTF8 = 1
        PDF = 2
        WORD_DOCUMENT = 3
        EXCEL_DOCUMENT = 4
        POWERPOINT_DOCUMENT = 5
        TXT = 6
        CSV = 7
        ZIP = 9

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
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether Sensitive Data
            Protection deidentification was successfully
            executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Match state for Sensitive Data Protection
            Deidentification. Value is MATCH_FOUND if content is
            de-identified.
        data (google.cloud.modelarmor_v1beta.types.DataItem):
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


class SdpFinding(proto.Message):
    r"""Finding corresponding to Sensitive Data Protection filter.

    Attributes:
        info_type (str):
            Name of Sensitive Data Protection info type
            for this finding.
        likelihood (google.cloud.modelarmor_v1beta.types.SdpFindingLikelihood):
            Identified confidence likelihood for ``info_type``.
        location (google.cloud.modelarmor_v1beta.types.SdpFinding.SdpFindingLocation):
            Location for this finding.
    """

    class SdpFindingLocation(proto.Message):
        r"""Location of this Sensitive Data Protection Finding within
        input content.

        Attributes:
            byte_range (google.cloud.modelarmor_v1beta.types.RangeInfo):
                Zero-based byte offsets delimiting the
                finding. These are relative to the finding's
                containing element. Note that when the content
                is not textual, this references the UTF-8
                encoded textual representation of the content.
                Note: Omitted if content is an image.
            codepoint_range (google.cloud.modelarmor_v1beta.types.RangeInfo):
                Unicode character offsets delimiting the
                finding. These are relative to the finding's
                containing element. Provided when the content is
                text.
                Note: Omitted if content is an image.
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


class PiAndJailbreakFilterResult(proto.Message):
    r"""Prompt injection and Jailbreak Filter Result.

    Attributes:
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether Prompt injection
            and Jailbreak filter was successfully executed
            or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Match state for Prompt injection
            and Jailbreak.
        confidence_level (google.cloud.modelarmor_v1beta.types.DetectionConfidenceLevel):
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
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether Malicious URI
            filter was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Match state for this Malicious URI. Value is
            MATCH_FOUND if at least one Malicious URI is found.
        malicious_uri_matched_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MaliciousUriFilterResult.MaliciousUriMatchedItem]):
            List of Malicious URIs found in data.
    """

    class MaliciousUriMatchedItem(proto.Message):
        r"""Information regarding malicious URI and its location within
        the input content.

        Attributes:
            uri (str):
                Malicious URI.
            locations (MutableSequence[google.cloud.modelarmor_v1beta.types.RangeInfo]):
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
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether Virus Scan was
            successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution status is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
            Output only. Match status for Virus. Value is MATCH_FOUND if
            the data is infected with a virus.
        scanned_content_type (google.cloud.modelarmor_v1beta.types.VirusScanFilterResult.ScannedContentType):
            Type of content scanned.
        scanned_size (int):
            Size of scanned content in bytes.

            This field is a member of `oneof`_ ``_scanned_size``.
        virus_details (MutableSequence[google.cloud.modelarmor_v1beta.types.VirusDetail]):
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
        threat_type (google.cloud.modelarmor_v1beta.types.VirusDetail.ThreatType):
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
        execution_state (google.cloud.modelarmor_v1beta.types.FilterExecutionState):
            Output only. Reports whether the CSAM filter
            was successfully executed or not.
        message_items (MutableSequence[google.cloud.modelarmor_v1beta.types.MessageItem]):
            Optional messages corresponding to the
            result. A message can provide warnings or error
            details. For example, if execution state is
            skipped then this field provides related
            reason/explanation.
        match_state (google.cloud.modelarmor_v1beta.types.FilterMatchState):
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
        message_type (google.cloud.modelarmor_v1beta.types.MessageItem.MessageType):
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
