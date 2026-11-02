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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "RunMode",
        "OperatorDefinition",
        "ResourceSpecification",
        "AttributeValue",
        "AnalyzerDefinition",
        "AnalysisDefinition",
        "RunStatus",
    },
)


class RunMode(proto.Enum):
    r"""RunMode represents the mode to launch the Process on.

    Values:
        RUN_MODE_UNSPECIFIED (0):
            Mode is unspecified.
        LIVE (1):
            Live mode. Meaning the Process is launched to
            handle live video source, and possible packet
            drops are expected.
        SUBMISSION (2):
            Submission mode. Meaning the Process is
            launched to handle bounded video files, with no
            packet drop. Completion status is tracked.
    """

    RUN_MODE_UNSPECIFIED = 0
    LIVE = 1
    SUBMISSION = 2


class OperatorDefinition(proto.Message):
    r"""Defines the interface of an Operator.

    Arguments to an operator are input/output streams that are
    getting processesed/returned while attributes are fixed
    configuration parameters.

    Attributes:
        operator (str):
            The name of this operator.

            Tentatively [A-Z][a-zA-Z0-9]\*, e.g., BboxCounter,
            PetDetector, PetDetector1.
        input_args (MutableSequence[google.cloud.visionai_v1.types.OperatorDefinition.ArgumentDefinition]):
            Declares input arguments.
        output_args (MutableSequence[google.cloud.visionai_v1.types.OperatorDefinition.ArgumentDefinition]):
            Declares output arguments.
        attributes (MutableSequence[google.cloud.visionai_v1.types.OperatorDefinition.AttributeDefinition]):
            Declares the attributes.
        resources (google.cloud.visionai_v1.types.ResourceSpecification):
            The resources for running the operator.
        short_description (str):
            Short description of the operator.
        description (str):
            Full description of the operator.
    """

    class ArgumentDefinition(proto.Message):
        r"""Defines an argument to an operator.

        Used for both inputs and outputs.

        Attributes:
            argument (str):
                The name of the argument.

                Tentatively `a-z <[_a-z0-9]*[a-z0-9]>`__?, e.g., video,
                audio, high_fps_frame.
            type_ (str):
                The data type of the argument.

                This should match the textual representation of
                a stream/Packet type.
        """

        argument: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AttributeDefinition(proto.Message):
        r"""Defines an attribute of an operator.

        Attributes:
            attribute (str):
                The name of the attribute.

                Tentatively `a-z <[_a-z0-9]*[a-z0-9]>`__?, e.g.,
                max_frames_per_video, resize_height.
            type_ (str):
                The type of this attribute.

                See attribute_value.proto for possibilities.
            default_value (google.cloud.visionai_v1.types.AttributeValue):
                The default value for the attribute.
        """

        attribute: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )
        default_value: "AttributeValue" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="AttributeValue",
        )

    operator: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_args: MutableSequence[ArgumentDefinition] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ArgumentDefinition,
    )
    output_args: MutableSequence[ArgumentDefinition] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ArgumentDefinition,
    )
    attributes: MutableSequence[AttributeDefinition] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=AttributeDefinition,
    )
    resources: "ResourceSpecification" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ResourceSpecification",
    )
    short_description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ResourceSpecification(proto.Message):
    r"""ResourceSpec collects a set of resources that can
    be used to specify requests and requirements.

    Note: Highly experimental as this can be runtime dependent. Can
    use the "extras" field to experiment first before trying to
    abstract it.

    Attributes:
        cpu (str):
            CPU specification.

            Examples: "100m", "0.5", "1", "2", ... correspond to 0.1,
            half, 1, or 2 cpus.

            Leave empty to let the system decide.

            Note that this does *not* determine the cpu vender/make, or
            its underlying clock speed and specific SIMD features. It is
            only the amount time it requires in timeslicing.
        cpu_limits (str):
            CPU limit.

            Examples:

            "100m", "0.5", "1", "2", ... correspond to
            0.1, half, 1, or 2 cpus.

            Leave empty to indicate no limit.
        memory (str):
            Memory specification (in bytes).

            Examples:

            "128974848", "129e6", "129M", "123Mi", ...
            correspond to 128974848 bytes, 129000000 bytes,
            129 mebibytes, 123 megabytes.

            Leave empty to let the system decide.
        memory_limits (str):
            Memory usage limits.

            Examples:

            "128974848", "129e6", "129M", "123Mi", ...
            correspond to 128974848 bytes, 129000000 bytes,
            129 mebibytes, 123 megabytes.

            Leave empty to indicate no limit.
        gpus (int):
            Number of gpus.
        latency_budget_ms (int):
            The maximum latency that this operator may
            use to process an element.
            If non positive, then a system default will be
            used. Operator developers should arrange for the
            system compute resources to be aligned with this
            latency budget; e.g. if you want a ML model to
            produce results within 500ms, then you should
            make sure you request enough cpu/gpu/memory to
            achieve that.
    """

    cpu: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cpu_limits: str = proto.Field(
        proto.STRING,
        number=5,
    )
    memory: str = proto.Field(
        proto.STRING,
        number=2,
    )
    memory_limits: str = proto.Field(
        proto.STRING,
        number=6,
    )
    gpus: int = proto.Field(
        proto.INT32,
        number=3,
    )
    latency_budget_ms: int = proto.Field(
        proto.INT32,
        number=4,
    )


