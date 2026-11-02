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

from google.cloud.dialogflow_v2.types import audio_config
from google.cloud.dialogflow_v2.types import fulfillment as gcd_fulfillment

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "Environment",
        "TextToSpeechSettings",
        "ListEnvironmentsRequest",
        "ListEnvironmentsResponse",
        "GetEnvironmentRequest",
        "CreateEnvironmentRequest",
        "UpdateEnvironmentRequest",
        "DeleteEnvironmentRequest",
        "GetEnvironmentHistoryRequest",
        "EnvironmentHistory",
    },
)


class Environment(proto.Message):
    r"""You can create multiple versions of your agent and publish them to
    separate environments.

    When you edit an agent, you are editing the draft agent. At any
    point, you can save the draft agent as an agent version, which is an
    immutable snapshot of your agent.

    When you save the draft agent, it is published to the default
    environment. When you create agent versions, you can publish them to
    custom environments. You can create a variety of custom environments
    for:

    - testing
    - development
    - production
    - etc.

    For more information, see the `versions and environments
    guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

    Attributes:
        name (str):
            Output only. The unique identifier of this agent
            environment. Supported formats:

            - ``projects/<Project ID>/agent/environments/<Environment ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``

            The environment ID for the default environment is ``-``.
        description (str):
            Optional. The developer-provided description
            for this environment. The maximum length is 500
            characters. If exceeded, the request is
            rejected.
        agent_version (str):
            Optional. The agent version loaded into this environment.
            Supported formats:

            - ``projects/<Project ID>/agent/versions/<Version ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>``
        state (google.cloud.dialogflow_v2.types.Environment.State):
            Output only. The state of this environment.
            This field is read-only, i.e., it cannot be set
            by create and update methods.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of this
            environment. This field is read-only, i.e., it
            cannot be set by create and update methods.
        text_to_speech_settings (google.cloud.dialogflow_v2.types.TextToSpeechSettings):
            Optional. Text to speech settings for this
            environment.
        fulfillment (google.cloud.dialogflow_v2.types.Fulfillment):
            Optional. The fulfillment settings to use for
            this environment.
    """

    class State(proto.Enum):
        r"""Represents an environment state. When an environment is pointed to a
        new agent version, the environment is temporarily set to the
        ``LOADING`` state. During that time, the environment keeps on
        serving the previous version of the agent. After the new agent
        version is done loading, the environment is set back to the
        ``RUNNING`` state.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified. This value is not used.
            STOPPED (1):
                Stopped.
            LOADING (2):
                Loading.
            RUNNING (3):
                Running.
        """

        STATE_UNSPECIFIED = 0
        STOPPED = 1
        LOADING = 2
        RUNNING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    agent_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    text_to_speech_settings: "TextToSpeechSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="TextToSpeechSettings",
    )
    fulfillment: gcd_fulfillment.Fulfillment = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcd_fulfillment.Fulfillment,
    )


class TextToSpeechSettings(proto.Message):
    r"""Instructs the speech synthesizer on how to generate the
    output audio content.

    Attributes:
        enable_text_to_speech (bool):
            Optional. Indicates whether text to speech is
            enabled. Even when this field is false, other
            settings in this proto are still retained.
        output_audio_encoding (google.cloud.dialogflow_v2.types.OutputAudioEncoding):
            Required. Audio encoding of the synthesized
            audio content.
        sample_rate_hertz (int):
            Optional. The synthesis sample rate (in
            hertz) for this audio. If not provided, then the
            synthesizer will use the default sample rate
            based on the audio encoding. If this is
            different from the voice's natural sample rate,
            then the synthesizer will honor this request by
            converting to the desired sample rate (which
            might result in worse audio quality).
        synthesize_speech_configs (MutableMapping[str, google.cloud.dialogflow_v2.types.SynthesizeSpeechConfig]):
            Optional. Configuration of how speech should
            be synthesized, mapping from language
            (https://cloud.google.com/dialogflow/docs/reference/language)
            to SynthesizeSpeechConfig.
    """

    enable_text_to_speech: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    output_audio_encoding: audio_config.OutputAudioEncoding = proto.Field(
        proto.ENUM,
        number=2,
        enum=audio_config.OutputAudioEncoding,
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=3,
    )
    synthesize_speech_configs: MutableMapping[
        str, audio_config.SynthesizeSpeechConfig
    ] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=audio_config.SynthesizeSpeechConfig,
    )


