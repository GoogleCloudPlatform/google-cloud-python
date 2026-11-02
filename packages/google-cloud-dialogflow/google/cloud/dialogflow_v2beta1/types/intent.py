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

from google.cloud.dialogflow_v2beta1.types import context

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "IntentView",
        "Intent",
        "ListIntentsRequest",
        "ListIntentsResponse",
        "GetIntentRequest",
        "CreateIntentRequest",
        "UpdateIntentRequest",
        "DeleteIntentRequest",
        "BatchUpdateIntentsRequest",
        "BatchUpdateIntentsResponse",
        "BatchDeleteIntentsRequest",
        "IntentBatch",
    },
)


class IntentView(proto.Enum):
    r"""Represents the options for views of an intent.
    An intent can be a sizable object. Therefore, we provide a
    resource view that does not return training phrases in the
    response by default.

    Values:
        INTENT_VIEW_UNSPECIFIED (0):
            Training phrases field is not populated in
            the response.
        INTENT_VIEW_FULL (1):
            All fields are populated.
    """

    INTENT_VIEW_UNSPECIFIED = 0
    INTENT_VIEW_FULL = 1


class Intent(proto.Message):
    r"""An intent categorizes an end-user's intention for one conversation
    turn. For each agent, you define many intents, where your combined
    intents can handle a complete conversation. When an end-user writes
    or says something, referred to as an end-user expression or end-user
    input, Dialogflow matches the end-user input to the best intent in
    your agent. Matching an intent is also known as intent
    classification.

    For more information, see the `intent
    guide <https://cloud.google.com/dialogflow/docs/intents-overview>`__.

    Attributes:
        name (str):
            Optional. The unique identifier of this intent. Required for
            [Intents.UpdateIntent][google.cloud.dialogflow.v2beta1.Intents.UpdateIntent]
            and
            [Intents.BatchUpdateIntents][google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents]
            methods. Supported formats:

            - ``projects/<Project ID>/agent/intents/<Intent ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>``
        display_name (str):
            Required. The name of this intent.
        webhook_state (google.cloud.dialogflow_v2beta1.types.Intent.WebhookState):
            Optional. Indicates whether webhooks are
            enabled for the intent.
        priority (int):
            Optional. The priority of this intent. Higher numbers
            represent higher priorities.

            - If the supplied value is unspecified or 0, the service
              translates the value to 500,000, which corresponds to the
              ``Normal`` priority in the console.
            - If the supplied value is negative, the intent is ignored
              in runtime detect intent requests.
        is_fallback (bool):
            Optional. Indicates whether this is a
            fallback intent.
        ml_enabled (bool):
            Optional. Indicates whether Machine Learning is enabled for
            the intent. Note: If ``ml_enabled`` setting is set to false,
            then this intent is not taken into account during inference
            in ``ML ONLY`` match mode. Also, auto-markup in the UI is
            turned off. DEPRECATED! Please use ``ml_disabled`` field
            instead. NOTE: If both ``ml_enabled`` and ``ml_disabled``
            are either not set or false, then the default value is
            determined as follows:

            - Before April 15th, 2018 the default is: ml_enabled = false
              / ml_disabled = true.
            - After April 15th, 2018 the default is: ml_enabled = true /
              ml_disabled = false.
        ml_disabled (bool):
            Optional. Indicates whether Machine Learning is disabled for
            the intent. Note: If ``ml_disabled`` setting is set to true,
            then this intent is not taken into account during inference
            in ``ML ONLY`` match mode. Also, auto-markup in the UI is
            turned off.
        live_agent_handoff (bool):
            Optional. Indicates that a live agent should be brought in
            to handle the interaction with the user. In most cases, when
            you set this flag to true, you would also want to set
            end_interaction to true as well. Default is false.
        end_interaction (bool):
            Optional. Indicates that this intent ends an
            interaction. Some integrations (e.g., Actions on
            Google or Dialogflow phone gateway) use this
            information to close interaction with an end
            user. Default is false.
        input_context_names (MutableSequence[str]):
            Optional. The list of context names required for this intent
            to be triggered. Formats:

            - ``projects/<Project ID>/agent/sessions/-/contexts/<Context ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/sessions/-/contexts/<Context ID>``
        events (MutableSequence[str]):
            Optional. The collection of event names that
            trigger the intent. If the collection of input
            contexts is not empty, all of the contexts must
            be present in the active user session for an
            event to trigger this intent. Event names are
            limited to 150 characters.
        training_phrases (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase]):
            Optional. The collection of examples that the
            agent is trained on.
        action (str):
            Optional. The name of the action associated
            with the intent. Note: The action name must not
            contain whitespaces.
        output_contexts (MutableSequence[google.cloud.dialogflow_v2beta1.types.Context]):
            Optional. The collection of contexts that are activated when
            the intent is matched. Context messages in this collection
            should not set the parameters field. Setting the
            ``lifespan_count`` to 0 will reset the context when the
            intent is matched. Format:
            ``projects/<Project ID>/agent/sessions/-/contexts/<Context ID>``.
        reset_contexts (bool):
            Optional. Indicates whether to delete all
            contexts in the current session when this intent
            is matched.
        parameters (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Parameter]):
            Optional. The collection of parameters
            associated with the intent.
        messages (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message]):
            Optional. The collection of rich messages corresponding to
            the ``Response`` field in the Dialogflow console.
        default_response_platforms (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.Platform]):
            Optional. The list of platforms for which the first
            responses will be copied from the messages in
            PLATFORM_UNSPECIFIED (i.e. default platform).
        root_followup_intent_name (str):
            Output only. The unique identifier of the root intent in the
            chain of followup intents. It identifies the correct
            followup intents chain for this intent.

            Format: ``projects/<Project ID>/agent/intents/<Intent ID>``.
        parent_followup_intent_name (str):
            Optional. The unique identifier of the parent intent in the
            chain of followup intents. You can set this field when
            creating an intent, for example with
            [CreateIntent][google.cloud.dialogflow.v2beta1.Intents.CreateIntent]
            or
            [BatchUpdateIntents][google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents],
            in order to make this intent a followup intent.

            It identifies the parent followup intent. Format:
            ``projects/<Project ID>/agent/intents/<Intent ID>``.
        followup_intent_info (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.FollowupIntentInfo]):
            Output only. Information about all followup
            intents that have this intent as a direct or
            indirect parent. We populate this field only in
            the output.
    """

    class WebhookState(proto.Enum):
        r"""Represents the different states that webhooks can be in.

        Values:
            WEBHOOK_STATE_UNSPECIFIED (0):
                Webhook is disabled in the agent and in the
                intent.
            WEBHOOK_STATE_ENABLED (1):
                Webhook is enabled in the agent and in the
                intent.
            WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING (2):
                Webhook is enabled in the agent and in the
                intent. Also, each slot filling prompt is
                forwarded to the webhook.
        """

        WEBHOOK_STATE_UNSPECIFIED = 0
        WEBHOOK_STATE_ENABLED = 1
        WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING = 2

    class TrainingPhrase(proto.Message):
        r"""Represents an example that the agent is trained on.

        Attributes:
            name (str):
                Output only. The unique identifier of this
                training phrase.
            type_ (google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase.Type):
                Required. The type of the training phrase.
            parts (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase.Part]):
                Required. The ordered list of training phrase parts. The
                parts are concatenated in order to form the training phrase.

                Note: The API does not automatically annotate training
                phrases like the Dialogflow Console does.

                Note: Do not forget to include whitespace at part
                boundaries, so the training phrase is well formatted when
                the parts are concatenated.

                If the training phrase does not need to be annotated with
                parameters, you just need a single part with only the
                [Part.text][google.cloud.dialogflow.v2beta1.Intent.TrainingPhrase.Part.text]
                field set.

                If you want to annotate the training phrase, you must create
                multiple parts, where the fields of each part are populated
                in one of two ways:

                - ``Part.text`` is set to a part of the phrase that has no
                  parameters.
                - ``Part.text`` is set to a part of the phrase that you want
                  to annotate, and the ``entity_type``, ``alias``, and
                  ``user_defined`` fields are all set.
            times_added_count (int):
                Optional. Indicates how many times this
                example was added to the intent. Each time a
                developer adds an existing sample by editing an
                intent or training, this counter is increased.
        """

        class Type(proto.Enum):
            r"""Represents different types of training phrases.

            Values:
                TYPE_UNSPECIFIED (0):
                    Not specified. This value should never be
                    used.
                EXAMPLE (1):
                    Examples do not contain @-prefixed entity
                    type names, but example parts can be annotated
                    with entity types.
                TEMPLATE (2):
                    Templates are not annotated with entity
                    types, but they can contain @-prefixed entity
                    type names as substrings. Note: Template mode
                    has been deprecated. Example mode is the only
                    supported way to create new training phrases. If
                    you have existing training phrases in template
                    mode, they will be removed during training and
                    it can cause a drop in agent performance.
            """

            TYPE_UNSPECIFIED = 0
            EXAMPLE = 1
            TEMPLATE = 2

        class Part(proto.Message):
            r"""Represents a part of a training phrase.

            Attributes:
                text (str):
                    Required. The text for this part.
                entity_type (str):
                    Optional. The entity type name prefixed with ``@``. This
                    field is required for annotated parts of the training
                    phrase.
                alias (str):
                    Optional. The parameter name for the value
                    extracted from the annotated part of the
                    example. This field is required for annotated
                    parts of the training phrase.
                user_defined (bool):
                    Optional. Indicates whether the text was
                    manually annotated. This field is set to true
                    when the Dialogflow Console is used to manually
                    annotate the part. When creating an annotated
                    part with the API, you must set this to true.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            entity_type: str = proto.Field(
                proto.STRING,
                number=2,
            )
            alias: str = proto.Field(
                proto.STRING,
                number=3,
            )
            user_defined: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Intent.TrainingPhrase.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Intent.TrainingPhrase.Type",
        )
        parts: MutableSequence["Intent.TrainingPhrase.Part"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="Intent.TrainingPhrase.Part",
        )
        times_added_count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class Parameter(proto.Message):
        r"""Represents intent parameters.

        Attributes:
            name (str):
                The unique identifier of this parameter.
            display_name (str):
                Required. The name of the parameter.
            value (str):
                Optional. The definition of the parameter value. It can be:

                - a constant string,
                - a parameter value defined as ``$parameter_name``,
                - an original parameter value defined as
                  ``$parameter_name.original``,
                - a parameter value from some context defined as
                  ``#context_name.parameter_name``.
            default_value (str):
                Optional. The default value to use when the ``value`` yields
                an empty result. Default values can be extracted from
                contexts by using the following syntax:
                ``#context_name.parameter_name``.
            entity_type_display_name (str):
                Optional. The name of the entity type, prefixed with ``@``,
                that describes values of the parameter. If the parameter is
                required, this must be provided.
            mandatory (bool):
                Optional. Indicates whether the parameter is
                required. That is, whether the intent cannot be
                completed without collecting the parameter
                value.
            prompts (MutableSequence[str]):
                Optional. The collection of prompts that the
                agent can present to the user in order to
                collect a value for the parameter.
            is_list (bool):
                Optional. Indicates whether the parameter
                represents a list of values.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        value: str = proto.Field(
            proto.STRING,
            number=3,
        )
        default_value: str = proto.Field(
            proto.STRING,
            number=4,
        )
        entity_type_display_name: str = proto.Field(
            proto.STRING,
            number=5,
        )
        mandatory: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        prompts: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        is_list: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class Message(proto.Message):
        r"""Corresponds to the ``Response`` field in the Dialogflow console.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text (google.cloud.dialogflow_v2beta1.types.Intent.Message.Text):
                Returns a text response.

                This field is a member of `oneof`_ ``message``.
            image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                Displays an image.

                This field is a member of `oneof`_ ``message``.
            quick_replies (google.cloud.dialogflow_v2beta1.types.Intent.Message.QuickReplies):
                Displays quick replies.

                This field is a member of `oneof`_ ``message``.
            card (google.cloud.dialogflow_v2beta1.types.Intent.Message.Card):
                Displays a card.

                This field is a member of `oneof`_ ``message``.
            payload (google.protobuf.struct_pb2.Struct):
                A custom platform-specific response.

                This field is a member of `oneof`_ ``message``.
            simple_responses (google.cloud.dialogflow_v2beta1.types.Intent.Message.SimpleResponses):
                Returns a voice or text-only response for
                Actions on Google.

                This field is a member of `oneof`_ ``message``.
            basic_card (google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard):
                Displays a basic card for Actions on Google.

                This field is a member of `oneof`_ ``message``.
            suggestions (google.cloud.dialogflow_v2beta1.types.Intent.Message.Suggestions):
                Displays suggestion chips for Actions on
                Google.

                This field is a member of `oneof`_ ``message``.
            link_out_suggestion (google.cloud.dialogflow_v2beta1.types.Intent.Message.LinkOutSuggestion):
                Displays a link out suggestion chip for
                Actions on Google.

                This field is a member of `oneof`_ ``message``.
            list_select (google.cloud.dialogflow_v2beta1.types.Intent.Message.ListSelect):
                Displays a list card for Actions on Google.

                This field is a member of `oneof`_ ``message``.
            carousel_select (google.cloud.dialogflow_v2beta1.types.Intent.Message.CarouselSelect):
                Displays a carousel card for Actions on
                Google.

                This field is a member of `oneof`_ ``message``.
            telephony_play_audio (google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonyPlayAudio):
                Plays audio from a file in Telephony Gateway.

                This field is a member of `oneof`_ ``message``.
            telephony_synthesize_speech (google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonySynthesizeSpeech):
                Synthesizes speech in Telephony Gateway.

                This field is a member of `oneof`_ ``message``.
            telephony_transfer_call (google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonyTransferCall):
                Transfers the call in Telephony Gateway.

                This field is a member of `oneof`_ ``message``.
            rbm_text (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmText):
                Rich Business Messaging (RBM) text response.

                RBM allows businesses to send enriched and
                branded versions of SMS. See
                https://jibe.google.com/business-messaging.

                This field is a member of `oneof`_ ``message``.
            rbm_standalone_rich_card (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard):
                Standalone Rich Business Messaging (RBM) rich
                card response.

                This field is a member of `oneof`_ ``message``.
            rbm_carousel_rich_card (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCarouselCard):
                Rich Business Messaging (RBM) carousel rich
                card response.

                This field is a member of `oneof`_ ``message``.
            browse_carousel_card (google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard):
                Browse carousel card for Actions on Google.

                This field is a member of `oneof`_ ``message``.
            table_card (google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCard):
                Table card for Actions on Google.

                This field is a member of `oneof`_ ``message``.
            media_content (google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent):
                The media content card for Actions on Google.

                This field is a member of `oneof`_ ``message``.
            platform (google.cloud.dialogflow_v2beta1.types.Intent.Message.Platform):
                Optional. The platform that this message is
                intended for.
        """

        class Platform(proto.Enum):
            r"""Represents different platforms that a rich message can be
            intended for.

            Values:
                PLATFORM_UNSPECIFIED (0):
                    Not specified.
                FACEBOOK (1):
                    Facebook.
                SLACK (2):
                    Slack.
                TELEGRAM (3):
                    Telegram.
                KIK (4):
                    Kik.
                SKYPE (5):
                    Skype.
                LINE (6):
                    Line.
                VIBER (7):
                    Viber.
                ACTIONS_ON_GOOGLE (8):
                    Google Assistant See `Dialogflow webhook
                    format <https://developers.google.com/assistant/actions/build/json/dialogflow-webhook-json>`__
                TELEPHONY (10):
                    Telephony Gateway.
                GOOGLE_HANGOUTS (11):
                    Google Hangouts.
            """

            PLATFORM_UNSPECIFIED = 0
            FACEBOOK = 1
            SLACK = 2
            TELEGRAM = 3
            KIK = 4
            SKYPE = 5
            LINE = 6
            VIBER = 7
            ACTIONS_ON_GOOGLE = 8
            TELEPHONY = 10
            GOOGLE_HANGOUTS = 11

        class Text(proto.Message):
            r"""The text response message.

            Attributes:
                text (MutableSequence[str]):
                    Optional. The collection of the agent's
                    responses.
            """

            text: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class Image(proto.Message):
            r"""The image response message.

            Attributes:
                image_uri (str):
                    Optional. The public URI to an image file.
                accessibility_text (str):
                    A text description of the image to be used for
                    accessibility, e.g., screen readers. Required if image_uri
                    is set for CarouselSelect.
            """

            image_uri: str = proto.Field(
                proto.STRING,
                number=1,
            )
            accessibility_text: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class QuickReplies(proto.Message):
            r"""The quick replies response message.

            Attributes:
                title (str):
                    Optional. The title of the collection of
                    quick replies.
                quick_replies (MutableSequence[str]):
                    Optional. The collection of quick replies.
            """

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            quick_replies: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        class Card(proto.Message):
            r"""The card response message.

            Attributes:
                title (str):
                    Optional. The title of the card.
                subtitle (str):
                    Optional. The subtitle of the card.
                image_uri (str):
                    Optional. The public URI to an image file for
                    the card.
                buttons (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.Card.Button]):
                    Optional. The collection of card buttons.
            """

            class Button(proto.Message):
                r"""Optional. Contains information about a button.

                Attributes:
                    text (str):
                        Optional. The text to show on the button.
                    postback (str):
                        Optional. The text to send back to the
                        Dialogflow API or a URI to open.
                """

                text: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                postback: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            subtitle: str = proto.Field(
                proto.STRING,
                number=2,
            )
            image_uri: str = proto.Field(
                proto.STRING,
                number=3,
            )
            buttons: MutableSequence["Intent.Message.Card.Button"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.Card.Button",
                )
            )

        class SimpleResponse(proto.Message):
            r"""The simple response message containing speech or text.

            Attributes:
                text_to_speech (str):
                    One of text_to_speech or ssml must be provided. The plain
                    text of the speech output. Mutually exclusive with ssml.
                ssml (str):
                    One of text_to_speech or ssml must be provided. Structured
                    spoken response to the user in the SSML format. Mutually
                    exclusive with text_to_speech.
                display_text (str):
                    Optional. The text to display.
            """

            text_to_speech: str = proto.Field(
                proto.STRING,
                number=1,
            )
            ssml: str = proto.Field(
                proto.STRING,
                number=2,
            )
            display_text: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class SimpleResponses(proto.Message):
            r"""The collection of simple response candidates. This message in
            ``QueryResult.fulfillment_messages`` and
            ``WebhookResponse.fulfillment_messages`` should contain only one
            ``SimpleResponse``.

            Attributes:
                simple_responses (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.SimpleResponse]):
                    Required. The list of simple responses.
            """

            simple_responses: MutableSequence["Intent.Message.SimpleResponse"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.SimpleResponse",
                )
            )

        class BasicCard(proto.Message):
            r"""The basic card message. Useful for displaying information.

            Attributes:
                title (str):
                    Optional. The title of the card.
                subtitle (str):
                    Optional. The subtitle of the card.
                formatted_text (str):
                    Required, unless image is present. The body
                    text of the card.
                image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                    Optional. The image for the card.
                buttons (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard.Button]):
                    Optional. The collection of card buttons.
            """

            class Button(proto.Message):
                r"""The button object that appears at the bottom of a card.

                Attributes:
                    title (str):
                        Required. The title of the button.
                    open_uri_action (google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard.Button.OpenUriAction):
                        Required. Action to take when a user taps on
                        the button.
                """

                class OpenUriAction(proto.Message):
                    r"""Opens the given URI.

                    Attributes:
                        uri (str):
                            Required. The HTTP or HTTPS scheme URI.
                    """

                    uri: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )

                title: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                open_uri_action: "Intent.Message.BasicCard.Button.OpenUriAction" = (
                    proto.Field(
                        proto.MESSAGE,
                        number=2,
                        message="Intent.Message.BasicCard.Button.OpenUriAction",
                    )
                )

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            subtitle: str = proto.Field(
                proto.STRING,
                number=2,
            )
            formatted_text: str = proto.Field(
                proto.STRING,
                number=3,
            )
            image: "Intent.Message.Image" = proto.Field(
                proto.MESSAGE,
                number=4,
                message="Intent.Message.Image",
            )
            buttons: MutableSequence["Intent.Message.BasicCard.Button"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=5,
                    message="Intent.Message.BasicCard.Button",
                )
            )

        class Suggestion(proto.Message):
            r"""The suggestion chip message that the user can tap to quickly
            post a reply to the conversation.

            Attributes:
                title (str):
                    Required. The text shown the in the
                    suggestion chip.
            """

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class Suggestions(proto.Message):
            r"""The collection of suggestions.

            Attributes:
                suggestions (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.Suggestion]):
                    Required. The list of suggested replies.
            """

            suggestions: MutableSequence["Intent.Message.Suggestion"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.Suggestion",
                )
            )

        class LinkOutSuggestion(proto.Message):
            r"""The suggestion chip message that allows the user to jump out
            to the app or website associated with this agent.

            Attributes:
                destination_name (str):
                    Required. The name of the app or site this
                    chip is linking to.
                uri (str):
                    Required. The URI of the app or site to open
                    when the user taps the suggestion chip.
            """

            destination_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            uri: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class ListSelect(proto.Message):
            r"""The card for presenting a list of options to select from.

            Attributes:
                title (str):
                    Optional. The overall title of the list.
                items (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.ListSelect.Item]):
                    Required. List items.
                subtitle (str):
                    Optional. Subtitle of the list.
            """

            class Item(proto.Message):
                r"""An item in the list.

                Attributes:
                    info (google.cloud.dialogflow_v2beta1.types.Intent.Message.SelectItemInfo):
                        Required. Additional information about this
                        option.
                    title (str):
                        Required. The title of the list item.
                    description (str):
                        Optional. The main text describing the item.
                    image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                        Optional. The image to display.
                """

                info: "Intent.Message.SelectItemInfo" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.SelectItemInfo",
                )
                title: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                description: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                image: "Intent.Message.Image" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.Image",
                )

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            items: MutableSequence["Intent.Message.ListSelect.Item"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="Intent.Message.ListSelect.Item",
                )
            )
            subtitle: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class CarouselSelect(proto.Message):
            r"""The card for presenting a carousel of options to select from.

            Attributes:
                items (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.CarouselSelect.Item]):
                    Required. Carousel items.
            """

            class Item(proto.Message):
                r"""An item in the carousel.

                Attributes:
                    info (google.cloud.dialogflow_v2beta1.types.Intent.Message.SelectItemInfo):
                        Required. Additional info about the option
                        item.
                    title (str):
                        Required. Title of the carousel item.
                    description (str):
                        Optional. The body text of the card.
                    image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                        Optional. The image to display.
                """

                info: "Intent.Message.SelectItemInfo" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.SelectItemInfo",
                )
                title: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                description: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                image: "Intent.Message.Image" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.Image",
                )

            items: MutableSequence["Intent.Message.CarouselSelect.Item"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.CarouselSelect.Item",
                )
            )

        class SelectItemInfo(proto.Message):
            r"""Additional info about the select item for when it is
            triggered in a dialog.

            Attributes:
                key (str):
                    Required. A unique key that will be sent back
                    to the agent if this response is given.
                synonyms (MutableSequence[str]):
                    Optional. A list of synonyms that can also be
                    used to trigger this item in dialog.
            """

            key: str = proto.Field(
                proto.STRING,
                number=1,
            )
            synonyms: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        class TelephonyPlayAudio(proto.Message):
            r"""Plays audio from a file in Telephony Gateway.

            Attributes:
                audio_uri (str):
                    Required. URI to a Google Cloud Storage object containing
                    the audio to play, e.g., "gs://bucket/object". The object
                    must contain a single channel (mono) of linear PCM audio (2
                    bytes / sample) at 8kHz.

                    This object must be readable by the
                    ``service-<Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com``
                    service account where is the number of the Telephony Gateway
                    project (usually the same as the Dialogflow agent project).
                    If the Google Cloud Storage bucket is in the Telephony
                    Gateway project, this permission is added by default when
                    enabling the Dialogflow V2 API.

                    For audio from other sources, consider using the
                    ``TelephonySynthesizeSpeech`` message with SSML.
            """

            audio_uri: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class TelephonySynthesizeSpeech(proto.Message):
            r"""Synthesizes speech and plays back the synthesized audio to the
            caller in Telephony Gateway.

            Telephony Gateway takes the synthesizer settings from
            ``DetectIntentResponse.output_audio_config`` which can either be set
            at request-level or can come from the agent-level synthesizer
            config.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                text (str):
                    The raw text to be synthesized.

                    This field is a member of `oneof`_ ``source``.
                ssml (str):
                    The SSML to be synthesized. For more information, see
                    `SSML <https://developers.google.com/actions/reference/ssml>`__.

                    This field is a member of `oneof`_ ``source``.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="source",
            )
            ssml: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="source",
            )

        class TelephonyTransferCall(proto.Message):
            r"""Transfers the call in Telephony Gateway.

            Attributes:
                phone_number (str):
                    Required. The phone number to transfer the call to in `E.164
                    format <https://en.wikipedia.org/wiki/E.164>`__.

                    We currently only allow transferring to US numbers
                    (+1xxxyyyzzzz).
            """

            phone_number: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class RbmText(proto.Message):
            r"""Rich Business Messaging (RBM) text response with suggestions.

            Attributes:
                text (str):
                    Required. Text sent and displayed to the
                    user.
                rbm_suggestion (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestion]):
                    Optional. One or more suggestions to show to
                    the user.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            rbm_suggestion: MutableSequence["Intent.Message.RbmSuggestion"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="Intent.Message.RbmSuggestion",
                )
            )

        class RbmCarouselCard(proto.Message):
            r"""Carousel Rich Business Messaging (RBM) rich card.

            Rich cards allow you to respond to users with more vivid content,
            e.g. with media and suggestions.

            If you want to show a single card with more control over the layout,
            please use
            [RbmStandaloneCard][google.cloud.dialogflow.v2beta1.Intent.Message.RbmStandaloneCard]
            instead.

            Attributes:
                card_width (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCarouselCard.CardWidth):
                    Required. The width of the cards in the
                    carousel.
                card_contents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent]):
                    Required. The cards in the carousel. A
                    carousel must have at least 2 cards and at most
                    10.
            """

            class CardWidth(proto.Enum):
                r"""The width of the cards in the carousel.

                Values:
                    CARD_WIDTH_UNSPECIFIED (0):
                        Not specified.
                    SMALL (1):
                        120 DP. Note that tall media cannot be used.
                    MEDIUM (2):
                        232 DP.
                """

                CARD_WIDTH_UNSPECIFIED = 0
                SMALL = 1
                MEDIUM = 2

            card_width: "Intent.Message.RbmCarouselCard.CardWidth" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Intent.Message.RbmCarouselCard.CardWidth",
            )
            card_contents: MutableSequence["Intent.Message.RbmCardContent"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="Intent.Message.RbmCardContent",
                )
            )

        class RbmStandaloneCard(proto.Message):
            r"""Standalone Rich Business Messaging (RBM) rich card.

            Rich cards allow you to respond to users with more vivid content,
            e.g. with media and suggestions.

            You can group multiple rich cards into one using
            [RbmCarouselCard][google.cloud.dialogflow.v2beta1.Intent.Message.RbmCarouselCard]
            but carousel cards will give you less control over the card layout.

            Attributes:
                card_orientation (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard.CardOrientation):
                    Required. Orientation of the card.
                thumbnail_image_alignment (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard.ThumbnailImageAlignment):
                    Required if orientation is horizontal.
                    Image preview alignment for standalone cards
                    with horizontal layout.
                card_content (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent):
                    Required. Card content.
            """

            class CardOrientation(proto.Enum):
                r"""Orientation of the card.

                Values:
                    CARD_ORIENTATION_UNSPECIFIED (0):
                        Not specified.
                    HORIZONTAL (1):
                        Horizontal layout.
                    VERTICAL (2):
                        Vertical layout.
                """

                CARD_ORIENTATION_UNSPECIFIED = 0
                HORIZONTAL = 1
                VERTICAL = 2

            class ThumbnailImageAlignment(proto.Enum):
                r"""Thumbnail preview alignment for standalone cards with
                horizontal layout.

                Values:
                    THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED (0):
                        Not specified.
                    LEFT (1):
                        Thumbnail preview is left-aligned.
                    RIGHT (2):
                        Thumbnail preview is right-aligned.
                """

                THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED = 0
                LEFT = 1
                RIGHT = 2

            card_orientation: "Intent.Message.RbmStandaloneCard.CardOrientation" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="Intent.Message.RbmStandaloneCard.CardOrientation",
                )
            )
            thumbnail_image_alignment: "Intent.Message.RbmStandaloneCard.ThumbnailImageAlignment" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Intent.Message.RbmStandaloneCard.ThumbnailImageAlignment",
            )
            card_content: "Intent.Message.RbmCardContent" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Intent.Message.RbmCardContent",
            )

        class RbmCardContent(proto.Message):
            r"""Rich Business Messaging (RBM) Card content

            Attributes:
                title (str):
                    Optional. Title of the card (at most 200
                    bytes).
                    At least one of the title, description or media
                    must be set.
                description (str):
                    Optional. Description of the card (at most
                    2000 bytes).
                    At least one of the title, description or media
                    must be set.
                media (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent.RbmMedia):
                    Optional. However at least one of the title,
                    description or media must be set. Media (image,
                    GIF or a video) to include in the card.
                suggestions (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestion]):
                    Optional. List of suggestions to include in
                    the card.
            """

            class RbmMedia(proto.Message):
                r"""Rich Business Messaging (RBM) Media displayed in Cards The following
                media-types are currently supported:

                Image Types

                - image/jpeg
                - image/jpg'
                - image/gif
                - image/png

                Video Types

                - video/h263
                - video/m4v
                - video/mp4
                - video/mpeg
                - video/mpeg4
                - video/webm

                Attributes:
                    file_uri (str):
                        Required. Publicly reachable URI of the file.
                        The RBM platform determines the MIME type of the
                        file from the content-type field in the HTTP
                        headers when the platform fetches the file. The
                        content-type field must be present and accurate
                        in the HTTP response from the URL.
                    thumbnail_uri (str):
                        Optional. Publicly reachable URI of the
                        thumbnail.If you don't provide a thumbnail URI,
                        the RBM platform displays a blank placeholder
                        thumbnail until the user's device downloads the
                        file. Depending on the user's setting, the file
                        may not download automatically and may require
                        the user to tap a download button.
                    height (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent.RbmMedia.Height):
                        Required for cards with vertical orientation.
                        The height of the media within a rich card with
                        a vertical layout. For a standalone card with
                        horizontal layout, height is not customizable,
                        and this field is ignored.
                """

                class Height(proto.Enum):
                    r"""Media height

                    Values:
                        HEIGHT_UNSPECIFIED (0):
                            Not specified.
                        SHORT (1):
                            112 DP.
                        MEDIUM (2):
                            168 DP.
                        TALL (3):
                            264 DP. Not available for rich card carousels
                            when the card width is set to small.
                    """

                    HEIGHT_UNSPECIFIED = 0
                    SHORT = 1
                    MEDIUM = 2
                    TALL = 3

                file_uri: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                thumbnail_uri: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                height: "Intent.Message.RbmCardContent.RbmMedia.Height" = proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="Intent.Message.RbmCardContent.RbmMedia.Height",
                )

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            description: str = proto.Field(
                proto.STRING,
                number=2,
            )
            media: "Intent.Message.RbmCardContent.RbmMedia" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Intent.Message.RbmCardContent.RbmMedia",
            )
            suggestions: MutableSequence["Intent.Message.RbmSuggestion"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.RbmSuggestion",
                )
            )

        class RbmSuggestion(proto.Message):
            r"""Rich Business Messaging (RBM) suggestion. Suggestions allow
            user to easily select/click a predefined response or perform an
            action (like opening a web uri).

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                reply (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedReply):
                    Predefined replies for user to select instead
                    of typing

                    This field is a member of `oneof`_ ``suggestion``.
                action (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction):
                    Predefined client side actions that user can
                    choose

                    This field is a member of `oneof`_ ``suggestion``.
            """

            reply: "Intent.Message.RbmSuggestedReply" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="suggestion",
                message="Intent.Message.RbmSuggestedReply",
            )
            action: "Intent.Message.RbmSuggestedAction" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="suggestion",
                message="Intent.Message.RbmSuggestedAction",
            )

        class RbmSuggestedReply(proto.Message):
            r"""Rich Business Messaging (RBM) suggested reply that the user
            can click instead of typing in their own response.

            Attributes:
                text (str):
                    Suggested reply text.
                postback_data (str):
                    Opaque payload that the Dialogflow receives
                    in a user event when the user taps the suggested
                    reply. This data will be also forwarded to
                    webhook to allow performing custom business
                    logic.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            postback_data: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class RbmSuggestedAction(proto.Message):
            r"""Rich Business Messaging (RBM) suggested client-side action
            that the user can choose from the card.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                text (str):
                    Text to display alongside the action.
                postback_data (str):
                    Opaque payload that the Dialogflow receives
                    in a user event when the user taps the suggested
                    action. This data will be also forwarded to
                    webhook to allow performing custom business
                    logic.
                dial (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionDial):
                    Suggested client side action: Dial a phone
                    number

                    This field is a member of `oneof`_ ``action``.
                open_url (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionOpenUri):
                    Suggested client side action: Open a URI on
                    device

                    This field is a member of `oneof`_ ``action``.
                share_location (google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionShareLocation):
                    Suggested client side action: Share user
                    location

                    This field is a member of `oneof`_ ``action``.
            """

            class RbmSuggestedActionDial(proto.Message):
                r"""Opens the user's default dialer app with the specified phone
                number but does not dial automatically.

                Attributes:
                    phone_number (str):
                        Required. The phone number to fill in the default dialer
                        app. This field should be in
                        `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format. An
                        example of a correctly formatted phone number: +15556767888.
                """

                phone_number: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class RbmSuggestedActionOpenUri(proto.Message):
                r"""Opens the user's default web browser app to the specified uri
                If the user has an app installed that is
                registered as the default handler for the URL, then this app
                will be opened instead, and its icon will be used in the
                suggested action UI.

                Attributes:
                    uri (str):
                        Required. The uri to open on the user device
                """

                uri: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class RbmSuggestedActionShareLocation(proto.Message):
                r"""Opens the device's location chooser so the user can pick a
                location to send back to the agent.

                """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            postback_data: str = proto.Field(
                proto.STRING,
                number=2,
            )
            dial: "Intent.Message.RbmSuggestedAction.RbmSuggestedActionDial" = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="action",
                    message="Intent.Message.RbmSuggestedAction.RbmSuggestedActionDial",
                )
            )
            open_url: "Intent.Message.RbmSuggestedAction.RbmSuggestedActionOpenUri" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="action",
                message="Intent.Message.RbmSuggestedAction.RbmSuggestedActionOpenUri",
            )
            share_location: "Intent.Message.RbmSuggestedAction.RbmSuggestedActionShareLocation" = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="action",
                message="Intent.Message.RbmSuggestedAction.RbmSuggestedActionShareLocation",
            )

        class MediaContent(proto.Message):
            r"""The media content card for Actions on Google.

            Attributes:
                media_type (google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent.ResponseMediaType):
                    Optional. What type of media is the content
                    (ie "audio").
                media_objects (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent.ResponseMediaObject]):
                    Required. List of media objects.
            """

            class ResponseMediaType(proto.Enum):
                r"""Format of response media type.

                Values:
                    RESPONSE_MEDIA_TYPE_UNSPECIFIED (0):
                        Unspecified.
                    AUDIO (1):
                        Response media type is audio.
                """

                RESPONSE_MEDIA_TYPE_UNSPECIFIED = 0
                AUDIO = 1

            class ResponseMediaObject(proto.Message):
                r"""Response media object for media content card.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    name (str):
                        Required. Name of media card.
                    description (str):
                        Optional. Description of media card.
                    large_image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                        Optional. Image to display above media
                        content.

                        This field is a member of `oneof`_ ``image``.
                    icon (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                        Optional. Icon to display above media
                        content.

                        This field is a member of `oneof`_ ``image``.
                    content_url (str):
                        Required. Url where the media is stored.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                description: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                large_image: "Intent.Message.Image" = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="image",
                    message="Intent.Message.Image",
                )
                icon: "Intent.Message.Image" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    oneof="image",
                    message="Intent.Message.Image",
                )
                content_url: str = proto.Field(
                    proto.STRING,
                    number=5,
                )

            media_type: "Intent.Message.MediaContent.ResponseMediaType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Intent.Message.MediaContent.ResponseMediaType",
            )
            media_objects: MutableSequence[
                "Intent.Message.MediaContent.ResponseMediaObject"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Intent.Message.MediaContent.ResponseMediaObject",
            )

        class BrowseCarouselCard(proto.Message):
            r"""Browse Carousel Card for Actions on Google.
            https://developers.google.com/actions/assistant/responses#browsing_carousel

            Attributes:
                items (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem]):
                    Required. List of items in the Browse
                    Carousel Card. Minimum of two items, maximum of
                    ten.
                image_display_options (google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.ImageDisplayOptions):
                    Optional. Settings for displaying the image. Applies to
                    every image in
                    [items][google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCard.items].
            """

            class ImageDisplayOptions(proto.Enum):
                r"""Image display options for Actions on Google. This should be
                used for when the image's aspect ratio does not match the image
                container's aspect ratio.

                Values:
                    IMAGE_DISPLAY_OPTIONS_UNSPECIFIED (0):
                        Fill the gaps between the image and the image
                        container with gray bars.
                    GRAY (1):
                        Fill the gaps between the image and the image
                        container with gray bars.
                    WHITE (2):
                        Fill the gaps between the image and the image
                        container with white bars.
                    CROPPED (3):
                        Image is scaled such that the image width and
                        height match or exceed the container dimensions.
                        This may crop the top and bottom of the image if
                        the scaled image height is greater than the
                        container height, or crop the left and right of
                        the image if the scaled image width is greater
                        than the container width. This is similar to
                        "Zoom Mode" on a widescreen TV when playing a
                        4:3 video.
                    BLURRED_BACKGROUND (4):
                        Pad the gaps between image and image frame
                        with a blurred copy of the same image.
                """

                IMAGE_DISPLAY_OPTIONS_UNSPECIFIED = 0
                GRAY = 1
                WHITE = 2
                CROPPED = 3
                BLURRED_BACKGROUND = 4

            class BrowseCarouselCardItem(proto.Message):
                r"""Browsing carousel tile

                Attributes:
                    open_uri_action (google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction):
                        Required. Action to present to the user.
                    title (str):
                        Required. Title of the carousel item. Maximum
                        of two lines of text.
                    description (str):
                        Optional. Description of the carousel item.
                        Maximum of four lines of text.
                    image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                        Optional. Hero image for the carousel item.
                    footer (str):
                        Optional. Text that appears at the bottom of
                        the Browse Carousel Card. Maximum of one line of
                        text.
                """

                class OpenUrlAction(proto.Message):
                    r"""Actions on Google action to open a given url.

                    Attributes:
                        url (str):
                            Required. URL
                        url_type_hint (google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint):
                            Optional. Specifies the type of viewer that
                            is used when opening the URL. Defaults to
                            opening via web browser.
                    """

                    class UrlTypeHint(proto.Enum):
                        r"""Type of the URI.

                        Values:
                            URL_TYPE_HINT_UNSPECIFIED (0):
                                Unspecified
                            AMP_ACTION (1):
                                Url would be an amp action
                            AMP_CONTENT (2):
                                URL that points directly to AMP content, or
                                to a canonical URL which refers to AMP content
                                via <link rel="amphtml">.
                        """

                        URL_TYPE_HINT_UNSPECIFIED = 0
                        AMP_ACTION = 1
                        AMP_CONTENT = 2

                    url: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    url_type_hint: "Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint" = proto.Field(
                        proto.ENUM,
                        number=3,
                        enum="Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint",
                    )

                open_uri_action: "Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction",
                )
                title: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                description: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                image: "Intent.Message.Image" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.Image",
                )
                footer: str = proto.Field(
                    proto.STRING,
                    number=5,
                )

            items: MutableSequence[
                "Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem",
            )
            image_display_options: "Intent.Message.BrowseCarouselCard.ImageDisplayOptions" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Intent.Message.BrowseCarouselCard.ImageDisplayOptions",
            )

        class TableCard(proto.Message):
            r"""Table card for Actions on Google.

            Attributes:
                title (str):
                    Required. Title of the card.
                subtitle (str):
                    Optional. Subtitle to the title.
                image (google.cloud.dialogflow_v2beta1.types.Intent.Message.Image):
                    Optional. Image which should be displayed on
                    the card.
                column_properties (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.ColumnProperties]):
                    Optional. Display properties for the columns
                    in this table.
                rows (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCardRow]):
                    Optional. Rows in this table of data.
                buttons (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard.Button]):
                    Optional. List of buttons for the card.
            """

            title: str = proto.Field(
                proto.STRING,
                number=1,
            )
            subtitle: str = proto.Field(
                proto.STRING,
                number=2,
            )
            image: "Intent.Message.Image" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Intent.Message.Image",
            )
            column_properties: MutableSequence["Intent.Message.ColumnProperties"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="Intent.Message.ColumnProperties",
                )
            )
            rows: MutableSequence["Intent.Message.TableCardRow"] = proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="Intent.Message.TableCardRow",
            )
            buttons: MutableSequence["Intent.Message.BasicCard.Button"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=6,
                    message="Intent.Message.BasicCard.Button",
                )
            )

        class ColumnProperties(proto.Message):
            r"""Column properties for
            [TableCard][google.cloud.dialogflow.v2beta1.Intent.Message.TableCard].

            Attributes:
                header (str):
                    Required. Column heading.
                horizontal_alignment (google.cloud.dialogflow_v2beta1.types.Intent.Message.ColumnProperties.HorizontalAlignment):
                    Optional. Defines text alignment for all
                    cells in this column.
            """

            class HorizontalAlignment(proto.Enum):
                r"""Text alignments within a cell.

                Values:
                    HORIZONTAL_ALIGNMENT_UNSPECIFIED (0):
                        Text is aligned to the leading edge of the
                        column.
                    LEADING (1):
                        Text is aligned to the leading edge of the
                        column.
                    CENTER (2):
                        Text is centered in the column.
                    TRAILING (3):
                        Text is aligned to the trailing edge of the
                        column.
                """

                HORIZONTAL_ALIGNMENT_UNSPECIFIED = 0
                LEADING = 1
                CENTER = 2
                TRAILING = 3

            header: str = proto.Field(
                proto.STRING,
                number=1,
            )
            horizontal_alignment: "Intent.Message.ColumnProperties.HorizontalAlignment" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Intent.Message.ColumnProperties.HorizontalAlignment",
            )

        class TableCardRow(proto.Message):
            r"""Row of
            [TableCard][google.cloud.dialogflow.v2beta1.Intent.Message.TableCard].

            Attributes:
                cells (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCardCell]):
                    Optional. List of cells that make up this
                    row.
                divider_after (bool):
                    Optional. Whether to add a visual divider
                    after this row.
            """

            cells: MutableSequence["Intent.Message.TableCardCell"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="Intent.Message.TableCardCell",
                )
            )
            divider_after: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        class TableCardCell(proto.Message):
            r"""Cell of
            [TableCardRow][google.cloud.dialogflow.v2beta1.Intent.Message.TableCardRow].

            Attributes:
                text (str):
                    Required. Text in this cell.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )

        text: "Intent.Message.Text" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="message",
            message="Intent.Message.Text",
        )
        image: "Intent.Message.Image" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="message",
            message="Intent.Message.Image",
        )
        quick_replies: "Intent.Message.QuickReplies" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="message",
            message="Intent.Message.QuickReplies",
        )
        card: "Intent.Message.Card" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="message",
            message="Intent.Message.Card",
        )
        payload: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="message",
            message=struct_pb2.Struct,
        )
        simple_responses: "Intent.Message.SimpleResponses" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="message",
            message="Intent.Message.SimpleResponses",
        )
        basic_card: "Intent.Message.BasicCard" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="message",
            message="Intent.Message.BasicCard",
        )
        suggestions: "Intent.Message.Suggestions" = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="message",
            message="Intent.Message.Suggestions",
        )
        link_out_suggestion: "Intent.Message.LinkOutSuggestion" = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="message",
            message="Intent.Message.LinkOutSuggestion",
        )
        list_select: "Intent.Message.ListSelect" = proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="message",
            message="Intent.Message.ListSelect",
        )
        carousel_select: "Intent.Message.CarouselSelect" = proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="message",
            message="Intent.Message.CarouselSelect",
        )
        telephony_play_audio: "Intent.Message.TelephonyPlayAudio" = proto.Field(
            proto.MESSAGE,
            number=13,
            oneof="message",
            message="Intent.Message.TelephonyPlayAudio",
        )
        telephony_synthesize_speech: "Intent.Message.TelephonySynthesizeSpeech" = (
            proto.Field(
                proto.MESSAGE,
                number=14,
                oneof="message",
                message="Intent.Message.TelephonySynthesizeSpeech",
            )
        )
        telephony_transfer_call: "Intent.Message.TelephonyTransferCall" = proto.Field(
            proto.MESSAGE,
            number=15,
            oneof="message",
            message="Intent.Message.TelephonyTransferCall",
        )
        rbm_text: "Intent.Message.RbmText" = proto.Field(
            proto.MESSAGE,
            number=18,
            oneof="message",
            message="Intent.Message.RbmText",
        )
        rbm_standalone_rich_card: "Intent.Message.RbmStandaloneCard" = proto.Field(
            proto.MESSAGE,
            number=19,
            oneof="message",
            message="Intent.Message.RbmStandaloneCard",
        )
        rbm_carousel_rich_card: "Intent.Message.RbmCarouselCard" = proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="message",
            message="Intent.Message.RbmCarouselCard",
        )
        browse_carousel_card: "Intent.Message.BrowseCarouselCard" = proto.Field(
            proto.MESSAGE,
            number=22,
            oneof="message",
            message="Intent.Message.BrowseCarouselCard",
        )
        table_card: "Intent.Message.TableCard" = proto.Field(
            proto.MESSAGE,
            number=23,
            oneof="message",
            message="Intent.Message.TableCard",
        )
        media_content: "Intent.Message.MediaContent" = proto.Field(
            proto.MESSAGE,
            number=24,
            oneof="message",
            message="Intent.Message.MediaContent",
        )
        platform: "Intent.Message.Platform" = proto.Field(
            proto.ENUM,
            number=6,
            enum="Intent.Message.Platform",
        )

    class FollowupIntentInfo(proto.Message):
        r"""Represents a single followup intent in the chain.

        Attributes:
            followup_intent_name (str):
                The unique identifier of the followup intent. Format:
                ``projects/<Project ID>/agent/intents/<Intent ID>``.
            parent_followup_intent_name (str):
                The unique identifier of the followup intent's parent.
                Format: ``projects/<Project ID>/agent/intents/<Intent ID>``.
        """

        followup_intent_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        parent_followup_intent_name: str = proto.Field(
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
    webhook_state: WebhookState = proto.Field(
        proto.ENUM,
        number=6,
        enum=WebhookState,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=3,
    )
    is_fallback: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    ml_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    ml_disabled: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    live_agent_handoff: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    end_interaction: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    input_context_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    training_phrases: MutableSequence[TrainingPhrase] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=TrainingPhrase,
    )
    action: str = proto.Field(
        proto.STRING,
        number=10,
    )
    output_contexts: MutableSequence[context.Context] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=context.Context,
    )
    reset_contexts: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    parameters: MutableSequence[Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=Parameter,
    )
    messages: MutableSequence[Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=Message,
    )
    default_response_platforms: MutableSequence[Message.Platform] = proto.RepeatedField(
        proto.ENUM,
        number=15,
        enum=Message.Platform,
    )
    root_followup_intent_name: str = proto.Field(
        proto.STRING,
        number=16,
    )
    parent_followup_intent_name: str = proto.Field(
        proto.STRING,
        number=17,
    )
    followup_intent_info: MutableSequence[FollowupIntentInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=FollowupIntentInfo,
    )


class ListIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.ListIntents][google.cloud.dialogflow.v2beta1.Intents.ListIntents].

    Attributes:
        parent (str):
            Required. The agent to list all intents from. Format:
            ``projects/<Project ID>/agent`` or
            ``projects/<Project ID>/locations/<Location ID>/agent``.

            Alternatively, you can specify the environment to list
            intents for. Format:
            ``projects/<Project ID>/agent/environments/<Environment ID>``
            or
            ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``.
            Note: training phrases of the intents will not be returned
            for non-draft environment.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        intent_view (google.cloud.dialogflow_v2beta1.types.IntentView):
            Optional. The resource view to apply to the
            returned intent.
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
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=3,
        enum="IntentView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListIntentsResponse(proto.Message):
    r"""The response message for
    [Intents.ListIntents][google.cloud.dialogflow.v2beta1.Intents.ListIntents].

    Attributes:
        intents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent]):
            The list of agent intents. There will be a maximum number of
            items returned based on the page_size field in the request.
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
    [Intents.GetIntent][google.cloud.dialogflow.v2beta1.Intents.GetIntent].

    Attributes:
        name (str):
            Required. The name of the intent. Supported formats:

            - ``projects/<Project ID>/agent/intents/<Intent ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>``
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        intent_view (google.cloud.dialogflow_v2beta1.types.IntentView):
            Optional. The resource view to apply to the
            returned intent.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=3,
        enum="IntentView",
    )


class CreateIntentRequest(proto.Message):
    r"""The request message for
    [Intents.CreateIntent][google.cloud.dialogflow.v2beta1.Intents.CreateIntent].

    Attributes:
        parent (str):
            Required. The agent to create a intent for. Supported
            formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        intent (google.cloud.dialogflow_v2beta1.types.Intent):
            Required. The intent to create.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        intent_view (google.cloud.dialogflow_v2beta1.types.IntentView):
            Optional. The resource view to apply to the
            returned intent.
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
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="IntentView",
    )


class UpdateIntentRequest(proto.Message):
    r"""The request message for
    [Intents.UpdateIntent][google.cloud.dialogflow.v2beta1.Intents.UpdateIntent].

    Attributes:
        intent (google.cloud.dialogflow_v2beta1.types.Intent):
            Required. The intent to update.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
        intent_view (google.cloud.dialogflow_v2beta1.types.IntentView):
            Optional. The resource view to apply to the
            returned intent.
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
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="IntentView",
    )


class DeleteIntentRequest(proto.Message):
    r"""The request message for
    [Intents.DeleteIntent][google.cloud.dialogflow.v2beta1.Intents.DeleteIntent].

    Attributes:
        name (str):
            Required. The name of the intent to delete. If this intent
            has direct or indirect followup intents, we also delete
            them.

            Supported formats:

            - ``projects/<Project ID>/agent/intents/<Intent ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchUpdateIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.BatchUpdateIntents][google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The name of the agent to update or create intents
            in. Supported formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        intent_batch_uri (str):
            The URI to a Google Cloud Storage file
            containing intents to update or create. The file
            format can either be a serialized proto (of
            IntentBatch type) or JSON object. Note: The URI
            must start with "gs://".

            This field is a member of `oneof`_ ``intent_batch``.
        intent_batch_inline (google.cloud.dialogflow_v2beta1.types.IntentBatch):
            The collection of intents to update or
            create.

            This field is a member of `oneof`_ ``intent_batch``.
        language_code (str):
            Optional. The language used to access language-specific
            data. If not specified, the agent's default language is
            used. For more information, see `Multilingual intent and
            entity
            data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
        intent_view (google.cloud.dialogflow_v2beta1.types.IntentView):
            Optional. The resource view to apply to the
            returned intent.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    intent_batch_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="intent_batch",
    )
    intent_batch_inline: "IntentBatch" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="intent_batch",
        message="IntentBatch",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )
    intent_view: "IntentView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="IntentView",
    )


class BatchUpdateIntentsResponse(proto.Message):
    r"""The response message for
    [Intents.BatchUpdateIntents][google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents].

    Attributes:
        intents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent]):
            The collection of updated or created intents.
    """

    intents: MutableSequence["Intent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Intent",
    )


class BatchDeleteIntentsRequest(proto.Message):
    r"""The request message for
    [Intents.BatchDeleteIntents][google.cloud.dialogflow.v2beta1.Intents.BatchDeleteIntents].

    Attributes:
        parent (str):
            Required. The name of the agent to delete all entities types
            for. Supported formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        intents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent]):
            Required. The collection of intents to delete. Only intent
            ``name`` must be filled in.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    intents: MutableSequence["Intent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Intent",
    )


class IntentBatch(proto.Message):
    r"""This message is a wrapper around a collection of intents.

    Attributes:
        intents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Intent]):
            A collection of intents.
    """

    intents: MutableSequence["Intent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Intent",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
