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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "SlsaProvenanceZeroTwo",
    },
)


class SlsaProvenanceZeroTwo(proto.Message):
    r"""See full explanation of fields at slsa.dev/provenance/v0.2.

    Attributes:
        builder (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaBuilder):

        build_type (str):

        invocation (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaInvocation):

        build_config (google.protobuf.struct_pb2.Struct):

        metadata (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaMetadata):

        materials (MutableSequence[grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaMaterial]):

    """

    class SlsaBuilder(proto.Message):
        r"""Identifies the entity that executed the recipe, which is
        trusted to have correctly performed the operation and populated
        this provenance.

        Attributes:
            id (str):

        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SlsaMaterial(proto.Message):
        r"""The collection of artifacts that influenced the build
        including sources, dependencies, build tools, base images, and
        so on.

        Attributes:
            uri (str):

            digest (MutableMapping[str, str]):

        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        digest: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )

    class SlsaInvocation(proto.Message):
        r"""Identifies the event that kicked off the build.

        Attributes:
            config_source (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaConfigSource):

            parameters (google.protobuf.struct_pb2.Struct):

            environment (google.protobuf.struct_pb2.Struct):

        """

        config_source: "SlsaProvenanceZeroTwo.SlsaConfigSource" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="SlsaProvenanceZeroTwo.SlsaConfigSource",
        )
        parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )
        environment: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Struct,
        )

    class SlsaConfigSource(proto.Message):
        r"""Describes where the config file that kicked off the build
        came from. This is effectively a pointer to the source where
        buildConfig came from.

        Attributes:
            uri (str):

            digest (MutableMapping[str, str]):

            entry_point (str):

        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        digest: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        entry_point: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SlsaMetadata(proto.Message):
        r"""Other properties of the build.

        Attributes:
            build_invocation_id (str):

            build_started_on (google.protobuf.timestamp_pb2.Timestamp):

            build_finished_on (google.protobuf.timestamp_pb2.Timestamp):

            completeness (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo.SlsaCompleteness):

            reproducible (bool):

        """

        build_invocation_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        build_started_on: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        build_finished_on: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        completeness: "SlsaProvenanceZeroTwo.SlsaCompleteness" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="SlsaProvenanceZeroTwo.SlsaCompleteness",
        )
        reproducible: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class SlsaCompleteness(proto.Message):
        r"""Indicates that the builder claims certain fields in this
        message to be complete.

        Attributes:
            parameters (bool):

            environment (bool):

            materials (bool):

        """

        parameters: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        environment: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        materials: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    builder: SlsaBuilder = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SlsaBuilder,
    )
    build_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    invocation: SlsaInvocation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SlsaInvocation,
    )
    build_config: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    metadata: SlsaMetadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SlsaMetadata,
    )
    materials: MutableSequence[SlsaMaterial] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=SlsaMaterial,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
