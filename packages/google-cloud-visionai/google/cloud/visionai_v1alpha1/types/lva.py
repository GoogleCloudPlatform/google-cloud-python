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
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "AttributeValue",
        "AnalyzerDefinition",
        "AnalysisDefinition",
    },
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
        inputs (MutableSequence[google.cloud.visionai_v1alpha1.types.AnalyzerDefinition.StreamInput]):
            Input streams.
        attrs (MutableMapping[str, google.cloud.visionai_v1alpha1.types.AttributeValue]):
            The attribute values that this analyzer
            applies to the operator.
            Supply a mapping between the attribute names and
            the actual value you wish to apply. If an
            attribute name is omitted, then it will take a
            preconfigured default value.
        debug_options (google.cloud.visionai_v1alpha1.types.AnalyzerDefinition.DebugOptions):
            Debug options.
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


class AnalysisDefinition(proto.Message):
    r"""Defines a full analysis.

    This is a description of the overall live analytics pipeline.
    You may think of this as an edge list representation of a
    multigraph.

    This may be directly authored by a human in protobuf textformat,
    or it may be generated by a programming API (perhaps Python or
    JavaScript depending on context).

    Attributes:
        analyzers (MutableSequence[google.cloud.visionai_v1alpha1.types.AnalyzerDefinition]):
            Analyzer definitions.
    """

    analyzers: MutableSequence["AnalyzerDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnalyzerDefinition",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
