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
import proto  # type: ignore

from google.cloud.dialogflowcx_v3.types import gcs

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "AdvancedSettings",
    },
)


class AdvancedSettings(proto.Message):
    r"""Hierarchical advanced settings for
    agent/flow/page/fulfillment/parameter. Settings exposed at lower
    level overrides the settings exposed at higher level. Overriding
    occurs at the sub-setting level. For example, the
    playback_interruption_settings at fulfillment level only overrides
    the playback_interruption_settings at the agent level, leaving other
    settings at the agent level unchanged.

    DTMF settings does not override each other. DTMF settings set at
    different levels define DTMF detections running in parallel.

    Hierarchy: Agent->Flow->Page->Fulfillment/Parameter.

    Attributes:
        audio_export_gcs_destination (google.cloud.dialogflowcx_v3.types.GcsDestination):
            If present, incoming audio is exported by
            Dialogflow to the configured Google Cloud
            Storage destination. Exposed at the following
            levels:

            - Agent level
            - Flow level
        speech_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings.SpeechSettings):
            Settings for speech to text detection.
            Exposed at the following levels:

            - Agent level
            - Flow level
            - Page level
            - Parameter level
        dtmf_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings.DtmfSettings):
            Settings for DTMF.
            Exposed at the following levels:

            - Agent level
            - Flow level
            - Page level
            - Parameter level.
        logging_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings.LoggingSettings):
            Settings for logging.
            Settings for Dialogflow History, Contact Center
            messages, StackDriver logs, and speech logging.
            Exposed at the following levels:

            - Agent level.
    """

    class SpeechSettings(proto.Message):
        r"""Define behaviors of speech to text detection.

        Attributes:
            endpointer_sensitivity (int):
                Sensitivity of the speech model that detects
                the end of speech. Scale from 0 to 100.
            no_speech_timeout (google.protobuf.duration_pb2.Duration):
                Timeout before detecting no speech.
            use_timeout_based_endpointing (bool):
                Use timeout based endpointing, interpreting
                endpointer sensitivity as seconds of timeout
                value.
            models (MutableMapping[str, str]):
                Mapping from language to Speech-to-Text model. The mapped
                Speech-to-Text model will be selected for requests from its
                corresponding language. For more information, see `Speech
                models <https://cloud.google.com/dialogflow/cx/docs/concept/speech-models>`__.
        """

        endpointer_sensitivity: int = proto.Field(
            proto.INT32,
            number=1,
        )
        no_speech_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        use_timeout_based_endpointing: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        models: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=5,
        )

    class DtmfSettings(proto.Message):
        r"""Define behaviors for DTMF (dual tone multi frequency).

        Attributes:
            enabled (bool):
                If true, incoming audio is processed for DTMF
                (dual tone multi frequency) events. For example,
                if the caller presses a button on their
                telephone keypad and DTMF processing is enabled,
                Dialogflow will detect the event (e.g. a "3" was
                pressed) in the incoming audio and pass the
                event to the bot to drive business logic (e.g.
                when 3 is pressed, return the account balance).
            max_digits (int):
                Max length of DTMF digits.
            finish_digit (str):
                The digit that terminates a DTMF digit
                sequence.
            interdigit_timeout_duration (google.protobuf.duration_pb2.Duration):
                Interdigit timeout setting for matching dtmf
                input to regex.
            endpointing_timeout_duration (google.protobuf.duration_pb2.Duration):
                Endpoint timeout setting for matching dtmf
                input to regex.
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        max_digits: int = proto.Field(
            proto.INT32,
            number=2,
        )
        finish_digit: str = proto.Field(
            proto.STRING,
            number=3,
        )
        interdigit_timeout_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
        endpointing_timeout_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )

    class LoggingSettings(proto.Message):
        r"""Define behaviors on logging.

        Attributes:
            enable_stackdriver_logging (bool):
                Enables Google Cloud Logging.
            enable_interaction_logging (bool):
                Enables DF Interaction logging.
            enable_consent_based_redaction (bool):
                Enables consent-based end-user input redaction, if true, a
                pre-defined session parameter
                ``$session.params.conversation-redaction`` will be used to
                determine if the utterance should be redacted.
        """

        enable_stackdriver_logging: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        enable_interaction_logging: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        enable_consent_based_redaction: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    audio_export_gcs_destination: gcs.GcsDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs.GcsDestination,
    )
    speech_settings: SpeechSettings = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SpeechSettings,
    )
    dtmf_settings: DtmfSettings = proto.Field(
        proto.MESSAGE,
        number=5,
        message=DtmfSettings,
    )
    logging_settings: LoggingSettings = proto.Field(
        proto.MESSAGE,
        number=6,
        message=LoggingSettings,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
