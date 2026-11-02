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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.video.transcoder.v1",
    manifest={
        "Job",
        "JobTemplate",
        "JobConfig",
        "Input",
        "Output",
        "EditAtom",
        "AdBreak",
        "ElementaryStream",
        "MuxStream",
        "Manifest",
        "PubsubDestination",
        "SpriteSheet",
        "Overlay",
        "PreprocessingConfig",
        "TrackDefinition",
        "InputAttributes",
        "VideoStream",
        "AudioStream",
        "TextStream",
        "SegmentSettings",
        "Encryption",
    },
)


class Job(proto.Message):
    r"""Transcoding job resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the job. Format:
            ``projects/{project_number}/locations/{location}/jobs/{job}``
        input_uri (str):
            Input only. Specify the ``input_uri`` to populate empty
            ``uri`` fields in each element of ``Job.config.inputs`` or
            ``JobTemplate.config.inputs`` when using template. URI of
            the media. Input files must be at least 5 seconds in
            duration and stored in Cloud Storage (for example,
            ``gs://bucket/inputs/file.mp4``). See `Supported input and
            output
            formats <https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats>`__.
        output_uri (str):
            Input only. Specify the ``output_uri`` to populate an empty
            ``Job.config.output.uri`` or
            ``JobTemplate.config.output.uri`` when using template. URI
            for the output file(s). For example,
            ``gs://my-bucket/outputs/``. See `Supported input and output
            formats <https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats>`__.
        template_id (str):
            Input only. Specify the ``template_id`` to use for
            populating ``Job.config``. The default is ``preset/web-hd``,
            which is the only supported preset.

            User defined JobTemplate: ``{job_template_id}``

            This field is a member of `oneof`_ ``job_config``.
        config (google.cloud.video.transcoder_v1.types.JobConfig):
            The configuration for this job.

            This field is a member of `oneof`_ ``job_config``.
        state (google.cloud.video.transcoder_v1.types.Job.ProcessingState):
            Output only. The current state of the job.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the job was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the transcoding
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the transcoding
            finished.
        ttl_after_completion_days (int):
            Job time to live value in days, which will be
            effective after job completion. Job should be
            deleted automatically after the given TTL. Enter
            a value between 1 and 90. The default is 30.
        labels (MutableMapping[str, str]):
            The labels associated with this job. You can
            use these to organize and group your jobs.
        error (google.rpc.status_pb2.Status):
            Output only. An error object that describes the reason for
            the failure. This property is always present when
            [ProcessingState][google.cloud.video.transcoder.v1.Job.ProcessingState]
            is ``FAILED``.
        mode (google.cloud.video.transcoder_v1.types.Job.ProcessingMode):
            The processing mode of the job. The default is
            ``PROCESSING_MODE_INTERACTIVE``.
        batch_mode_priority (int):
            The processing priority of a batch job.
            This field can only be set for batch mode jobs.
            The default value is 0. This value cannot be
            negative. Higher values correspond to higher
            priorities for the job.
        optimization (google.cloud.video.transcoder_v1.types.Job.OptimizationStrategy):
            Optional. The optimization strategy of the job. The default
            is ``AUTODETECT``.
        fill_content_gaps (bool):
            Optional. Insert silence and duplicate frames
            when timestamp gaps are detected in a given
            stream.
    """

    class ProcessingState(proto.Enum):
        r"""The current state of the job.

        Values:
            PROCESSING_STATE_UNSPECIFIED (0):
                The processing state is not specified.
            PENDING (1):
                The job is enqueued and will be picked up for
                processing soon.
            RUNNING (2):
                The job is being processed.
            SUCCEEDED (3):
                The job has been completed successfully.
            FAILED (4):
                The job has failed. For additional information, see
                `Troubleshooting <https://cloud.google.com/transcoder/docs/troubleshooting>`__.
        """

        PROCESSING_STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4

    class ProcessingMode(proto.Enum):
        r"""The processing mode of the job.

        Values:
            PROCESSING_MODE_UNSPECIFIED (0):
                The job processing mode is not specified.
            PROCESSING_MODE_INTERACTIVE (1):
                The job processing mode is interactive mode.
                Interactive job will either be ran or rejected
                if quota does not allow for it.
            PROCESSING_MODE_BATCH (2):
                The job processing mode is batch mode.
                Batch mode allows queuing of jobs.
        """

        PROCESSING_MODE_UNSPECIFIED = 0
        PROCESSING_MODE_INTERACTIVE = 1
        PROCESSING_MODE_BATCH = 2

    class OptimizationStrategy(proto.Enum):
        r"""The optimization strategy of the job. The default is ``AUTODETECT``.

        Values:
            OPTIMIZATION_STRATEGY_UNSPECIFIED (0):
                The optimization strategy is not specified.
            AUTODETECT (1):
                Prioritize job processing speed.
            DISABLED (2):
                Disable all optimizations.
        """

        OPTIMIZATION_STRATEGY_UNSPECIFIED = 0
        AUTODETECT = 1
        DISABLED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    output_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    template_id: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="job_config",
    )
    config: "JobConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="job_config",
        message="JobConfig",
    )
    state: ProcessingState = proto.Field(
        proto.ENUM,
        number=8,
        enum=ProcessingState,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    ttl_after_completion_days: int = proto.Field(
        proto.INT32,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=17,
        message=status_pb2.Status,
    )
    mode: ProcessingMode = proto.Field(
        proto.ENUM,
        number=20,
        enum=ProcessingMode,
    )
    batch_mode_priority: int = proto.Field(
        proto.INT32,
        number=21,
    )
    optimization: OptimizationStrategy = proto.Field(
        proto.ENUM,
        number=22,
        enum=OptimizationStrategy,
    )
    fill_content_gaps: bool = proto.Field(
        proto.BOOL,
        number=25,
    )


class JobTemplate(proto.Message):
    r"""Transcoding job template resource.

    Attributes:
        name (str):
            The resource name of the job template. Format:
            ``projects/{project_number}/locations/{location}/jobTemplates/{job_template}``
        config (google.cloud.video.transcoder_v1.types.JobConfig):
            The configuration for this template.
        labels (MutableMapping[str, str]):
            The labels associated with this job template.
            You can use these to organize and group your job
            templates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "JobConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobConfig",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class JobConfig(proto.Message):
    r"""Job configuration

    Attributes:
        inputs (MutableSequence[google.cloud.video.transcoder_v1.types.Input]):
            List of input assets stored in Cloud Storage.
        edit_list (MutableSequence[google.cloud.video.transcoder_v1.types.EditAtom]):
            List of edit atoms. Defines the ultimate
            timeline of the resulting file or manifest.
        elementary_streams (MutableSequence[google.cloud.video.transcoder_v1.types.ElementaryStream]):
            List of elementary streams.
        mux_streams (MutableSequence[google.cloud.video.transcoder_v1.types.MuxStream]):
            List of multiplexing settings for output
            streams.
        manifests (MutableSequence[google.cloud.video.transcoder_v1.types.Manifest]):
            List of output manifests.
        output (google.cloud.video.transcoder_v1.types.Output):
            Output configuration.
        ad_breaks (MutableSequence[google.cloud.video.transcoder_v1.types.AdBreak]):
            List of ad breaks. Specifies where to insert
            ad break tags in the output manifests.
        pubsub_destination (google.cloud.video.transcoder_v1.types.PubsubDestination):
            Destination on Pub/Sub.
        sprite_sheets (MutableSequence[google.cloud.video.transcoder_v1.types.SpriteSheet]):
            List of output sprite sheets.
            Spritesheets require at least one VideoStream in
            the Jobconfig.
        overlays (MutableSequence[google.cloud.video.transcoder_v1.types.Overlay]):
            List of overlays on the output video, in
            descending Z-order.
        encryptions (MutableSequence[google.cloud.video.transcoder_v1.types.Encryption]):
            List of encryption configurations for the content. Each
            configuration has an ID. Specify this ID in the
            [MuxStream.encryption_id][google.cloud.video.transcoder.v1.MuxStream.encryption_id]
            field to indicate the configuration to use for that
            ``MuxStream`` output.
    """

    inputs: MutableSequence["Input"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Input",
    )
    edit_list: MutableSequence["EditAtom"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="EditAtom",
    )
    elementary_streams: MutableSequence["ElementaryStream"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ElementaryStream",
    )
    mux_streams: MutableSequence["MuxStream"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="MuxStream",
    )
    manifests: MutableSequence["Manifest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Manifest",
    )
    output: "Output" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Output",
    )
    ad_breaks: MutableSequence["AdBreak"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="AdBreak",
    )
    pubsub_destination: "PubsubDestination" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="PubsubDestination",
    )
    sprite_sheets: MutableSequence["SpriteSheet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="SpriteSheet",
    )
    overlays: MutableSequence["Overlay"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="Overlay",
    )
    encryptions: MutableSequence["Encryption"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="Encryption",
    )


class Input(proto.Message):
    r"""Input asset.

    Attributes:
        key (str):
            A unique key for this input. Must be
            specified when using advanced mapping and edit
            lists.
        uri (str):
            URI of the media. Input files must be at least 5 seconds in
            duration and stored in Cloud Storage (for example,
            ``gs://bucket/inputs/file.mp4``). If empty, the value is
            populated from
            [Job.input_uri][google.cloud.video.transcoder.v1.Job.input_uri].
            See `Supported input and output
            formats <https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats>`__.
        preprocessing_config (google.cloud.video.transcoder_v1.types.PreprocessingConfig):
            Preprocessing configurations.
        attributes (google.cloud.video.transcoder_v1.types.InputAttributes):
            Optional. Input Attributes.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    preprocessing_config: "PreprocessingConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PreprocessingConfig",
    )
    attributes: "InputAttributes" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="InputAttributes",
    )


