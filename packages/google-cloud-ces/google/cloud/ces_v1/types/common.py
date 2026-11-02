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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "ExecutionType",
        "Callback",
        "ModelSettings",
        "TriggerAction",
        "TlsConfig",
        "ServiceDirectoryConfig",
        "ChannelProfile",
        "Span",
    },
)


class ExecutionType(proto.Enum):
    r"""The execution type of the tool or toolset.

    Values:
        EXECUTION_TYPE_UNSPECIFIED (0):
            The execution type is unspecified. Defaults to
            ``SYNCHRONOUS`` if unspecified.
        SYNCHRONOUS (1):
            The tool is executed synchronously. The
            session is blocked until the tool returns.
        ASYNCHRONOUS (2):
            The tool is executed asynchronously. The
            session will continue while the tool is
            executing.
    """

    EXECUTION_TYPE_UNSPECIFIED = 0
    SYNCHRONOUS = 1
    ASYNCHRONOUS = 2


class Callback(proto.Message):
    r"""A callback defines the custom logic to be executed at various
    stages of agent interaction.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        python_code (str):
            Required. The python code to execute for the
            callback.

            This field is a member of `oneof`_ ``callback``.
        description (str):
            Optional. Human-readable description of the
            callback.
        disabled (bool):
            Optional. Whether the callback is disabled.
            Disabled callbacks are ignored by the agent.
        proactive_execution_enabled (bool):
            Optional. If enabled, the callback will also be executed on
            intermediate model outputs. This setting only affects after
            model callback. **ENABLE WITH CAUTION**. Typically after
            model callback only needs to be executed after receiving all
            model responses. Enabling proactive execution may have
            negative implication on the execution cost and latency, and
            should only be enabled in rare situations.
    """

    python_code: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="callback",
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    proactive_execution_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ModelSettings(proto.Message):
    r"""Model settings contains various configurations for the LLM
    model.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        model (str):
            Optional. The LLM model that the agent should
            use. If not set, the agent will inherit the
            model from its parent agent.
        temperature (float):
            Optional. If set, this temperature will be
            used for the LLM model. Temperature controls the
            randomness of the model's responses. Lower
            temperatures produce responses that are more
            predictable. Higher temperatures produce
            responses that are more creative.

            This field is a member of `oneof`_ ``_temperature``.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    temperature: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class TriggerAction(proto.Message):
    r"""Action that is taken when a certain precondition is met.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        respond_immediately (google.cloud.ces_v1.types.TriggerAction.RespondImmediately):
            Optional. Immediately respond with a
            preconfigured response.

            This field is a member of `oneof`_ ``action``.
        transfer_agent (google.cloud.ces_v1.types.TriggerAction.TransferAgent):
            Optional. Transfer the conversation to a
            different agent.

            This field is a member of `oneof`_ ``action``.
        generative_answer (google.cloud.ces_v1.types.TriggerAction.GenerativeAnswer):
            Optional. Respond with a generative answer.

            This field is a member of `oneof`_ ``action``.
    """

    class Response(proto.Message):
        r"""Represents a response from the agent.

        Attributes:
            text (str):
                Required. Text for the agent to respond with.
            disabled (bool):
                Optional. Whether the response is disabled.
                Disabled responses are not used by the agent.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class RespondImmediately(proto.Message):
        r"""The agent will immediately respond with a preconfigured
        response.

        Attributes:
            responses (MutableSequence[google.cloud.ces_v1.types.TriggerAction.Response]):
                Required. The canned responses for the agent
                to choose from. The response is chosen randomly.
        """

        responses: MutableSequence["TriggerAction.Response"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TriggerAction.Response",
        )

    class GenerativeAnswer(proto.Message):
        r"""The agent will immediately respond with a generative answer.

        Attributes:
            prompt (str):
                Required. The prompt to use for the
                generative answer.
        """

        prompt: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TransferAgent(proto.Message):
        r"""The agent will transfer the conversation to a different
        agent.

        Attributes:
            agent (str):
                Required. The name of the agent to transfer the conversation
                to. The agent must be in the same app as the current agent.
                Format:
                ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        """

        agent: str = proto.Field(
            proto.STRING,
            number=1,
        )

    respond_immediately: RespondImmediately = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message=RespondImmediately,
    )
    transfer_agent: TransferAgent = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message=TransferAgent,
    )
    generative_answer: GenerativeAnswer = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message=GenerativeAnswer,
    )