class AttributeValue(proto.Message):
    r"""Represents an actual value of an operator attribute.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        i (int):
            int.

            This field is a member of `oneof`_ ``value``.
        f (float):
            float.

            This field is a member of `oneof`_ ``value``.
        b (bool):
            bool.

            This field is a member of `oneof`_ ``value``.
        s (bytes):
            string.

            This field is a member of `oneof`_ ``value``.
    """

    i: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="value",
    )
    f: float = proto.Field(
        proto.FLOAT,
        number=2,
        oneof="value",
    )
    b: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof="value",
    )
    s: bytes = proto.Field(
        proto.BYTES,
        number=4,
        oneof="value",
    )


class AnalyzerDefinition(proto.Message):
    r"""Defines an Analyzer.

    An analyzer processes data from its input streams using the
    logic defined in the Operator that it represents. Of course, it
    produces data for the output streams declared in the Operator.

    Attributes:
        analyzer (str):
            The name of this analyzer.

            Tentatively [a-z][a-z0-9]\ *(\_[a-z0-9]+)*.
        operator (str):
            The name of the operator that this analyzer
            runs.
            Must match the name of a supported operator.
        inputs (MutableSequence[google.cloud.visionai_v1.types.AnalyzerDefinition.StreamInput]):
            Input streams.
        attrs (MutableMapping[str, google.cloud.visionai_v1.types.AttributeValue]):
            The attribute values that this analyzer
            applies to the operator.
            Supply a mapping between the attribute names and
            the actual value you wish to apply. If an
            attribute name is omitted, then it will take a
            preconfigured default value.
        debug_options (google.cloud.visionai_v1.types.AnalyzerDefinition.DebugOptions):
            Debug options.
        operator_option (google.cloud.visionai_v1.types.AnalyzerDefinition.OperatorOption):
            Operator option.
    """

    class StreamInput(proto.Message):
        r"""The inputs to this analyzer.

        We accept input name references of the following form: :

        Example:

        Suppose you had an operator named "SomeOp" that has 2 output
        arguments, the first of which is named "foo" and the second of which
        is named "bar", and an operator named "MyOp" that accepts 2 inputs.

        Also suppose that there is an analyzer named "some-analyzer" that is
        running "SomeOp" and another analyzer named "my-analyzer" running
        "MyOp".

        To indicate that "my-analyzer" is to consume "some-analyzer"'s "foo"
        output as its first input and "some-analyzer"'s "bar" output as its
        second input, you can set this field to the following: input =
        ["some-analyzer:foo", "some-analyzer:bar"]

        Attributes:
            input (str):
                The name of the stream input (as discussed
                above).
        """

        input: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class DebugOptions(proto.Message):
        r"""Options available for debugging purposes only.

        Attributes:
            environment_variables (MutableMapping[str, str]):
                Environment variables.
        """

        environment_variables: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    class OperatorOption(proto.Message):
        r"""Option related to the operator.

        Attributes:
            tag (str):
                Tag of the operator.
            registry (str):
                Registry of the operator. e.g. public, dev.
        """

        tag: str = proto.Field(
            proto.STRING,
            number=1,
        )
        registry: str = proto.Field(
            proto.STRING,
            number=2,
        )

    analyzer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operator: str = proto.Field(
        proto.STRING,
        number=2,
    )
    inputs: MutableSequence[StreamInput] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=StreamInput,
    )
    attrs: MutableMapping[str, "AttributeValue"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message="AttributeValue",
    )
    debug_options: DebugOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        message=DebugOptions,
    )
    operator_option: OperatorOption = proto.Field(
        proto.MESSAGE,
        number=6,
        message=OperatorOption,
    )


class AnalysisDefinition(proto.Message):
    r"""Defines a full analysis.

    This is a description of the overall live analytics pipeline.
    You may think of this as an edge list representation of a
    multigraph.

    This may be directly authored by a human in protobuf textformat,
    or it may be generated by a programming API (perhaps Python or
    JavaScript depending on context).

    Attributes:
        analyzers (MutableSequence[google.cloud.visionai_v1.types.AnalyzerDefinition]):
            Analyzer definitions.
    """

    analyzers: MutableSequence["AnalyzerDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnalyzerDefinition",
    )


class RunStatus(proto.Message):
    r"""Message describing the status of the Process.

    Attributes:
        state (google.cloud.visionai_v1.types.RunStatus.State):
            The state of the Process.
        reason (str):
            The reason of becoming the state.
    """

    class State(proto.Enum):
        r"""State represents the running status of the Process.

        Values:
            STATE_UNSPECIFIED (0):
                State is unspecified.
            INITIALIZING (1):
                INITIALIZING means the Process is scheduled
                but yet ready to handle real traffic.
            RUNNING (2):
                RUNNING means the Process is up running and
                handling traffic.
            COMPLETED (3):
                COMPLETED means the Process has completed the
                processing, especially for non-streaming use
                case.
            FAILED (4):
                FAILED means the Process failed to complete
                the processing.
            PENDING (5):
                PENDING means the Process is created but yet
                to be scheduled.
        """

        STATE_UNSPECIFIED = 0
        INITIALIZING = 1
        RUNNING = 2
        COMPLETED = 3
        FAILED = 4
        PENDING = 5

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