class Output(proto.Message):
    r"""Location of output file(s) in a Cloud Storage bucket.

    Attributes:
        uri (str):
            URI for the output file(s). For example,
            ``gs://my-bucket/outputs/``. Must be a directory and not a
            top-level bucket. If empty, the value is populated from
            [Job.output_uri][google.cloud.video.transcoder.v1.Job.output_uri].
            See `Supported input and output
            formats <https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats>`__.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EditAtom(proto.Message):
    r"""Edit atom.

    Attributes:
        key (str):
            A unique key for this atom. Must be specified
            when using advanced mapping.
        inputs (MutableSequence[str]):
            List of
            [Input.key][google.cloud.video.transcoder.v1.Input.key]
            values identifying files that should be used in this atom.
            The listed ``inputs`` must have the same timeline.
        end_time_offset (google.protobuf.duration_pb2.Duration):
            End time in seconds for the atom, relative to the input file
            timeline. When ``end_time_offset`` is not specified, the
            ``inputs`` are used until the end of the atom.
        start_time_offset (google.protobuf.duration_pb2.Duration):
            Start time in seconds for the atom, relative to the input
            file timeline. The default is ``0s``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inputs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    start_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class AdBreak(proto.Message):
    r"""Ad break.

    Attributes:
        start_time_offset (google.protobuf.duration_pb2.Duration):
            Start time in seconds for the ad break, relative to the
            output file timeline. The default is ``0s``.
    """

    start_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class ElementaryStream(proto.Message):
    r"""Encoding of an input file such as an audio, video, or text
    track. Elementary streams must be packaged before
    mapping and sharing between different output formats.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        key (str):
            A unique key for this elementary stream.
        video_stream (google.cloud.video.transcoder_v1.types.VideoStream):
            Encoding of a video stream.

            This field is a member of `oneof`_ ``elementary_stream``.
        audio_stream (google.cloud.video.transcoder_v1.types.AudioStream):
            Encoding of an audio stream.

            This field is a member of `oneof`_ ``elementary_stream``.
        text_stream (google.cloud.video.transcoder_v1.types.TextStream):
            Encoding of a text stream. For example,
            closed captions or subtitles.

            This field is a member of `oneof`_ ``elementary_stream``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=4,
    )
    video_stream: "VideoStream" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="elementary_stream",
        message="VideoStream",
    )
    audio_stream: "AudioStream" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="elementary_stream",
        message="AudioStream",
    )
    text_stream: "TextStream" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="elementary_stream",
        message="TextStream",
    )


class MuxStream(proto.Message):
    r"""Multiplexing settings for output stream.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        key (str):
            A unique key for this multiplexed stream.
        file_name (str):
            The name of the generated file. The default is
            [MuxStream.key][google.cloud.video.transcoder.v1.MuxStream.key]
            with the extension suffix corresponding to the
            [MuxStream.container][google.cloud.video.transcoder.v1.MuxStream.container].

            Individual segments also have an incremental 10-digit
            zero-padded suffix starting from 0 before the extension,
            such as ``mux_stream0000000123.ts``.
        container (str):
            The container format. The default is ``mp4``

            Supported streaming formats:

            - ``ts``
            - ``fmp4``- the corresponding file extension is ``.m4s``

            Supported standalone file formats:

            - ``mp4``
            - ``mp3``
            - ``ogg``
            - ``vtt``

            See also: `Supported input and output
            formats <https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats>`__
        elementary_streams (MutableSequence[str]):
            List of
            [ElementaryStream.key][google.cloud.video.transcoder.v1.ElementaryStream.key]
            values multiplexed in this stream.
        segment_settings (google.cloud.video.transcoder_v1.types.SegmentSettings):
            Segment settings for ``ts``, ``fmp4`` and ``vtt``.
        encryption_id (str):
            Identifier of the encryption configuration to
            use. If omitted, output will be unencrypted.
        fmp4 (google.cloud.video.transcoder_v1.types.MuxStream.Fmp4Config):
            Optional. ``fmp4`` container configuration.

            This field is a member of `oneof`_ ``container_config``.
    """

    class Fmp4Config(proto.Message):
        r"""``fmp4`` container configuration.

        Attributes:
            codec_tag (str):
                Optional. Specify the codec tag string that will be used in
                the media bitstream. When not specified, the codec
                appropriate value is used.

                Supported H265 codec tags:

                - ``hvc1`` (default)
                - ``hev1``
        """

        codec_tag: str = proto.Field(
            proto.STRING,
            number=1,
        )

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    container: str = proto.Field(
        proto.STRING,
        number=3,
    )
    elementary_streams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    segment_settings: "SegmentSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SegmentSettings",
    )
    encryption_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    fmp4: Fmp4Config = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="container_config",
        message=Fmp4Config,
    )


class Manifest(proto.Message):
    r"""Manifest configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        file_name (str):
            The name of the generated file. The default is ``manifest``
            with the extension suffix corresponding to the
            [Manifest.type][google.cloud.video.transcoder.v1.Manifest.type].
        type_ (google.cloud.video.transcoder_v1.types.Manifest.ManifestType):
            Required. Type of the manifest.
        mux_streams (MutableSequence[str]):
            Required. List of user supplied
            [MuxStream.key][google.cloud.video.transcoder.v1.MuxStream.key]
            values that should appear in this manifest.

            When
            [Manifest.type][google.cloud.video.transcoder.v1.Manifest.type]
            is ``HLS``, a media manifest with name
            [MuxStream.key][google.cloud.video.transcoder.v1.MuxStream.key]
            and ``.m3u8`` extension is generated for each element in
            this list.
        dash (google.cloud.video.transcoder_v1.types.Manifest.DashConfig):
            ``DASH`` manifest configuration.

            This field is a member of `oneof`_ ``manifest_config``.
    """

    class ManifestType(proto.Enum):
        r"""The manifest type, which corresponds to the adaptive
        streaming format used.

        Values:
            MANIFEST_TYPE_UNSPECIFIED (0):
                The manifest type is not specified.
            HLS (1):
                Create an HLS manifest. The corresponding file extension is
                ``.m3u8``.
            DASH (2):
                Create an MPEG-DASH manifest. The corresponding file
                extension is ``.mpd``.
        """

        MANIFEST_TYPE_UNSPECIFIED = 0
        HLS = 1
        DASH = 2

    class DashConfig(proto.Message):
        r"""``DASH`` manifest configuration.

        Attributes:
            segment_reference_scheme (google.cloud.video.transcoder_v1.types.Manifest.DashConfig.SegmentReferenceScheme):
                The segment reference scheme for a ``DASH`` manifest. The
                default is ``SEGMENT_LIST``.
        """

        class SegmentReferenceScheme(proto.Enum):
            r"""The segment reference scheme for a ``DASH`` manifest.

            Values:
                SEGMENT_REFERENCE_SCHEME_UNSPECIFIED (0):
                    The segment reference scheme is not
                    specified.
                SEGMENT_LIST (1):
                    Explicitly lists the URLs of media files for each segment.
                    For example, if
                    [SegmentSettings.individual_segments][google.cloud.video.transcoder.v1.SegmentSettings.individual_segments]
                    is ``true``, then the manifest contains fields similar to
                    the following:

                    .. code:: xml

                       <Initialization sourceURL="my-hd-stream-init.m4s"/>
                         <SegmentList presentationTimeOffset="0" duration="1000"
                         timescale="10000">
                           <SegmentURL media="hd-stream0000000000.m4s"/>
                           <SegmentURL media="hd-stream0000000001.m4s"/>
                           ...
                SEGMENT_TEMPLATE_NUMBER (2):
                    [SegmentSettings.individual_segments][google.cloud.video.transcoder.v1.SegmentSettings.individual_segments]
                    must be set to ``true`` to use this segment reference
                    scheme. Uses the DASH specification ``<SegmentTemplate>``
                    tag to determine the URLs of media files for each segment.
                    For example:

                    .. code:: xml

                       <SegmentTemplate presentationTimeOffset="0" timescale="10000"
                             initialization="my-hd-stream-init.m4s"
                             media="hd-stream$Number%010d$.m4s" startNumber="0">
                         ...
            """

            SEGMENT_REFERENCE_SCHEME_UNSPECIFIED = 0
            SEGMENT_LIST = 1
            SEGMENT_TEMPLATE_NUMBER = 2

        segment_reference_scheme: "Manifest.DashConfig.SegmentReferenceScheme" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="Manifest.DashConfig.SegmentReferenceScheme",
            )
        )

    file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: ManifestType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ManifestType,
    )
    mux_streams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    dash: DashConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="manifest_config",
        message=DashConfig,
    )


class PubsubDestination(proto.Message):
    r"""A Pub/Sub destination.

    Attributes:
        topic (str):
            The name of the Pub/Sub topic to publish job completion
            notification to. For example:
            ``projects/{project}/topics/{topic}``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SpriteSheet(proto.Message):
    r"""Sprite sheet configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        format_ (str):
            Format type. The default is ``jpeg``.

            Supported formats:

            - ``jpeg``
        file_prefix (str):
            Required. File name prefix for the generated sprite sheets.

            Each sprite sheet has an incremental 10-digit zero-padded
            suffix starting from 0 before the extension, such as
            ``sprite_sheet0000000123.jpeg``.
        sprite_width_pixels (int):
            Required. The width of sprite in pixels. Must be an even
            integer. To preserve the source aspect ratio, set the
            [SpriteSheet.sprite_width_pixels][google.cloud.video.transcoder.v1.SpriteSheet.sprite_width_pixels]
            field or the
            [SpriteSheet.sprite_height_pixels][google.cloud.video.transcoder.v1.SpriteSheet.sprite_height_pixels]
            field, but not both (the API will automatically calculate
            the missing field).

            For portrait videos that contain horizontal ASR and rotation
            metadata, provide the width, in pixels, per the horizontal
            ASR. The API calculates the height per the horizontal ASR.
            The API detects any rotation metadata and swaps the
            requested height and width for the output.
        sprite_height_pixels (int):
            Required. The height of sprite in pixels. Must be an even
            integer. To preserve the source aspect ratio, set the
            [SpriteSheet.sprite_height_pixels][google.cloud.video.transcoder.v1.SpriteSheet.sprite_height_pixels]
            field or the
            [SpriteSheet.sprite_width_pixels][google.cloud.video.transcoder.v1.SpriteSheet.sprite_width_pixels]
            field, but not both (the API will automatically calculate
            the missing field).

            For portrait videos that contain horizontal ASR and rotation
            metadata, provide the height, in pixels, per the horizontal
            ASR. The API calculates the width per the horizontal ASR.
            The API detects any rotation metadata and swaps the
            requested height and width for the output.
        column_count (int):
            The maximum number of sprites per row in a
            sprite sheet. The default is 0, which indicates
            no maximum limit.
        row_count (int):
            The maximum number of rows per sprite sheet.
            When the sprite sheet is full, a new sprite
            sheet is created. The default is 0, which
            indicates no maximum limit.
        start_time_offset (google.protobuf.duration_pb2.Duration):
            Start time in seconds, relative to the output file timeline.
            Determines the first sprite to pick. The default is ``0s``.
        end_time_offset (google.protobuf.duration_pb2.Duration):
            End time in seconds, relative to the output file timeline.
            When ``end_time_offset`` is not specified, the sprites are
            generated until the end of the output file.
        total_count (int):
            Total number of sprites. Create the specified
            number of sprites distributed evenly across the
            timeline of the output media. The default is
            100.

            This field is a member of `oneof`_ ``extraction_strategy``.
        interval (google.protobuf.duration_pb2.Duration):
            Starting from ``0s``, create sprites at regular intervals.
            Specify the interval value in seconds.

            This field is a member of `oneof`_ ``extraction_strategy``.
        quality (int):
            The quality of the generated sprite sheet.
            Enter a value between 1 and 100, where 1 is the
            lowest quality and 100 is the highest quality.
            The default is 100. A high quality value
            corresponds to a low image data compression
            ratio.
    """

    format_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sprite_width_pixels: int = proto.Field(
        proto.INT32,
        number=3,
    )
    sprite_height_pixels: int = proto.Field(
        proto.INT32,
        number=4,
    )
    column_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    start_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    total_count: int = proto.Field(
        proto.INT32,
        number=9,
        oneof="extraction_strategy",
    )
    interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="extraction_strategy",
        message=duration_pb2.Duration,
    )
    quality: int = proto.Field(
        proto.INT32,
        number=11,
    )