class ListEnvironmentsRequest(proto.Message):
    r"""The request message for
    [Environments.ListEnvironments][google.cloud.dialogflow.v2.Environments.ListEnvironments].

    Attributes:
        parent (str):
            Required. The agent to list all environments from. Format:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
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
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListEnvironmentsResponse(proto.Message):
    r"""The response message for
    [Environments.ListEnvironments][google.cloud.dialogflow.v2.Environments.ListEnvironments].

    Attributes:
        environments (MutableSequence[google.cloud.dialogflow_v2.types.Environment]):
            The list of agent environments. There will be a maximum
            number of items returned based on the page_size field in the
            request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    environments: MutableSequence["Environment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.GetEnvironment][google.cloud.dialogflow.v2.Environments.GetEnvironment].

    Attributes:
        name (str):
            Required. The name of the environment. Supported formats:

            - ``projects/<Project ID>/agent/environments/<Environment ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``

            The environment ID for the default environment is ``-``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.CreateEnvironment][google.cloud.dialogflow.v2.Environments.CreateEnvironment].

    Attributes:
        parent (str):
            Required. The agent to create an environment for. Supported
            formats:

            - ``projects/<Project ID>/agent``
            - ``projects/<Project ID>/locations/<Location ID>/agent``
        environment (google.cloud.dialogflow_v2.types.Environment):
            Required. The environment to create.
        environment_id (str):
            Required. The unique id of the new
            environment.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Environment",
    )
    environment_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.UpdateEnvironment][google.cloud.dialogflow.v2.Environments.UpdateEnvironment].

    Attributes:
        environment (google.cloud.dialogflow_v2.types.Environment):
            Required. The environment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
        allow_load_to_draft_and_discard_changes (bool):
            Optional. This field is used to prevent accidental overwrite
            of the default environment, which is an operation that
            cannot be undone. To confirm that the caller desires this
            overwrite, this field must be explicitly set to true when
            updating the default environment (environment ID = ``-``).
    """

    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_load_to_draft_and_discard_changes: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.DeleteEnvironment][google.cloud.dialogflow.v2.Environments.DeleteEnvironment].

    Attributes:
        name (str):
            Required. The name of the environment to delete. / Format:

            - ``projects/<Project ID>/agent/environments/<Environment ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``

            The environment ID for the default environment is ``-``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEnvironmentHistoryRequest(proto.Message):
    r"""The request message for
    [Environments.GetEnvironmentHistory][google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory].

    Attributes:
        parent (str):
            Required. The name of the environment to retrieve history
            for. Supported formats:

            - ``projects/<Project ID>/agent/environments/<Environment ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``

            The environment ID for the default environment is ``-``.
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
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EnvironmentHistory(proto.Message):
    r"""The response message for
    [Environments.GetEnvironmentHistory][google.cloud.dialogflow.v2.Environments.GetEnvironmentHistory].

    Attributes:
        parent (str):
            Output only. The name of the environment this history is
            for. Supported formats:

            - ``projects/<Project ID>/agent/environments/<Environment ID>``
            - ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>``

            The environment ID for the default environment is ``-``.
        entries (MutableSequence[google.cloud.dialogflow_v2.types.EnvironmentHistory.Entry]):
            Output only. The list of agent environments. There will be a
            maximum number of items returned based on the page_size
            field in the request.
        next_page_token (str):
            Output only. Token to retrieve the next page
            of results, or empty if there are no more
            results in the list.
    """

    class Entry(proto.Message):
        r"""Represents an environment history entry.

        Attributes:
            agent_version (str):
                The agent version loaded into this
                environment history entry.
            description (str):
                The developer-provided description for this
                environment history entry.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                The creation time of this environment history
                entry.
        """

        agent_version: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    @property
    def raw_page(self):
        return self

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entries: MutableSequence[Entry] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Entry,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
