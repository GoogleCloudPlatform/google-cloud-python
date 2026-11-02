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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.discoveryengine_v1beta.types import grounded_generation_service

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "AssistAnswer",
        "AssistantContent",
        "AssistantGroundedContent",
    },
)


class AssistAnswer(proto.Message):
    r"""AssistAnswer resource, main part of
    [AssistResponse][google.cloud.discoveryengine.v1beta.AssistResponse].

    Attributes:
        name (str):
            Immutable. Identifier. Resource name of the
            ``AssistAnswer``. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/assistAnswers/{assist_answer}``

            This field must be a UTF-8 encoded string with a length
            limit of 1024 characters.
        state (google.cloud.discoveryengine_v1beta.types.AssistAnswer.State):
            State of the answer generation.
        replies (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistAnswer.Reply]):
            Replies of the assistant.
        assist_skipped_reasons (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistAnswer.AssistSkippedReason]):
            Reasons for not answering the assist call.
        customer_policy_enforcement_result (google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult):
            Optional. The field contains information
            about the various policy checks' results like
            the banned phrases or the Model Armor checks.
            This field is populated only if the assist call
            was skipped due to a policy violation.
    """

    class State(proto.Enum):
        r"""State of the answer generation.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown.
            IN_PROGRESS (1):
                Assist operation is currently in progress.
            FAILED (2):
                Assist operation has failed.
            SUCCEEDED (3):
                Assist operation has succeeded.
            SKIPPED (4):
                Assist operation has been skipped.
            CANCELLED (5):
                Assist operation has been cancelled (e.g.
                client closed the stream). May contain a partial
                response.
        """

        STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        FAILED = 2
        SUCCEEDED = 3
        SKIPPED = 4
        CANCELLED = 5

    class AssistSkippedReason(proto.Enum):
        r"""Possible reasons for not answering an assist call.

        Values:
            ASSIST_SKIPPED_REASON_UNSPECIFIED (0):
                Default value. Skip reason is not specified.
            NON_ASSIST_SEEKING_QUERY_IGNORED (1):
                The assistant ignored the query, because it
                did not appear to be answer-seeking.
            CUSTOMER_POLICY_VIOLATION (2):
                The assistant ignored the query or refused to
                answer because of a customer policy violation
                (e.g., the query or the answer contained a
                banned phrase).
        """

        ASSIST_SKIPPED_REASON_UNSPECIFIED = 0
        NON_ASSIST_SEEKING_QUERY_IGNORED = 1
        CUSTOMER_POLICY_VIOLATION = 2

    class Reply(proto.Message):
        r"""One part of the multi-part response of the assist call.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            grounded_content (google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent):
                Possibly grounded response text or media from
                the assistant.

                This field is a member of `oneof`_ ``reply``.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                The time when the reply was created.
        """

        grounded_content: "AssistantGroundedContent" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="reply",
            message="AssistantGroundedContent",
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=14,
            message=timestamp_pb2.Timestamp,
        )

    class CustomerPolicyEnforcementResult(proto.Message):
        r"""Customer policy enforcement results. Contains the results of
        the various policy checks, like the banned phrases or the Model
        Armor checks.

        Attributes:
            verdict (google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.Verdict):
                Final verdict of the customer policy
                enforcement. If only one policy blocked the
                processing, the verdict is BLOCK.
            policy_results (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.PolicyEnforcementResult]):
                Customer policy enforcement results.
                Populated only if the assist call was skipped
                due to a policy violation. It contains results
                from those filters that blocked the processing
                of the query.
        """

        class Verdict(proto.Enum):
            r"""The verdict of the customer policy enforcement.

            Values:
                UNSPECIFIED (0):
                    Unknown value.
                ALLOW (1):
                    There was no policy violation.
                BLOCK (2):
                    Processing was blocked by the customer
                    policy.
            """

            UNSPECIFIED = 0
            ALLOW = 1
            BLOCK = 2

        class BannedPhraseEnforcementResult(proto.Message):
            r"""Customer policy enforcement result for the banned phrase
            policy.

            Attributes:
                banned_phrases (MutableSequence[str]):
                    The banned phrases that were found in the
                    query or the answer.
            """

            banned_phrases: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class ModelArmorEnforcementResult(proto.Message):
            r"""Customer policy enforcement result for the Model Armor
            policy.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                model_armor_violation (str):
                    The Model Armor violation that was found.

                    This field is a member of `oneof`_ ``result``.
                error (google.rpc.status_pb2.Status):
                    The error returned by Model Armor if the
                    policy enforcement failed for some reason.

                    This field is a member of `oneof`_ ``result``.
            """

            model_armor_violation: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="result",
            )
            error: status_pb2.Status = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="result",
                message=status_pb2.Status,
            )

        class PolicyEnforcementResult(proto.Message):
            r"""Customer policy enforcement result for a single policy type.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                banned_phrase_enforcement_result (google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.BannedPhraseEnforcementResult):
                    The policy enforcement result for the banned
                    phrase policy.

                    This field is a member of `oneof`_ ``enforcement_result``.
                model_armor_enforcement_result (google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.ModelArmorEnforcementResult):
                    The policy enforcement result for the Model
                    Armor policy.

                    This field is a member of `oneof`_ ``enforcement_result``.
            """

            banned_phrase_enforcement_result: "AssistAnswer.CustomerPolicyEnforcementResult.BannedPhraseEnforcementResult" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="enforcement_result",
                message="AssistAnswer.CustomerPolicyEnforcementResult.BannedPhraseEnforcementResult",
            )
            model_armor_enforcement_result: "AssistAnswer.CustomerPolicyEnforcementResult.ModelArmorEnforcementResult" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="enforcement_result",
                message="AssistAnswer.CustomerPolicyEnforcementResult.ModelArmorEnforcementResult",
            )

        verdict: "AssistAnswer.CustomerPolicyEnforcementResult.Verdict" = proto.Field(
            proto.ENUM,
            number=1,
            enum="AssistAnswer.CustomerPolicyEnforcementResult.Verdict",
        )
        policy_results: MutableSequence[
            "AssistAnswer.CustomerPolicyEnforcementResult.PolicyEnforcementResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="AssistAnswer.CustomerPolicyEnforcementResult.PolicyEnforcementResult",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    replies: MutableSequence[Reply] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Reply,
    )
    assist_skipped_reasons: MutableSequence[AssistSkippedReason] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum=AssistSkippedReason,
    )
    customer_policy_enforcement_result: CustomerPolicyEnforcementResult = proto.Field(
        proto.MESSAGE,
        number=8,
        message=CustomerPolicyEnforcementResult,
    )