class Overlay(proto.Message):
    r"""Overlay configuration.

    Attributes:
        image (google.cloud.video.transcoder_v1.types.Overlay.Image):
            Image overlay.
        animations (MutableSequence[google.cloud.video.transcoder_v1.types.Overlay.Animation]):
            List of animations. The list should be
            chronological, without any time overlap.
    """

    class FadeType(proto.Enum):
        r"""Fade type for the overlay: ``FADE_IN`` or ``FADE_OUT``.

        Values:
            FADE_TYPE_UNSPECIFIED (0):
                The fade type is not specified.
            FADE_IN (1):
                Fade the overlay object into view.
            FADE_OUT (2):
                Fade the overlay object out of view.
        """

        FADE_TYPE_UNSPECIFIED = 0
        FADE_IN = 1
        FADE_OUT = 2

    class NormalizedCoordinate(proto.Message):
        r"""2D normalized coordinates. Default: ``{0.0, 0.0}``

        Attributes:
            x (float):
                Normalized x coordinate.
            y (float):
                Normalized y coordinate.
        """

        x: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        y: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )

    class Image(proto.Message):
        r"""Overlaid image.

        Attributes:
            uri (str):
                Required. URI of the image in Cloud Storage. For example,
                ``gs://bucket/inputs/image.png``. Only PNG and JPEG images
                are supported.
            resolution (google.cloud.video.transcoder_v1.types.Overlay.NormalizedCoordinate):
                Normalized image resolution, based on output video
                resolution. Valid values: ``0.0``–``1.0``. To respect the
                original image aspect ratio, set either ``x`` or ``y`` to
                ``0.0``. To use the original image resolution, set both
                ``x`` and ``y`` to ``0.0``.
            alpha (float):
                Target image opacity. Valid values are from ``1.0`` (solid,
                default) to ``0.0`` (transparent), exclusive. Set this to a
                value greater than ``0.0``.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resolution: "Overlay.NormalizedCoordinate" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Overlay.NormalizedCoordinate",
        )
        alpha: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    class AnimationStatic(proto.Message):
        r"""Display static overlay object.

        Attributes:
            xy (google.cloud.video.transcoder_v1.types.Overlay.NormalizedCoordinate):
                Normalized coordinates based on output video resolution.
                Valid values: ``0.0``–``1.0``. ``xy`` is the upper-left
                coordinate of the overlay object. For example, use the x and
                y coordinates {0,0} to position the top-left corner of the
                overlay animation in the top-left corner of the output
                video.
            start_time_offset (google.protobuf.duration_pb2.Duration):
                The time to start displaying the overlay
                object, in seconds. Default: 0
        """

        xy: "Overlay.NormalizedCoordinate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Overlay.NormalizedCoordinate",
        )
        start_time_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    class AnimationFade(proto.Message):
        r"""Display overlay object with fade animation.

        Attributes:
            fade_type (google.cloud.video.transcoder_v1.types.Overlay.FadeType):
                Required. Type of fade animation: ``FADE_IN`` or
                ``FADE_OUT``.
            xy (google.cloud.video.transcoder_v1.types.Overlay.NormalizedCoordinate):
                Normalized coordinates based on output video resolution.
                Valid values: ``0.0``–``1.0``. ``xy`` is the upper-left
                coordinate of the overlay object. For example, use the x and
                y coordinates {0,0} to position the top-left corner of the
                overlay animation in the top-left corner of the output
                video.
            start_time_offset (google.protobuf.duration_pb2.Duration):
                The time to start the fade animation, in
                seconds. Default: 0
            end_time_offset (google.protobuf.duration_pb2.Duration):
                The time to end the fade animation, in seconds. Default:
                ``start_time_offset`` + 1s
        """

        fade_type: "Overlay.FadeType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Overlay.FadeType",
        )
        xy: "Overlay.NormalizedCoordinate" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Overlay.NormalizedCoordinate",
        )
        start_time_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        end_time_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )

    class AnimationEnd(proto.Message):
        r"""End previous overlay animation from the video. Without
        ``AnimationEnd``, the overlay object will keep the state of previous
        animation until the end of the video.

        Attributes:
            start_time_offset (google.protobuf.duration_pb2.Duration):
                The time to end overlay object, in seconds.
                Default: 0
        """

        start_time_offset: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    class Animation(proto.Message):
        r"""Animation types.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            animation_static (google.cloud.video.transcoder_v1.types.Overlay.AnimationStatic):
                Display static overlay object.

                This field is a member of `oneof`_ ``animation_type``.
            animation_fade (google.cloud.video.transcoder_v1.types.Overlay.AnimationFade):
                Display overlay object with fade animation.

                This field is a member of `oneof`_ ``animation_type``.
            animation_end (google.cloud.video.transcoder_v1.types.Overlay.AnimationEnd):
                End previous animation.

                This field is a member of `oneof`_ ``animation_type``.
        """

        animation_static: "Overlay.AnimationStatic" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="animation_type",
            message="Overlay.AnimationStatic",
        )
        animation_fade: "Overlay.AnimationFade" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="animation_type",
            message="Overlay.AnimationFade",
        )
        animation_end: "Overlay.AnimationEnd" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="animation_type",
            message="Overlay.AnimationEnd",
        )

    image: Image = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Image,
    )
    animations: MutableSequence[Animation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Animation,
    )


class PreprocessingConfig(proto.Message):
    r"""Preprocessing configurations.

    Attributes:
        color (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Color):
            Color preprocessing configuration.
        denoise (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Denoise):
            Denoise preprocessing configuration.
        deblock (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Deblock):
            Deblock preprocessing configuration.
        audio (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Audio):
            Audio preprocessing configuration.
        crop (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Crop):
            Specify the video cropping configuration.
        pad (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Pad):
            Specify the video pad filter configuration.
        deinterlace (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Deinterlace):
            Specify the video deinterlace configuration.
    """

    class Color(proto.Message):
        r"""Color preprocessing configuration.

        **Note:** This configuration is not supported.

        Attributes:
            saturation (float):
                Control color saturation of the video. Enter
                a value between -1 and 1, where -1 is fully
                desaturated and 1 is maximum saturation. 0 is no
                change. The default is 0.
            contrast (float):
                Control black and white contrast of the
                video. Enter a value between -1 and 1, where -1
                is minimum contrast and 1 is maximum contrast. 0
                is no change. The default is 0.
            brightness (float):
                Control brightness of the video. Enter a
                value between -1 and 1, where -1 is minimum
                brightness and 1 is maximum brightness. 0 is no
                change. The default is 0.
        """

        saturation: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        contrast: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        brightness: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    class Denoise(proto.Message):
        r"""Denoise preprocessing configuration.

        **Note:** This configuration is not supported.

        Attributes:
            strength (float):
                Set strength of the denoise. Enter a value
                between 0 and 1. The higher the value, the
                smoother the image. 0 is no denoising. The
                default is 0.
            tune (str):
                Set the denoiser mode. The default is ``standard``.

                Supported denoiser modes:

                - ``standard``
                - ``grain``
        """

        strength: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        tune: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Deblock(proto.Message):
        r"""Deblock preprocessing configuration.

        **Note:** This configuration is not supported.

        Attributes:
            strength (float):
                Set strength of the deblocker. Enter a value
                between 0 and 1. The higher the value, the
                stronger the block removal. 0 is no deblocking.
                The default is 0.
            enabled (bool):
                Enable deblocker. The default is ``false``.
        """

        strength: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        enabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class Audio(proto.Message):
        r"""Audio preprocessing configuration.

        Attributes:
            lufs (float):
                Specify audio loudness normalization in loudness units
                relative to full scale (LUFS). Enter a value between -24 and
                0 (the default), where:

                - -24 is the Advanced Television Systems Committee (ATSC
                  A/85) standard
                - -23 is the EU R128 broadcast standard
                - -19 is the prior standard for online mono audio
                - -18 is the ReplayGain standard
                - -16 is the prior standard for stereo audio
                - -14 is the new online audio standard recommended by
                  Spotify, as well as Amazon Echo
                - 0 disables normalization
            high_boost (bool):
                Enable boosting high frequency components. The default is
                ``false``.

                **Note:** This field is not supported.
            low_boost (bool):
                Enable boosting low frequency components. The default is
                ``false``.

                **Note:** This field is not supported.
        """

        lufs: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        high_boost: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        low_boost: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class Crop(proto.Message):
        r"""Video cropping configuration for the input video. The cropped
        input video is scaled to match the output resolution.

        Attributes:
            top_pixels (int):
                The number of pixels to crop from the top.
                The default is 0.
            bottom_pixels (int):
                The number of pixels to crop from the bottom.
                The default is 0.
            left_pixels (int):
                The number of pixels to crop from the left.
                The default is 0.
            right_pixels (int):
                The number of pixels to crop from the right.
                The default is 0.
        """

        top_pixels: int = proto.Field(
            proto.INT32,
            number=1,
        )
        bottom_pixels: int = proto.Field(
            proto.INT32,
            number=2,
        )
        left_pixels: int = proto.Field(
            proto.INT32,
            number=3,
        )
        right_pixels: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class Pad(proto.Message):
        r"""Pad filter configuration for the input video. The padded
        input video is scaled after padding with black to match the
        output resolution.

        Attributes:
            top_pixels (int):
                The number of pixels to add to the top. The
                default is 0.
            bottom_pixels (int):
                The number of pixels to add to the bottom.
                The default is 0.
            left_pixels (int):
                The number of pixels to add to the left. The
                default is 0.
            right_pixels (int):
                The number of pixels to add to the right. The
                default is 0.
        """

        top_pixels: int = proto.Field(
            proto.INT32,
            number=1,
        )
        bottom_pixels: int = proto.Field(
            proto.INT32,
            number=2,
        )
        left_pixels: int = proto.Field(
            proto.INT32,
            number=3,
        )
        right_pixels: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class Deinterlace(proto.Message):
        r"""Deinterlace configuration for input video.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            yadif (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Deinterlace.YadifConfig):
                Specifies the Yet Another Deinterlacing
                Filter Configuration.

                This field is a member of `oneof`_ ``deinterlacing_filter``.
            bwdif (google.cloud.video.transcoder_v1.types.PreprocessingConfig.Deinterlace.BwdifConfig):
                Specifies the Bob Weaver Deinterlacing Filter
                Configuration.

                This field is a member of `oneof`_ ``deinterlacing_filter``.
        """

        class YadifConfig(proto.Message):
            r"""Yet Another Deinterlacing Filter Configuration.

            Attributes:
                mode (str):
                    Specifies the deinterlacing mode to adopt. The default is
                    ``send_frame``. Supported values:

                    - ``send_frame``: Output one frame for each frame
                    - ``send_field``: Output one frame for each field
                disable_spatial_interlacing (bool):
                    Disable spacial interlacing. The default is ``false``.
                parity (str):
                    The picture field parity assumed for the input interlaced
                    video. The default is ``auto``. Supported values:

                    - ``tff``: Assume the top field is first
                    - ``bff``: Assume the bottom field is first
                    - ``auto``: Enable automatic detection of field parity
                deinterlace_all_frames (bool):
                    Deinterlace all frames rather than just the frames
                    identified as interlaced. The default is ``false``.
            """

            mode: str = proto.Field(
                proto.STRING,
                number=1,
            )
            disable_spatial_interlacing: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            parity: str = proto.Field(
                proto.STRING,
                number=3,
            )
            deinterlace_all_frames: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        class BwdifConfig(proto.Message):
            r"""Bob Weaver Deinterlacing Filter Configuration.

            Attributes:
                mode (str):
                    Specifies the deinterlacing mode to adopt. The default is
                    ``send_frame``. Supported values:

                    - ``send_frame``: Output one frame for each frame
                    - ``send_field``: Output one frame for each field
                parity (str):
                    The picture field parity assumed for the input interlaced
                    video. The default is ``auto``. Supported values:

                    - ``tff``: Assume the top field is first
                    - ``bff``: Assume the bottom field is first
                    - ``auto``: Enable automatic detection of field parity
                deinterlace_all_frames (bool):
                    Deinterlace all frames rather than just the frames
                    identified as interlaced. The default is ``false``.
            """

            mode: str = proto.Field(
                proto.STRING,
                number=1,
            )
            parity: str = proto.Field(
                proto.STRING,
                number=2,
            )
            deinterlace_all_frames: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        yadif: "PreprocessingConfig.Deinterlace.YadifConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="deinterlacing_filter",
            message="PreprocessingConfig.Deinterlace.YadifConfig",
        )
        bwdif: "PreprocessingConfig.Deinterlace.BwdifConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="deinterlacing_filter",
            message="PreprocessingConfig.Deinterlace.BwdifConfig",
        )

    color: Color = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Color,
    )
    denoise: Denoise = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Denoise,
    )
    deblock: Deblock = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Deblock,
    )
    audio: Audio = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Audio,
    )
    crop: Crop = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Crop,
    )
    pad: Pad = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Pad,
    )
    deinterlace: Deinterlace = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Deinterlace,
    )


class TrackDefinition(proto.Message):
    r"""Track definition for the input asset.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        input_track (int):
            The input track.

            This field is a member of `oneof`_ ``_input_track``.
        languages (MutableSequence[str]):
            Optional. A list of languages spoken in the input asset,
            represented by a BCP 47 language code, such as "en-US" or
            "sr-Latn". For more information, see
            https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
        detect_languages (bool):
            Optional. Whether to automatically detect the
            languages present in the track. If true, the
            system will attempt to identify all the
            languages present in the track and populate the
            languages field.
        detected_languages (MutableSequence[str]):
            Output only. A list of languages detected in the input
            asset, represented by a BCP 47 language code, such as
            "en-US" or "sr-Latn". For more information, see
            https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
            This field is only populated if the detect_languages field
            is set to true.
    """

    input_track: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    languages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    detect_languages: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    detected_languages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class InputAttributes(proto.Message):
    r"""Input attributes that provide additional information about
    the input asset.

    Attributes:
        track_definitions (MutableSequence[google.cloud.video.transcoder_v1.types.TrackDefinition]):
            Optional. A list of track definitions for the
            input asset.
    """

    track_definitions: MutableSequence["TrackDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TrackDefinition",
    )


class VideoStream(proto.Message):
    r"""Video stream resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        h264 (google.cloud.video.transcoder_v1.types.VideoStream.H264CodecSettings):
            H264 codec settings.

            This field is a member of `oneof`_ ``codec_settings``.
        h265 (google.cloud.video.transcoder_v1.types.VideoStream.H265CodecSettings):
            H265 codec settings.

            This field is a member of `oneof`_ ``codec_settings``.
        vp9 (google.cloud.video.transcoder_v1.types.VideoStream.Vp9CodecSettings):
            VP9 codec settings.

            This field is a member of `oneof`_ ``codec_settings``.
    """

    class FrameRateConversionStrategy(proto.Enum):
        r"""The conversion strategy for desired frame rate.

        Values:
            FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED (0):
                Unspecified frame rate conversion strategy.
            DOWNSAMPLE (1):
                Selectively retain frames to reduce the output frame rate.
                Every *n* th frame is kept, where
                ``n = ceil(input frame rate / target frame rate)``. When *n*
                = 1 (that is, the target frame rate is greater than the
                input frame rate), the output frame rate matches the input
                frame rate. When *n* > 1, frames are dropped and the output
                frame rate is equal to ``(input frame rate / n)``. For more
                information, see `Calculate frame
                rate <https://cloud.google.com/transcoder/docs/concepts/frame-rate>`__.
            DROP_DUPLICATE (2):
                Drop or duplicate frames to match the
                specified frame rate.
        """

        FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED = 0
        DOWNSAMPLE = 1
        DROP_DUPLICATE = 2

    class H264ColorFormatSDR(proto.Message):
        r"""Convert the input video to a Standard Dynamic Range (SDR)
        video.

        """

    class H264ColorFormatHLG(proto.Message):
        r"""Convert the input video to a Hybrid Log Gamma (HLG) video."""

    class H264CodecSettings(proto.Message):
        r"""H264 codec settings.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            width_pixels (int):
                The width of the video in pixels. Must be an
                even integer. When not specified, the width is
                adjusted to match the specified height and input
                aspect ratio. If both are omitted, the input
                width is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the width, in
                pixels, per the horizontal ASR. The API
                calculates the height per the horizontal ASR.
                The API detects any rotation metadata and swaps
                the requested height and width for the output.
            height_pixels (int):
                The height of the video in pixels. Must be an
                even integer. When not specified, the height is
                adjusted to match the specified width and input
                aspect ratio. If both are omitted, the input
                height is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the height, in
                pixels, per the horizontal ASR. The API
                calculates the width per the horizontal ASR. The
                API detects any rotation metadata and swaps the
                requested height and width for the output.
            frame_rate (float):
                Required. The target video frame rate in
                frames per second (FPS). Must be less than or
                equal to 120.
            frame_rate_conversion_strategy (google.cloud.video.transcoder_v1.types.VideoStream.FrameRateConversionStrategy):
                Optional. Frame rate conversion strategy for desired frame
                rate. The default is ``DOWNSAMPLE``.
            bitrate_bps (int):
                Required. The video bitrate in bits per
                second. The minimum value is 1,000. The maximum
                value is 800,000,000.
            pixel_format (str):
                Pixel format to use. The default is ``yuv420p``.

                Supported pixel formats:

                - ``yuv420p`` pixel format
                - ``yuv422p`` pixel format
                - ``yuv444p`` pixel format
                - ``yuv420p10`` 10-bit HDR pixel format
                - ``yuv422p10`` 10-bit HDR pixel format
                - ``yuv444p10`` 10-bit HDR pixel format
                - ``yuv420p12`` 12-bit HDR pixel format
                - ``yuv422p12`` 12-bit HDR pixel format
                - ``yuv444p12`` 12-bit HDR pixel format
            rate_control_mode (str):
                Specify the mode. The default is ``vbr``.

                Supported rate control modes:

                - ``vbr`` - variable bitrate
                - ``crf`` - constant rate factor
            crf_level (int):
                Target CRF level. Must be between 10 and 36,
                where 10 is the highest quality and 36 is the
                most efficient compression. The default is 21.
            allow_open_gop (bool):
                Specifies whether an open Group of Pictures (GOP) structure
                should be allowed or not. The default is ``false``.
            gop_frame_count (int):
                Select the GOP size based on the specified
                frame count. Must be greater than zero.

                This field is a member of `oneof`_ ``gop_mode``.
            gop_duration (google.protobuf.duration_pb2.Duration):
                Select the GOP size based on the specified duration. The
                default is ``3s``. Note that ``gopDuration`` must be less
                than or equal to ```segmentDuration`` <#SegmentSettings>`__,
                and ```segmentDuration`` <#SegmentSettings>`__ must be
                divisible by ``gopDuration``.

                This field is a member of `oneof`_ ``gop_mode``.
            enable_two_pass (bool):
                Use two-pass encoding strategy to achieve better video
                quality.
                [H264CodecSettings.rate_control_mode][google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.rate_control_mode]
                must be ``vbr``. The default is ``false``.
            vbv_size_bits (int):
                Size of the Video Buffering Verifier (VBV) buffer in bits.
                Must be greater than zero. The default is equal to
                [H264CodecSettings.bitrate_bps][google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.bitrate_bps].
            vbv_fullness_bits (int):
                Initial fullness of the Video Buffering Verifier (VBV)
                buffer in bits. Must be greater than zero. The default is
                equal to 90% of
                [H264CodecSettings.vbv_size_bits][google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.vbv_size_bits].
            entropy_coder (str):
                The entropy coder to use. The default is ``cabac``.

                Supported entropy coders:

                - ``cavlc``
                - ``cabac``
            b_pyramid (bool):
                Allow B-pyramid for reference frame selection. This may not
                be supported on all decoders. The default is ``false``.
            b_frame_count (int):
                The number of consecutive B-frames. Must be greater than or
                equal to zero. Must be less than
                [H264CodecSettings.gop_frame_count][google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.gop_frame_count]
                if set. The default is 0.
            aq_strength (float):
                Specify the intensity of the adaptive
                quantizer (AQ). Must be between 0 and 1, where 0
                disables the quantizer and 1 maximizes the
                quantizer. A higher value equals a lower bitrate
                but smoother image. The default is 0.
            profile (str):
                Enforces the specified codec profile. The following profiles
                are supported:

                - ``baseline``
                - ``main``
                - ``high`` (default)

                The available options are
                `FFmpeg-compatible <https://trac.ffmpeg.org/wiki/Encode/H.264#Tune>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``H264CodecSettings`` message.
            tune (str):
                Enforces the specified codec tune. The available options are
                `FFmpeg-compatible <https://trac.ffmpeg.org/wiki/Encode/H.264#Tune>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``H264CodecSettings`` message.
            preset (str):
                Enforces the specified codec preset. The default is
                ``veryfast``. The available options are
                `FFmpeg-compatible <https://trac.ffmpeg.org/wiki/Encode/H.264#Preset>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``H264CodecSettings`` message.
            sdr (google.cloud.video.transcoder_v1.types.VideoStream.H264ColorFormatSDR):
                Optional. SDR color format setting for H264.

                This field is a member of `oneof`_ ``color_format``.
            hlg (google.cloud.video.transcoder_v1.types.VideoStream.H264ColorFormatHLG):
                Optional. HLG color format setting for H264.

                This field is a member of `oneof`_ ``color_format``.
        """

        width_pixels: int = proto.Field(
            proto.INT32,
            number=1,
        )
        height_pixels: int = proto.Field(
            proto.INT32,
            number=2,
        )
        frame_rate: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )
        frame_rate_conversion_strategy: "VideoStream.FrameRateConversionStrategy" = (
            proto.Field(
                proto.ENUM,
                number=23,
                enum="VideoStream.FrameRateConversionStrategy",
            )
        )
        bitrate_bps: int = proto.Field(
            proto.INT32,
            number=4,
        )
        pixel_format: str = proto.Field(
            proto.STRING,
            number=5,
        )
        rate_control_mode: str = proto.Field(
            proto.STRING,
            number=6,
        )
        crf_level: int = proto.Field(
            proto.INT32,
            number=7,
        )
        allow_open_gop: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        gop_frame_count: int = proto.Field(
            proto.INT32,
            number=9,
            oneof="gop_mode",
        )
        gop_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="gop_mode",
            message=duration_pb2.Duration,
        )
        enable_two_pass: bool = proto.Field(
            proto.BOOL,
            number=11,
        )
        vbv_size_bits: int = proto.Field(
            proto.INT32,
            number=12,
        )
        vbv_fullness_bits: int = proto.Field(
            proto.INT32,
            number=13,
        )
        entropy_coder: str = proto.Field(
            proto.STRING,
            number=14,
        )
        b_pyramid: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        b_frame_count: int = proto.Field(
            proto.INT32,
            number=16,
        )
        aq_strength: float = proto.Field(
            proto.DOUBLE,
            number=17,
        )
        profile: str = proto.Field(
            proto.STRING,
            number=18,
        )
        tune: str = proto.Field(
            proto.STRING,
            number=19,
        )
        preset: str = proto.Field(
            proto.STRING,
            number=20,
        )
        sdr: "VideoStream.H264ColorFormatSDR" = proto.Field(
            proto.MESSAGE,
            number=21,
            oneof="color_format",
            message="VideoStream.H264ColorFormatSDR",
        )
        hlg: "VideoStream.H264ColorFormatHLG" = proto.Field(
            proto.MESSAGE,
            number=22,
            oneof="color_format",
            message="VideoStream.H264ColorFormatHLG",
        )

    class H265ColorFormatSDR(proto.Message):
        r"""Convert the input video to a Standard Dynamic Range (SDR)
        video.

        """

    class H265ColorFormatHLG(proto.Message):
        r"""Convert the input video to a Hybrid Log Gamma (HLG) video."""

    class H265ColorFormatHDR10(proto.Message):
        r"""Convert the input video to a High Dynamic Range 10 (HDR10)
        video.

        """

    class H265CodecSettings(proto.Message):
        r"""H265 codec settings.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            width_pixels (int):
                The width of the video in pixels. Must be an
                even integer. When not specified, the width is
                adjusted to match the specified height and input
                aspect ratio. If both are omitted, the input
                width is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the width, in
                pixels, per the horizontal ASR. The API
                calculates the height per the horizontal ASR.
                The API detects any rotation metadata and swaps
                the requested height and width for the output.
            height_pixels (int):
                The height of the video in pixels. Must be an
                even integer. When not specified, the height is
                adjusted to match the specified width and input
                aspect ratio. If both are omitted, the input
                height is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the height, in
                pixels, per the horizontal ASR. The API
                calculates the width per the horizontal ASR. The
                API detects any rotation metadata and swaps the
                requested height and width for the output.
            frame_rate (float):
                Required. The target video frame rate in
                frames per second (FPS). Must be less than or
                equal to 120.
            frame_rate_conversion_strategy (google.cloud.video.transcoder_v1.types.VideoStream.FrameRateConversionStrategy):
                Optional. Frame rate conversion strategy for desired frame
                rate. The default is ``DOWNSAMPLE``.
            bitrate_bps (int):
                Required. The video bitrate in bits per
                second. The minimum value is 1,000. The maximum
                value is 800,000,000.
            pixel_format (str):
                Pixel format to use. The default is ``yuv420p``.

                Supported pixel formats:

                - ``yuv420p`` pixel format
                - ``yuv422p`` pixel format
                - ``yuv444p`` pixel format
                - ``yuv420p10`` 10-bit HDR pixel format
                - ``yuv422p10`` 10-bit HDR pixel format
                - ``yuv444p10`` 10-bit HDR pixel format
                - ``yuv420p12`` 12-bit HDR pixel format
                - ``yuv422p12`` 12-bit HDR pixel format
                - ``yuv444p12`` 12-bit HDR pixel format
            rate_control_mode (str):
                Specify the mode. The default is ``vbr``.

                Supported rate control modes:

                - ``vbr`` - variable bitrate
                - ``crf`` - constant rate factor
            crf_level (int):
                Target CRF level. Must be between 10 and 36,
                where 10 is the highest quality and 36 is the
                most efficient compression. The default is 21.
            allow_open_gop (bool):
                Specifies whether an open Group of Pictures (GOP) structure
                should be allowed or not. The default is ``false``.
            gop_frame_count (int):
                Select the GOP size based on the specified
                frame count. Must be greater than zero.

                This field is a member of `oneof`_ ``gop_mode``.
            gop_duration (google.protobuf.duration_pb2.Duration):
                Select the GOP size based on the specified duration. The
                default is ``3s``. Note that ``gopDuration`` must be less
                than or equal to ```segmentDuration`` <#SegmentSettings>`__,
                and ```segmentDuration`` <#SegmentSettings>`__ must be
                divisible by ``gopDuration``.

                This field is a member of `oneof`_ ``gop_mode``.
            enable_two_pass (bool):
                Use two-pass encoding strategy to achieve better video
                quality.
                [H265CodecSettings.rate_control_mode][google.cloud.video.transcoder.v1.VideoStream.H265CodecSettings.rate_control_mode]
                must be ``vbr``. The default is ``false``.
            vbv_size_bits (int):
                Size of the Video Buffering Verifier (VBV) buffer in bits.
                Must be greater than zero. The default is equal to
                ``VideoStream.bitrate_bps``.
            vbv_fullness_bits (int):
                Initial fullness of the Video Buffering Verifier (VBV)
                buffer in bits. Must be greater than zero. The default is
                equal to 90% of
                [H265CodecSettings.vbv_size_bits][google.cloud.video.transcoder.v1.VideoStream.H265CodecSettings.vbv_size_bits].
            b_pyramid (bool):
                Allow B-pyramid for reference frame selection. This may not
                be supported on all decoders. The default is ``false``.
            b_frame_count (int):
                The number of consecutive B-frames. Must be greater than or
                equal to zero. Must be less than
                [H265CodecSettings.gop_frame_count][google.cloud.video.transcoder.v1.VideoStream.H265CodecSettings.gop_frame_count]
                if set. The default is 0.
            aq_strength (float):
                Specify the intensity of the adaptive
                quantizer (AQ). Must be between 0 and 1, where 0
                disables the quantizer and 1 maximizes the
                quantizer. A higher value equals a lower bitrate
                but smoother image. The default is 0.
            profile (str):
                Enforces the specified codec profile. The following profiles
                are supported:

                - 8-bit profiles

                  - ``main`` (default)
                  - ``main-intra``
                  - ``mainstillpicture``

                - 10-bit profiles

                  - ``main10`` (default)
                  - ``main10-intra``
                  - ``main422-10``
                  - ``main422-10-intra``
                  - ``main444-10``
                  - ``main444-10-intra``

                - 12-bit profiles

                  - ``main12`` (default)
                  - ``main12-intra``
                  - ``main422-12``
                  - ``main422-12-intra``
                  - ``main444-12``
                  - ``main444-12-intra``

                The available options are
                `FFmpeg-compatible <https://x265.readthedocs.io/>`__. Note
                that certain values for this field may cause the transcoder
                to override other fields you set in the
                ``H265CodecSettings`` message.
            tune (str):
                Enforces the specified codec tune. The available options are
                `FFmpeg-compatible <https://trac.ffmpeg.org/wiki/Encode/H.265>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``H265CodecSettings`` message.
            preset (str):
                Enforces the specified codec preset. The default is
                ``veryfast``. The available options are
                `FFmpeg-compatible <https://trac.ffmpeg.org/wiki/Encode/H.265>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``H265CodecSettings`` message.
            sdr (google.cloud.video.transcoder_v1.types.VideoStream.H265ColorFormatSDR):
                Optional. SDR color format setting for H265.

                This field is a member of `oneof`_ ``color_format``.
            hlg (google.cloud.video.transcoder_v1.types.VideoStream.H265ColorFormatHLG):
                Optional. HLG color format setting for H265.

                This field is a member of `oneof`_ ``color_format``.
            hdr10 (google.cloud.video.transcoder_v1.types.VideoStream.H265ColorFormatHDR10):
                Optional. HDR10 color format setting for
                H265.

                This field is a member of `oneof`_ ``color_format``.
        """

        width_pixels: int = proto.Field(
            proto.INT32,
            number=1,
        )
        height_pixels: int = proto.Field(
            proto.INT32,
            number=2,
        )
        frame_rate: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )
        frame_rate_conversion_strategy: "VideoStream.FrameRateConversionStrategy" = (
            proto.Field(
                proto.ENUM,
                number=23,
                enum="VideoStream.FrameRateConversionStrategy",
            )
        )
        bitrate_bps: int = proto.Field(
            proto.INT32,
            number=4,
        )
        pixel_format: str = proto.Field(
            proto.STRING,
            number=5,
        )
        rate_control_mode: str = proto.Field(
            proto.STRING,
            number=6,
        )
        crf_level: int = proto.Field(
            proto.INT32,
            number=7,
        )
        allow_open_gop: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        gop_frame_count: int = proto.Field(
            proto.INT32,
            number=9,
            oneof="gop_mode",
        )
        gop_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="gop_mode",
            message=duration_pb2.Duration,
        )
        enable_two_pass: bool = proto.Field(
            proto.BOOL,
            number=11,
        )
        vbv_size_bits: int = proto.Field(
            proto.INT32,
            number=12,
        )
        vbv_fullness_bits: int = proto.Field(
            proto.INT32,
            number=13,
        )
        b_pyramid: bool = proto.Field(
            proto.BOOL,
            number=14,
        )
        b_frame_count: int = proto.Field(
            proto.INT32,
            number=15,
        )
        aq_strength: float = proto.Field(
            proto.DOUBLE,
            number=16,
        )
        profile: str = proto.Field(
            proto.STRING,
            number=17,
        )
        tune: str = proto.Field(
            proto.STRING,
            number=18,
        )
        preset: str = proto.Field(
            proto.STRING,
            number=19,
        )
        sdr: "VideoStream.H265ColorFormatSDR" = proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="color_format",
            message="VideoStream.H265ColorFormatSDR",
        )
        hlg: "VideoStream.H265ColorFormatHLG" = proto.Field(
            proto.MESSAGE,
            number=21,
            oneof="color_format",
            message="VideoStream.H265ColorFormatHLG",
        )
        hdr10: "VideoStream.H265ColorFormatHDR10" = proto.Field(
            proto.MESSAGE,
            number=22,
            oneof="color_format",
            message="VideoStream.H265ColorFormatHDR10",
        )

    class Vp9ColorFormatSDR(proto.Message):
        r"""Convert the input video to a Standard Dynamic Range (SDR)
        video.

        """

    class Vp9ColorFormatHLG(proto.Message):
        r"""Convert the input video to a Hybrid Log Gamma (HLG) video."""

    class Vp9CodecSettings(proto.Message):
        r"""VP9 codec settings.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            width_pixels (int):
                The width of the video in pixels. Must be an
                even integer. When not specified, the width is
                adjusted to match the specified height and input
                aspect ratio. If both are omitted, the input
                width is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the width, in
                pixels, per the horizontal ASR. The API
                calculates the height per the horizontal ASR.
                The API detects any rotation metadata and swaps
                the requested height and width for the output.
            height_pixels (int):
                The height of the video in pixels. Must be an
                even integer. When not specified, the height is
                adjusted to match the specified width and input
                aspect ratio. If both are omitted, the input
                height is used.

                For portrait videos that contain horizontal ASR
                and rotation metadata, provide the height, in
                pixels, per the horizontal ASR. The API
                calculates the width per the horizontal ASR. The
                API detects any rotation metadata and swaps the
                requested height and width for the output.
            frame_rate (float):
                Required. The target video frame rate in
                frames per second (FPS). Must be less than or
                equal to 120.
            frame_rate_conversion_strategy (google.cloud.video.transcoder_v1.types.VideoStream.FrameRateConversionStrategy):
                Optional. Frame rate conversion strategy for desired frame
                rate. The default is ``DOWNSAMPLE``.
            bitrate_bps (int):
                Required. The video bitrate in bits per
                second. The minimum value is 1,000. The maximum
                value is 480,000,000.
            pixel_format (str):
                Pixel format to use. The default is ``yuv420p``.

                Supported pixel formats:

                - ``yuv420p`` pixel format
                - ``yuv422p`` pixel format
                - ``yuv444p`` pixel format
                - ``yuv420p10`` 10-bit HDR pixel format
                - ``yuv422p10`` 10-bit HDR pixel format
                - ``yuv444p10`` 10-bit HDR pixel format
                - ``yuv420p12`` 12-bit HDR pixel format
                - ``yuv422p12`` 12-bit HDR pixel format
                - ``yuv444p12`` 12-bit HDR pixel format
            rate_control_mode (str):
                Specify the mode. The default is ``vbr``.

                Supported rate control modes:

                - ``vbr`` - variable bitrate
            crf_level (int):
                Target CRF level. Must be between 10 and 36, where 10 is the
                highest quality and 36 is the most efficient compression.
                The default is 21.

                **Note:** This field is not supported.
            gop_frame_count (int):
                Select the GOP size based on the specified
                frame count. Must be greater than zero.

                This field is a member of `oneof`_ ``gop_mode``.
            gop_duration (google.protobuf.duration_pb2.Duration):
                Select the GOP size based on the specified duration. The
                default is ``3s``. Note that ``gopDuration`` must be less
                than or equal to ```segmentDuration`` <#SegmentSettings>`__,
                and ```segmentDuration`` <#SegmentSettings>`__ must be
                divisible by ``gopDuration``.

                This field is a member of `oneof`_ ``gop_mode``.
            profile (str):
                Enforces the specified codec profile. The following profiles
                are supported:

                - ``profile0`` (default)
                - ``profile1``
                - ``profile2``
                - ``profile3``

                The available options are
                `WebM-compatible <https://www.webmproject.org/vp9/profiles/>`__.
                Note that certain values for this field may cause the
                transcoder to override other fields you set in the
                ``Vp9CodecSettings`` message.
            sdr (google.cloud.video.transcoder_v1.types.VideoStream.Vp9ColorFormatSDR):
                Optional. SDR color format setting for VP9.

                This field is a member of `oneof`_ ``color_format``.
            hlg (google.cloud.video.transcoder_v1.types.VideoStream.Vp9ColorFormatHLG):
                Optional. HLG color format setting for VP9.

                This field is a member of `oneof`_ ``color_format``.
        """

        width_pixels: int = proto.Field(
            proto.INT32,
            number=1,
        )
        height_pixels: int = proto.Field(
            proto.INT32,
            number=2,
        )
        frame_rate: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )
        frame_rate_conversion_strategy: "VideoStream.FrameRateConversionStrategy" = (
            proto.Field(
                proto.ENUM,
                number=13,
                enum="VideoStream.FrameRateConversionStrategy",
            )
        )
        bitrate_bps: int = proto.Field(
            proto.INT32,
            number=4,
        )
        pixel_format: str = proto.Field(
            proto.STRING,
            number=5,
        )
        rate_control_mode: str = proto.Field(
            proto.STRING,
            number=6,
        )
        crf_level: int = proto.Field(
            proto.INT32,
            number=7,
        )
        gop_frame_count: int = proto.Field(
            proto.INT32,
            number=8,
            oneof="gop_mode",
        )
        gop_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="gop_mode",
            message=duration_pb2.Duration,
        )
        profile: str = proto.Field(
            proto.STRING,
            number=10,
        )
        sdr: "VideoStream.Vp9ColorFormatSDR" = proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="color_format",
            message="VideoStream.Vp9ColorFormatSDR",
        )
        hlg: "VideoStream.Vp9ColorFormatHLG" = proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="color_format",
            message="VideoStream.Vp9ColorFormatHLG",
        )

    h264: H264CodecSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="codec_settings",
        message=H264CodecSettings,
    )
    h265: H265CodecSettings = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="codec_settings",
        message=H265CodecSettings,
    )
    vp9: Vp9CodecSettings = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="codec_settings",
        message=Vp9CodecSettings,
    )


class AudioStream(proto.Message):
    r"""Audio stream resource.

    Attributes:
        codec (str):
            The codec for this audio stream. The default is ``aac``.

            Supported audio codecs:

            - ``aac``
            - ``aac-he``
            - ``aac-he-v2``
            - ``mp3``
            - ``ac3``
            - ``eac3``
            - ``vorbis``
        bitrate_bps (int):
            Required. Audio bitrate in bits per second.
            Must be between 1 and 10,000,000.
        channel_count (int):
            Number of audio channels. Must be between 1
            and 6. The default is 2.
        channel_layout (MutableSequence[str]):
            A list of channel names specifying layout of the audio
            channels. This only affects the metadata embedded in the
            container headers, if supported by the specified format. The
            default is ``["fl", "fr"]``.

            Supported channel names:

            - ``fl`` - Front left channel
            - ``fr`` - Front right channel
            - ``sl`` - Side left channel
            - ``sr`` - Side right channel
            - ``fc`` - Front center channel
            - ``lfe`` - Low frequency
        mapping_ (MutableSequence[google.cloud.video.transcoder_v1.types.AudioStream.AudioMapping]):
            The mapping for the
            [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list]
            atoms with audio
            [EditAtom.inputs][google.cloud.video.transcoder.v1.EditAtom.inputs].
        sample_rate_hertz (int):
            The audio sample rate in Hertz. The default
            is 48000 Hertz.
        language_code (str):
            The BCP-47 language code, such as ``en-US`` or ``sr-Latn``.
            For more information, see
            https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
            Not supported in MP4 files.
        display_name (str):
            The name for this particular audio stream
            that will be added to the HLS/DASH manifest. Not
            supported in MP4 files.
    """

    class AudioMapping(proto.Message):
        r"""The mapping for the
        [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list]
        atoms with audio
        [EditAtom.inputs][google.cloud.video.transcoder.v1.EditAtom.inputs].

        Attributes:
            atom_key (str):
                Required. The
                [EditAtom.key][google.cloud.video.transcoder.v1.EditAtom.key]
                that references the atom with audio inputs in the
                [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list].
            input_key (str):
                Required. The
                [Input.key][google.cloud.video.transcoder.v1.Input.key] that
                identifies the input file.
            input_track (int):
                Required. The zero-based index of the track
                in the input file.
            input_channel (int):
                Required. The zero-based index of the channel
                in the input audio stream.
            output_channel (int):
                Required. The zero-based index of the channel
                in the output audio stream.
            gain_db (float):
                Audio volume control in dB. Negative values
                decrease volume, positive values increase. The
                default is 0.
        """

        atom_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        input_key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        input_track: int = proto.Field(
            proto.INT32,
            number=3,
        )
        input_channel: int = proto.Field(
            proto.INT32,
            number=4,
        )
        output_channel: int = proto.Field(
            proto.INT32,
            number=5,
        )
        gain_db: float = proto.Field(
            proto.DOUBLE,
            number=6,
        )

    codec: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bitrate_bps: int = proto.Field(
        proto.INT32,
        number=2,
    )
    channel_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    channel_layout: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    mapping_: MutableSequence[AudioMapping] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=AudioMapping,
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=6,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )


class TextStream(proto.Message):
    r"""Encoding of a text stream. For example, closed captions or
    subtitles.

    Attributes:
        codec (str):
            The codec for this text stream. The default is ``webvtt``.

            Supported text codecs:

            - ``srt``
            - ``ttml``
            - ``cea608``
            - ``cea708``
            - ``webvtt``
        language_code (str):
            The BCP-47 language code, such as ``en-US`` or ``sr-Latn``.
            For more information, see
            https://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
            Not supported in MP4 files.
        mapping_ (MutableSequence[google.cloud.video.transcoder_v1.types.TextStream.TextMapping]):
            The mapping for the
            [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list]
            atoms with text
            [EditAtom.inputs][google.cloud.video.transcoder.v1.EditAtom.inputs].
        display_name (str):
            The name for this particular text stream that
            will be added to the HLS/DASH manifest. Not
            supported in MP4 files.
    """

    class TextMapping(proto.Message):
        r"""The mapping for the
        [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list]
        atoms with text
        [EditAtom.inputs][google.cloud.video.transcoder.v1.EditAtom.inputs].

        Attributes:
            atom_key (str):
                Required. The
                [EditAtom.key][google.cloud.video.transcoder.v1.EditAtom.key]
                that references atom with text inputs in the
                [JobConfig.edit_list][google.cloud.video.transcoder.v1.JobConfig.edit_list].
            input_key (str):
                Required. The
                [Input.key][google.cloud.video.transcoder.v1.Input.key] that
                identifies the input file.
            input_track (int):
                Required. The zero-based index of the track
                in the input file.
        """

        atom_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        input_key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        input_track: int = proto.Field(
            proto.INT32,
            number=3,
        )

    codec: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mapping_: MutableSequence[TextMapping] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=TextMapping,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SegmentSettings(proto.Message):
    r"""Segment settings for ``ts``, ``fmp4`` and ``vtt``.

    Attributes:
        segment_duration (google.protobuf.duration_pb2.Duration):
            Duration of the segments in seconds. The default is
            ``6.0s``. Note that ``segmentDuration`` must be greater than
            or equal to ```gopDuration`` <#videostream>`__, and
            ``segmentDuration`` must be divisible by
            ```gopDuration`` <#videostream>`__.
        individual_segments (bool):
            Required. Create an individual segment file. The default is
            ``false``.
    """

    segment_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    individual_segments: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Encryption(proto.Message):
    r"""Encryption settings.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Required. Identifier for this set of
            encryption options.
        aes_128 (google.cloud.video.transcoder_v1.types.Encryption.Aes128Encryption):
            Configuration for AES-128 encryption.

            This field is a member of `oneof`_ ``encryption_mode``.
        sample_aes (google.cloud.video.transcoder_v1.types.Encryption.SampleAesEncryption):
            Configuration for SAMPLE-AES encryption.

            This field is a member of `oneof`_ ``encryption_mode``.
        mpeg_cenc (google.cloud.video.transcoder_v1.types.Encryption.MpegCommonEncryption):
            Configuration for MPEG Common Encryption
            (MPEG-CENC).

            This field is a member of `oneof`_ ``encryption_mode``.
        secret_manager_key_source (google.cloud.video.transcoder_v1.types.Encryption.SecretManagerSource):
            Keys are stored in Google Secret Manager.

            This field is a member of `oneof`_ ``secret_source``.
        drm_systems (google.cloud.video.transcoder_v1.types.Encryption.DrmSystems):
            Required. DRM system(s) to use; at least one
            must be specified. If a DRM system is omitted,
            it is considered disabled.
    """

    class Aes128Encryption(proto.Message):
        r"""Configuration for AES-128 encryption."""

    class SampleAesEncryption(proto.Message):
        r"""Configuration for SAMPLE-AES encryption."""

    class MpegCommonEncryption(proto.Message):
        r"""Configuration for MPEG Common Encryption (MPEG-CENC).

        Attributes:
            scheme (str):
                Required. Specify the encryption scheme.

                Supported encryption schemes:

                - ``cenc``
                - ``cbcs``
        """

        scheme: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class SecretManagerSource(proto.Message):
        r"""Configuration for secrets stored in Google Secret Manager.

        Attributes:
            secret_version (str):
                Required. The name of the Secret Version containing the
                encryption key in the following format:
                ``projects/{project}/secrets/{secret_id}/versions/{version_number}``

                Note that only numbered versions are supported. Aliases like
                "latest" are not supported.
        """

        secret_version: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Widevine(proto.Message):
        r"""Widevine configuration."""

    class Fairplay(proto.Message):
        r"""Fairplay configuration."""

    class Playready(proto.Message):
        r"""Playready configuration."""

    class Clearkey(proto.Message):
        r"""Clearkey configuration."""

    class DrmSystems(proto.Message):
        r"""Defines configuration for DRM systems in use.

        Attributes:
            widevine (google.cloud.video.transcoder_v1.types.Encryption.Widevine):
                Widevine configuration.
            fairplay (google.cloud.video.transcoder_v1.types.Encryption.Fairplay):
                Fairplay configuration.
            playready (google.cloud.video.transcoder_v1.types.Encryption.Playready):
                Playready configuration.
            clearkey (google.cloud.video.transcoder_v1.types.Encryption.Clearkey):
                Clearkey configuration.
        """

        widevine: "Encryption.Widevine" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Encryption.Widevine",
        )
        fairplay: "Encryption.Fairplay" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Encryption.Fairplay",
        )
        playready: "Encryption.Playready" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Encryption.Playready",
        )
        clearkey: "Encryption.Clearkey" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Encryption.Clearkey",
        )

    id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    aes_128: Aes128Encryption = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="encryption_mode",
        message=Aes128Encryption,
    )
    sample_aes: SampleAesEncryption = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="encryption_mode",
        message=SampleAesEncryption,
    )
    mpeg_cenc: MpegCommonEncryption = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="encryption_mode",
        message=MpegCommonEncryption,
    )
    secret_manager_key_source: SecretManagerSource = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="secret_source",
        message=SecretManagerSource,
    )
    drm_systems: DrmSystems = proto.Field(
        proto.MESSAGE,
        number=8,
        message=DrmSystems,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