class TlsConfig(proto.Message):
    r"""The TLS configuration.

    Attributes:
        ca_certs (MutableSequence[google.cloud.ces_v1.types.TlsConfig.CaCert]):
            Required. Specifies a list of allowed custom
            CA certificates for HTTPS verification.
    """

    class CaCert(proto.Message):
        r"""The CA certificate.

        Attributes:
            display_name (str):
                Required. The name of the allowed custom CA
                certificates. This can be used to disambiguate
                the custom CA certificates.
            cert (bytes):
                Required. The allowed custom CA certificates (in DER format)
                for HTTPS verification. This overrides the default SSL trust
                store. If this is empty or unspecified, CES will use
                Google's default trust store to verify certificates. N.B.
                Make sure the HTTPS server certificates are signed with
                "subject alt name". For instance a certificate can be
                self-signed using the following command:

                ::

                      openssl x509 -req -days 200 -in example.com.csr \
                        -signkey example.com.key \
                        -out example.com.crt \
                        -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cert: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )

    ca_certs: MutableSequence[CaCert] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CaCert,
    )


class ServiceDirectoryConfig(proto.Message):
    r"""Configuration for tools using Service Directory.

    Attributes:
        service (str):
            Required. The name of `Service
            Directory <https://cloud.google.com/service-directory>`__
            service. Format:
            ``projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}``.
            Location of the service directory must be the same as the
            location of the app.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ChannelProfile(proto.Message):
    r"""A ChannelProfile configures the agent's behavior for a
    specific communication channel, such as web UI or telephony.

    Attributes:
        profile_id (str):
            Optional. The unique identifier of the
            channel profile.
        channel_type (google.cloud.ces_v1.types.ChannelProfile.ChannelType):
            Optional. The type of the channel profile.
        persona_property (google.cloud.ces_v1.types.ChannelProfile.PersonaProperty):
            Optional. The persona property of the channel
            profile.
        disable_dtmf (bool):
            Optional. Whether to disable DTMF (dual-tone
            multi-frequency).
        disable_barge_in_control (bool):
            Optional. Whether to disable user barge-in control in the
            conversation.

            - **true**: User interruptions are disabled while the agent
              is speaking.
            - **false**: The agent retains automatic control over when
              the user can interrupt.
        web_widget_config (google.cloud.ces_v1.types.ChannelProfile.WebWidgetConfig):
            Optional. The configuration for the web
            widget.
        noise_suppression_level (str):
            Optional. The noise suppression level of the channel
            profile. Available values are "low", "moderate", "high",
            "very_high".
        whatsapp_config (google.cloud.ces_v1.types.ChannelProfile.WhatsAppConfig):
            Optional. Configuration specific to WhatsApp
            deployments.
        instagram_config (google.cloud.ces_v1.types.ChannelProfile.InstagramConfig):
            Optional. Configuration specific to Instagram
            deployments.
    """

    class ChannelType(proto.Enum):
        r"""The type of the channel profile.

        Values:
            UNKNOWN (0):
                Unknown channel type.
            WEB_UI (2):
                Web UI channel.
            API (3):
                API channel.
            TWILIO (4):
                Twilio channel.
            GOOGLE_TELEPHONY_PLATFORM (5):
                Google Telephony Platform channel.
            CONTACT_CENTER_AS_A_SERVICE (6):
                Contact Center as a Service (CCaaS) channel.
            CONTACT_CENTER_AS_A_SERVICE_CHAT (11):
                Contact Center as a Service (CCaaS Chat)
                channel.
            FIVE9 (7):
                Five9 channel.
            CONTACT_CENTER_INTEGRATION (8):
                Third party contact center integration
                channel.
            WHATSAPP (9):
                WhatsApp channel.
            INSTAGRAM (10):
                Instagram channel.
        """

        UNKNOWN = 0
        WEB_UI = 2
        API = 3
        TWILIO = 4
        GOOGLE_TELEPHONY_PLATFORM = 5
        CONTACT_CENTER_AS_A_SERVICE = 6
        CONTACT_CENTER_AS_A_SERVICE_CHAT = 11
        FIVE9 = 7
        CONTACT_CENTER_INTEGRATION = 8
        WHATSAPP = 9
        INSTAGRAM = 10

    class PersonaProperty(proto.Message):
        r"""Represents the persona property of a channel.

        Attributes:
            persona (google.cloud.ces_v1.types.ChannelProfile.PersonaProperty.Persona):
                Optional. The persona of the channel.
        """

        class Persona(proto.Enum):
            r"""The persona of the channel.

            Values:
                UNKNOWN (0):
                    UNKNOWN persona.
                CONCISE (1):
                    The agent keeps the responses concise and to
                    the point
                CHATTY (2):
                    The agent provides additional context,
                    explanations, and details
            """

            UNKNOWN = 0
            CONCISE = 1
            CHATTY = 2

        persona: "ChannelProfile.PersonaProperty.Persona" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ChannelProfile.PersonaProperty.Persona",
        )

    class WebWidgetConfig(proto.Message):
        r"""Message for configuration for the web widget.

        Attributes:
            modality (google.cloud.ces_v1.types.ChannelProfile.WebWidgetConfig.Modality):
                Optional. The modality of the web widget.
            theme (google.cloud.ces_v1.types.ChannelProfile.WebWidgetConfig.Theme):
                Optional. The theme of the web widget.
            web_widget_title (str):
                Optional. The title of the web widget.
            security_settings (google.cloud.ces_v1.types.ChannelProfile.WebWidgetConfig.SecuritySettings):
                Optional. The security settings of the web
                widget.
        """

        class Modality(proto.Enum):
            r"""Modality of the web widget.

            Values:
                MODALITY_UNSPECIFIED (0):
                    Unknown modality.
                CHAT_AND_VOICE (1):
                    Widget supports both chat and voice input.
                VOICE_ONLY (2):
                    Widget supports only voice input.
                CHAT_ONLY (3):
                    Widget supports only chat input.
                CHAT_VOICE_AND_VIDEO (4):
                    Widget supports chat, voice, and video input.
            """

            MODALITY_UNSPECIFIED = 0
            CHAT_AND_VOICE = 1
            VOICE_ONLY = 2
            CHAT_ONLY = 3
            CHAT_VOICE_AND_VIDEO = 4

        class Theme(proto.Enum):
            r"""Theme of the web widget.

            Values:
                THEME_UNSPECIFIED (0):
                    Unknown theme.
                LIGHT (1):
                    Light theme.
                DARK (2):
                    Dark theme.
            """

            THEME_UNSPECIFIED = 0
            LIGHT = 1
            DARK = 2

        class SecuritySettings(proto.Message):
            r"""Security settings for the web widget.

            Attributes:
                enable_public_access (bool):
                    Optional. Indicates whether public access to the web widget
                    is enabled. If ``true``, the web widget will be publicly
                    accessible. If ``false``, the web widget must be integrated
                    with your own authentication and authorization system to
                    return valid credentials for accessing the CES agent.
                enable_origin_check (bool):
                    Optional. Indicates whether origin check for the web widget
                    is enabled. If ``true``, the web widget will check the
                    origin of the website that loads the web widget and only
                    allow it to be loaded in the same origin or any of the
                    allowed origins.
                allowed_origins (MutableSequence[str]):
                    Optional. The origins that are allowed to
                    host the web widget. An origin is defined by RFC
                    6454. If empty, all origins are allowed. A
                    maximum of 100 origins is allowed. Example:
                    "https://example.com".
                enable_recaptcha (bool):
                    Optional. Indicates whether reCAPTCHA
                    verification for the web widget is enabled.
            """

            enable_public_access: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            enable_origin_check: bool = proto.Field(
                proto.BOOL,
                number=4,
            )
            allowed_origins: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            enable_recaptcha: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        modality: "ChannelProfile.WebWidgetConfig.Modality" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ChannelProfile.WebWidgetConfig.Modality",
        )
        theme: "ChannelProfile.WebWidgetConfig.Theme" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ChannelProfile.WebWidgetConfig.Theme",
        )
        web_widget_title: str = proto.Field(
            proto.STRING,
            number=3,
        )
        security_settings: "ChannelProfile.WebWidgetConfig.SecuritySettings" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message="ChannelProfile.WebWidgetConfig.SecuritySettings",
            )
        )

    class WhatsAppConfig(proto.Message):
        r"""Configuration specific to WhatsApp deployments.

        Attributes:
            waba_id (str):
                Required. The WhatsApp Business Account ID.
            phone_number_id (str):
                Required. The Meta phone number ID.
            phone_number (str):
                Optional. The phone number in E.164 format.
            display_name (str):
                Output only. The fetched Meta business page
                name.
            thumbnail_url (str):
                Output only. The fetched Meta business
                profile thumbnail URL.
            description (str):
                Output only. The description of the Meta
                business page or profile.
        """

        waba_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        phone_number_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        phone_number: str = proto.Field(
            proto.STRING,
            number=3,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=4,
        )
        thumbnail_url: str = proto.Field(
            proto.STRING,
            number=5,
        )
        description: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class InstagramConfig(proto.Message):
        r"""Configuration specific to Instagram deployments.

        Attributes:
            instagram_account_id (str):
                Required. The Instagram Account ID.
            display_name (str):
                Output only. The fetched Meta business page
                name.
            thumbnail_url (str):
                Output only. The fetched Meta business
                profile thumbnail URL.
            description (str):
                Output only. The description of the Meta
                business page or profile.
        """

        instagram_account_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        thumbnail_url: str = proto.Field(
            proto.STRING,
            number=3,
        )
        description: str = proto.Field(
            proto.STRING,
            number=4,
        )

    profile_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    channel_type: ChannelType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ChannelType,
    )
    persona_property: PersonaProperty = proto.Field(
        proto.MESSAGE,
        number=2,
        message=PersonaProperty,
    )
    disable_dtmf: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    disable_barge_in_control: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    web_widget_config: WebWidgetConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=WebWidgetConfig,
    )
    noise_suppression_level: str = proto.Field(
        proto.STRING,
        number=8,
    )
    whatsapp_config: WhatsAppConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=WhatsAppConfig,
    )
    instagram_config: InstagramConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=InstagramConfig,
    )


class Span(proto.Message):
    r"""A span is a unit of work or a single operation during the
    request processing.

    Attributes:
        name (str):
            Output only. The name of the span.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of the span.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of the span.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration of the span.
        attributes (google.protobuf.struct_pb2.Struct):
            Output only. Key-value attributes associated
            with the span.
        child_spans (MutableSequence[google.cloud.ces_v1.types.Span]):
            Output only. The child spans that are nested
            under this span.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    attributes: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    child_spans: MutableSequence["Span"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Span",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