class AssistantContent(proto.Message):
    r"""Multi-modal content.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Inline text.

            This field is a member of `oneof`_ ``data``.
        inline_data (google.cloud.discoveryengine_v1beta.types.AssistantContent.Blob):
            Inline binary data.

            This field is a member of `oneof`_ ``data``.
        file (google.cloud.discoveryengine_v1beta.types.AssistantContent.File):
            A file, e.g., an audio summary.

            This field is a member of `oneof`_ ``data``.
        executable_code (google.cloud.discoveryengine_v1beta.types.AssistantContent.ExecutableCode):
            Code generated by the model that is meant to
            be executed.

            This field is a member of `oneof`_ ``data``.
        code_execution_result (google.cloud.discoveryengine_v1beta.types.AssistantContent.CodeExecutionResult):
            Result of executing an ExecutableCode.

            This field is a member of `oneof`_ ``data``.
        role (str):
            The producer of the content. Can be "model"
            or "user".
        thought (bool):
            Optional. Indicates if the part is thought
            from the model.
    """

    class Blob(proto.Message):
        r"""Inline blob.

        Attributes:
            mime_type (str):
                Required. The media type (MIME type) of the
                generated data.
            data (bytes):
                Required. Raw bytes.
        """

        mime_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        data: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )

    class File(proto.Message):
        r"""A file, e.g., an audio summary.

        Attributes:
            mime_type (str):
                Required. The media type (MIME type) of the
                file.
            file_id (str):
                Required. The file ID.
        """

        mime_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        file_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ExecutableCode(proto.Message):
        r"""Code generated by the model that is meant to be executed by
        the model.

        Attributes:
            code (str):
                Required. The code content. Currently only
                supports Python.
        """

        code: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class CodeExecutionResult(proto.Message):
        r"""Result of executing ExecutableCode.

        Attributes:
            outcome (google.cloud.discoveryengine_v1beta.types.AssistantContent.CodeExecutionResult.Outcome):
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

        outcome: "AssistantContent.CodeExecutionResult.Outcome" = proto.Field(
            proto.ENUM,
            number=1,
            enum="AssistantContent.CodeExecutionResult.Outcome",
        )
        output: str = proto.Field(
            proto.STRING,
            number=2,
        )

    text: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="data",
    )
    inline_data: Blob = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message=Blob,
    )
    file: File = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message=File,
    )
    executable_code: ExecutableCode = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data",
        message=ExecutableCode,
    )
    code_execution_result: CodeExecutionResult = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message=CodeExecutionResult,
    )
    role: str = proto.Field(
        proto.STRING,
        number=1,
    )
    thought: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class AssistantGroundedContent(proto.Message):
    r"""A piece of content and possibly its grounding information.

    Not all content needs grounding. Phrases like "Of course, I will
    gladly search it for you." do not need grounding.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_grounding_metadata (google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata):
            Metadata for grounding based on text sources.

            This field is a member of `oneof`_ ``metadata``.
        content (google.cloud.discoveryengine_v1beta.types.AssistantContent):
            The content.
        citation_metadata (google.cloud.discoveryengine_v1beta.types.CitationMetadata):
            Source attribution of the generated content. See also
            https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview#citation_check
    """

    class TextGroundingMetadata(proto.Message):
        r"""Grounding details for text sources.

        Attributes:
            segments (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Segment]):
                Grounding information for parts of the text.
            visual_segments (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.VisualSegment]):
                Grounding information for parts of the visual
                content.
            references (MutableSequence[google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference]):
                References for the grounded text.
        """

        class Segment(proto.Message):
            r"""Grounding information for a segment of the text.

            Attributes:
                start_index (int):
                    Zero-based index indicating the start of the
                    segment, measured in bytes of a UTF-8 string
                    (i.e. characters encoded on multiple bytes have
                    a length of more than one).
                end_index (int):
                    End of the segment, exclusive.
                reference_indices (MutableSequence[int]):
                    References for the segment.
                grounding_score (float):
                    Score for the segment.
                text (str):
                    The text segment itself.
            """

            start_index: int = proto.Field(
                proto.INT64,
                number=1,
            )
            end_index: int = proto.Field(
                proto.INT64,
                number=2,
            )
            reference_indices: MutableSequence[int] = proto.RepeatedField(
                proto.INT32,
                number=4,
            )
            grounding_score: float = proto.Field(
                proto.FLOAT,
                number=5,
            )
            text: str = proto.Field(
                proto.STRING,
                number=6,
            )

        class VisualSegment(proto.Message):
            r"""Grounding information for a visual segment.

            Attributes:
                reference_indices (MutableSequence[int]):
                    References for the visual segment.
                content_id (str):
                    The content id of the visual segment. In order to display
                    the citation of the visual element, this content_id needs to
                    match with the
                    ``grounded_content.content_metadata.content_id`` field.
            """

            reference_indices: MutableSequence[int] = proto.RepeatedField(
                proto.INT32,
                number=1,
            )
            content_id: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class Reference(proto.Message):
            r"""Referenced content and related document metadata.

            Attributes:
                content (str):
                    Referenced text content.
                code_snippet (str):
                    Chunk of code snippet from the referenced
                    document.
                document_metadata (google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata):
                    Document metadata.
            """

            class DocumentMetadata(proto.Message):
                r"""Document metadata.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    language (google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata.Language):

                    document (str):
                        Document resource name.

                        This field is a member of `oneof`_ ``_document``.
                    uri (str):
                        URI for the document. It may contain a URL
                        that redirects to the actual website.

                        This field is a member of `oneof`_ ``_uri``.
                    title (str):
                        Title.

                        This field is a member of `oneof`_ ``_title``.
                    page_identifier (str):
                        Page identifier.

                        This field is a member of `oneof`_ ``_page_identifier``.
                    domain (str):
                        Domain name from the document URI. Note that the ``uri``
                        field may contain a URL that redirects to the actual
                        website, in which case this will contain the domain name of
                        the target site.

                        This field is a member of `oneof`_ ``_domain``.
                    mime_type (str):
                        The mime type of the document.
                        https://www.iana.org/assignments/media-types/media-types.xhtml.

                        This field is a member of `oneof`_ ``_mime_type``.
                """

                class Language(proto.Enum):
                    r"""Language of the referenced content. For now, it is only used
                    for code.

                    Values:
                        LANGUAGE_UNSPECIFIED (0):
                            No description available.
                        PYTHON (1):
                            No description available.
                        SQL (2):
                            No description available.
                    """

                    LANGUAGE_UNSPECIFIED = 0
                    PYTHON = 1
                    SQL = 2

                language: "AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata.Language" = proto.Field(
                    proto.ENUM,
                    number=8,
                    enum="AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata.Language",
                )
                document: str = proto.Field(
                    proto.STRING,
                    number=1,
                    optional=True,
                )
                uri: str = proto.Field(
                    proto.STRING,
                    number=2,
                    optional=True,
                )
                title: str = proto.Field(
                    proto.STRING,
                    number=3,
                    optional=True,
                )
                page_identifier: str = proto.Field(
                    proto.STRING,
                    number=4,
                    optional=True,
                )
                domain: str = proto.Field(
                    proto.STRING,
                    number=5,
                    optional=True,
                )
                mime_type: str = proto.Field(
                    proto.STRING,
                    number=7,
                    optional=True,
                )

            content: str = proto.Field(
                proto.STRING,
                number=1,
            )
            code_snippet: str = proto.Field(
                proto.STRING,
                number=4,
            )
            document_metadata: "AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata",
            )

        segments: MutableSequence[
            "AssistantGroundedContent.TextGroundingMetadata.Segment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AssistantGroundedContent.TextGroundingMetadata.Segment",
        )
        visual_segments: MutableSequence[
            "AssistantGroundedContent.TextGroundingMetadata.VisualSegment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="AssistantGroundedContent.TextGroundingMetadata.VisualSegment",
        )
        references: MutableSequence[
            "AssistantGroundedContent.TextGroundingMetadata.Reference"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="AssistantGroundedContent.TextGroundingMetadata.Reference",
        )

    text_grounding_metadata: TextGroundingMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="metadata",
        message=TextGroundingMetadata,
    )
    content: "AssistantContent" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AssistantContent",
    )
    citation_metadata: grounded_generation_service.CitationMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=grounded_generation_service.CitationMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
