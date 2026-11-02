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

from google.cloud.dialogflowcx_v3beta1.types import inline

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "IntentView",
        "Intent",
        "ListIntentsRequest",
        "ListIntentsResponse",
        "GetIntentRequest",
        "CreateIntentRequest",
        "UpdateIntentRequest",
        "DeleteIntentRequest",
        "ImportIntentsRequest",
        "ImportIntentsResponse",
        "ImportIntentsMetadata",
        "ExportIntentsRequest",
        "ExportIntentsResponse",
        "ExportIntentsMetadata",
    },
)


class IntentView(proto.Enum):
    r"""Represents the options for views of an intent.
    An intent can be a sizable object. Therefore, we provide a
    resource view that does not return training phrases in the
    response.

    Values:
        INTENT_VIEW_UNSPECIFIED (0):
            Not specified. Treated as INTENT_VIEW_FULL.
        INTENT_VIEW_PARTIAL (1):
            Training phrases field is not populated in
            the response.
        INTENT_VIEW_FULL (2):
            All fields are populated.
    """

    INTENT_VIEW_UNSPECIFIED = 0
    INTENT_VIEW_PARTIAL = 1
    INTENT_VIEW_FULL = 2


class Intent(proto.Message):
    r"""An intent represents a user's intent to interact with a
    conversational agent.
    You can provide information for the Dialogflow API to use to
    match user input to an intent by adding training phrases (i.e.,
    examples of user input) to your intent.

    Attributes:
        name (str):
            The unique identifier of the intent. Required for the
            [Intents.UpdateIntent][google.cloud.dialogflow.cx.v3beta1.Intents.UpdateIntent]
            method.
            [Intents.CreateIntent][google.cloud.dialogflow.cx.v3beta1.Intents.CreateIntent]
            populates the name automatically. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
        display_name (str):
            Required. The human-readable name of the
            intent, unique within the agent.
        training_phrases (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Intent.TrainingPhrase]):
            The collection of training phrases the agent
            is trained on to identify the intent.
        parameters (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Intent.Parameter]):
            The collection of parameters associated with
            the intent.
        priority (int):
            The priority of this intent. Higher numbers represent higher
            priorities.

            - If the supplied value is unspecified or 0, the service
              translates the value to 500,000, which corresponds to the
              ``Normal`` priority in the console.
            - If the supplied value is negative, the intent is ignored
              in runtime detect intent requests.
        is_fallback (bool):
            Indicates whether this is a fallback intent.
            Currently only default fallback intent is
            allowed in the agent, which is added upon agent
            creation.
            Adding training phrases to fallback intent is
            useful in the case of requests that are
            mistakenly matched, since training phrases
            assigned to fallback intents act as negative
            examples that triggers no-match event.
        labels (MutableMapping[str, str]):
            The key/value metadata to label an intent. Labels can
            contain lowercase letters, digits and the symbols '-' and
            '\_'. International characters are allowed, including
            letters from unicase alphabets. Keys must start with a
            letter. Keys and values can be no longer than 63 characters
            and no more than 128 bytes.

            Prefix "sys-" is reserved for Dialogflow defined labels.
            Currently allowed Dialogflow defined labels include:

            - sys-head
            - sys-contextual The above labels do not require value.
              "sys-head" means the intent is a head intent.
              "sys-contextual" means the intent is a contextual intent.
        description (str):
            Human readable description for better
            understanding an intent like its scope, content,
            result etc. Maximum character limit: 1000
            characters.
        dtmf_pattern (str):
            Optional. Matching DTMF pattern for the
            intent.
    """

    class TrainingPhrase(proto.Message):
        r"""Represents an example that the agent is trained on to
        identify the intent.

        Attributes:
            id (str):
                Output only. The unique identifier of the
                training phrase.
            parts (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Intent.TrainingPhrase.Part]):
                Required. The ordered list of training phrase parts. The
                parts are concatenated in order to form the training phrase.

                Note: The API does not automatically annotate training
                phrases like the Dialogflow Console does.

                Note: Do not forget to include whitespace at part
                boundaries, so the training phrase is well formatted when
                the parts are concatenated.

                If the training phrase does not need to be annotated with
                parameters, you just need a single part with only the
                [Part.text][google.cloud.dialogflow.cx.v3beta1.Intent.TrainingPhrase.Part.text]
                field set.

                If you want to annotate the training phrase, you must create
                multiple parts, where the fields of each part are populated
                in one of two ways:

                - ``Part.text`` is set to a part of the phrase that has no
                  parameters.
                - ``Part.text`` is set to a part of the phrase that you want
                  to annotate, and the ``parameter_id`` field is set.
            repeat_count (int):
                Indicates how many times this example was
                added to the intent.
        """

        class Part(proto.Message):
            r"""Represents a part of a training phrase.

            Attributes:
                text (str):
                    Required. The text for this part.
                parameter_id (str):
                    The
                    [parameter][google.cloud.dialogflow.cx.v3beta1.Intent.Parameter]
                    used to annotate this part of the training phrase. This
                    field is required for annotated parts of the training
                    phrase.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            parameter_id: str = proto.Field(
                proto.STRING,
                number=2,
            )

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        parts: MutableSequence["Intent.TrainingPhrase.Part"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Intent.TrainingPhrase.Part",
        )
        repeat_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class Parameter(proto.Message):
        r"""Represents an intent parameter.

        Attributes:
            id (str):
                Required. The unique identifier of the parameter. This field
                is used by [training
                phrases][google.cloud.dialogflow.cx.v3beta1.Intent.TrainingPhrase]
                to annotate their
                [parts][google.cloud.dialogflow.cx.v3beta1.Intent.TrainingPhrase.Part].
            entity_type (str):
                Required. The entity type of the parameter. Format:
                ``projects/-/locations/-/agents/-/entityTypes/<SystemEntityTypeID>``
                for system entity types (for example,
                ``projects/-/locations/-/agents/-/entityTypes/sys.date``),
                or
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>``
                for developer entity types.
            is_list (bool):
                Indicates whether the parameter represents a
                list of values.
            redact (bool):
                Indicates whether the parameter content should be redacted
                in log. If redaction is enabled, the parameter content will
                be replaced by parameter name during logging. Note: the
                parameter content is subject to redaction if either
                parameter level redaction or [entity type level
                redaction][google.cloud.dialogflow.cx.v3beta1.EntityType.redact]
                is enabled.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        entity_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        is_list: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        redact: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    training_phrases: MutableSequence[TrainingPhrase] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=TrainingPhrase,
    )
    parameters: MutableSequence[Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Parameter,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=5,
    )
    is_fallback: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    dtmf_pattern: str = proto.Field(
        proto.STRING,
        number=16,
    )


class ListIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.ListIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ListIntents].

    Attributes:
        parent (str):
            Required. The agent to list all intents for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        language_code (str):
            The language to list intents for. The following fields are
            language dependent:

            - ``Intent.training_phrases.parts.text``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
        intent_view (google.cloud.dialogflowcx_v3beta1.types.IntentView):
            The resource view to apply to the returned
            intent.
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
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="IntentView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListIntentsResponse(proto.Message):
    r"""The response message for
    [Intents.ListIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ListIntents].

    Attributes:
        intents (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Intent]):
            The list of intents. There will be a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    intents: MutableSequence["Intent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Intent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetIntentRequest(proto.Message):
    r"""The request message for
    [Intents.GetIntent][google.cloud.dialogflow.cx.v3beta1.Intents.GetIntent].

    Attributes:
        name (str):
            Required. The name of the intent. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
        language_code (str):
            The language to retrieve the intent for. The following
            fields are language dependent:

            - ``Intent.training_phrases.parts.text``

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


class CreateIntentRequest(proto.Message):
    r"""The request message for
    [Intents.CreateIntent][google.cloud.dialogflow.cx.v3beta1.Intents.CreateIntent].

    Attributes:
        parent (str):
            Required. The agent to create an intent for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        intent (google.cloud.dialogflowcx_v3beta1.types.Intent):
            Required. The intent to create.
        language_code (str):
            The language of the following fields in ``intent``:

            - ``Intent.training_phrases.parts.text``

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
    intent: "Intent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Intent",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateIntentRequest(proto.Message):
    r"""The request message for
    [Intents.UpdateIntent][google.cloud.dialogflow.cx.v3beta1.Intents.UpdateIntent].

    Attributes:
        intent (google.cloud.dialogflowcx_v3beta1.types.Intent):
            Required. The intent to update.
        language_code (str):
            The language of the following fields in ``intent``:

            - ``Intent.training_phrases.parts.text``

            If not specified, the agent's default language is used.
            `Many
            languages <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    intent: "Intent" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Intent",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteIntentRequest(proto.Message):
    r"""The request message for
    [Intents.DeleteIntent][google.cloud.dialogflow.cx.v3beta1.Intents.DeleteIntent].

    Attributes:
        name (str):
            Required. The name of the intent to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.ImportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ImportIntents].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The agent to import the intents into. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        intents_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            import intents from. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a read operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have read permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``intents``.
        intents_content (google.cloud.dialogflowcx_v3beta1.types.InlineSource):
            Uncompressed byte content of intents.

            This field is a member of `oneof`_ ``intents``.
        merge_option (google.cloud.dialogflowcx_v3beta1.types.ImportIntentsRequest.MergeOption):
            Merge option for importing intents. If not specified,
            ``REJECT`` is assumed.
    """

    class MergeOption(proto.Enum):
        r"""Merge option when display name conflicts exist during import.

        Values:
            MERGE_OPTION_UNSPECIFIED (0):
                Unspecified. Should not be used.
            REJECT (1):
                DEPRECATED: Please use
                [REPORT_CONFLICT][ImportIntentsRequest.REPORT_CONFLICT]
                instead. Fail the request if there are intents whose display
                names conflict with the display names of intents in the
                agent.
            REPLACE (2):
                Replace the original intent in the agent with
                the new intent when display name conflicts
                exist.
            MERGE (3):
                Merge the original intent with the new intent
                when display name conflicts exist.
            RENAME (4):
                Create new intents with new display names to
                differentiate them from the existing intents
                when display name conflicts exist.
            REPORT_CONFLICT (5):
                Report conflict information if display names
                conflict is detected. Otherwise, import intents.
            KEEP (6):
                Keep the original intent and discard the
                conflicting new intent when display name
                conflicts exist.
        """

        MERGE_OPTION_UNSPECIFIED = 0
        REJECT = 1
        REPLACE = 2
        MERGE = 3
        RENAME = 4
        REPORT_CONFLICT = 5
        KEEP = 6

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    intents_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="intents",
    )
    intents_content: inline.InlineSource = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="intents",
        message=inline.InlineSource,
    )
    merge_option: MergeOption = proto.Field(
        proto.ENUM,
        number=4,
        enum=MergeOption,
    )


class ImportIntentsResponse(proto.Message):
    r"""The response message for
    [Intents.ImportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ImportIntents].

    Attributes:
        intents (MutableSequence[str]):
            The unique identifier of the imported intents. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
        conflicting_resources (google.cloud.dialogflowcx_v3beta1.types.ImportIntentsResponse.ConflictingResources):
            Info which resources have conflicts when
            [REPORT_CONFLICT][ImportIntentsResponse.REPORT_CONFLICT]
            merge_option is set in ImportIntentsRequest.
    """

    class ConflictingResources(proto.Message):
        r"""Conflicting resources detected during the import process. Only
        filled when [REPORT_CONFLICT][ImportIntentsResponse.REPORT_CONFLICT]
        is set in the request and there are conflicts in the display names.

        Attributes:
            intent_display_names (MutableSequence[str]):
                Display names of conflicting intents.
            entity_display_names (MutableSequence[str]):
                Display names of conflicting entities.
        """

        intent_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        entity_display_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    intents: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    conflicting_resources: ConflictingResources = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ConflictingResources,
    )


class ImportIntentsMetadata(proto.Message):
    r"""Metadata returned for the
    [Intents.ImportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ImportIntents]
    long running operation.

    """


class ExportIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.ExportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ExportIntents].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The name of the parent agent to export intents.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        intents (MutableSequence[str]):
            Required. The name of the intents to export. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
        intents_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the intents to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``destination``.
        intents_content_inline (bool):
            Optional. The option to return the serialized
            intents inline.

            This field is a member of `oneof`_ ``destination``.
        data_format (google.cloud.dialogflowcx_v3beta1.types.ExportIntentsRequest.DataFormat):
            Optional. The data format of the exported intents. If not
            specified, ``BLOB`` is assumed.
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported intents.

        Values:
            DATA_FORMAT_UNSPECIFIED (0):
                Unspecified format. Treated as ``BLOB``.
            BLOB (1):
                Intents will be exported as raw bytes.
            JSON (2):
                Intents will be exported in JSON format.
            CSV (3):
                Intents will be exported in CSV format.
        """

        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1
        JSON = 2
        CSV = 3

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    intents: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    intents_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="destination",
    )
    intents_content_inline: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="destination",
    )
    data_format: DataFormat = proto.Field(
        proto.ENUM,
        number=5,
        enum=DataFormat,
    )


class ExportIntentsResponse(proto.Message):
    r"""The response message for
    [Intents.ExportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ExportIntents].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        intents_uri (str):
            The URI to a file containing the exported intents. This
            field is populated only if ``intents_uri`` is specified in
            [ExportIntentsRequest][google.cloud.dialogflow.cx.v3beta1.ExportIntentsRequest].

            This field is a member of `oneof`_ ``intents``.
        intents_content (google.cloud.dialogflowcx_v3beta1.types.InlineDestination):
            Uncompressed byte content for intents. This field is
            populated only if ``intents_content_inline`` is set to true
            in
            [ExportIntentsRequest][google.cloud.dialogflow.cx.v3beta1.ExportIntentsRequest].

            This field is a member of `oneof`_ ``intents``.
    """

    intents_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="intents",
    )
    intents_content: inline.InlineDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="intents",
        message=inline.InlineDestination,
    )


class ExportIntentsMetadata(proto.Message):
    r"""Metadata returned for the
    [Intents.ExportIntents][google.cloud.dialogflow.cx.v3beta1.Intents.ExportIntents]
    long running operation.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
