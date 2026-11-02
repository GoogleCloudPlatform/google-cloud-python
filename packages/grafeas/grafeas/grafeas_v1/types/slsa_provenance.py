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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "SlsaProvenance",
    },
)


class SlsaProvenance(proto.Message):
    r"""

    Attributes:
        builder (grafeas.grafeas_v1.types.SlsaProvenance.SlsaBuilder):
            required
        recipe (grafeas.grafeas_v1.types.SlsaProvenance.SlsaRecipe):
            Identifies the configuration used for the
            build. When combined with materials, this SHOULD
            fully describe the build, such that re-running
            this recipe results in bit-for-bit identical
            output (if the build is reproducible).
        metadata (grafeas.grafeas_v1.types.SlsaProvenance.SlsaMetadata):

        materials (MutableSequence[grafeas.grafeas_v1.types.SlsaProvenance.Material]):
            The collection of artifacts that influenced
            the build including sources, dependencies, build
            tools, base images, and so on. This is
            considered to be incomplete unless
            metadata.completeness.materials is true. Unset
            or null is equivalent to empty.
    """

    class SlsaRecipe(proto.Message):
        r"""Steps taken to build the artifact.
        For a TaskRun, typically each container corresponds to one step
        in the recipe.

        Attributes:
            type_ (str):
                URI indicating what type of recipe was
                performed. It determines the meaning of
                recipe.entryPoint, recipe.arguments,
                recipe.environment, and materials.
            defined_in_material (int):
                Index in materials containing the recipe
                steps that are not implied by recipe.type. For
                example, if the recipe type were "make", then
                this would point to the source containing the
                Makefile, not the make program itself. Set to -1
                if the recipe doesn't come from a material, as
                zero is default unset value for int64.
            entry_point (str):
                String identifying the entry point into the
                build. This is often a path to a configuration
                file and/or a target label within that file. The
                syntax and meaning are defined by recipe.type.
                For example, if the recipe type were "make",
                then this would reference the directory in which
                to run make as well as which target to use.
            arguments (google.protobuf.any_pb2.Any):
                Collection of all external inputs that
                influenced the build on top of
                recipe.definedInMaterial and recipe.entryPoint.
                For example, if the recipe type were "make",
                then this might be the flags passed to make
                aside from the target, which is captured in
                recipe.entryPoint. Depending on the recipe Type,
                the structure may be different.
            environment (google.protobuf.any_pb2.Any):
                Any other builder-controlled inputs necessary
                for correctly evaluating the recipe. Usually
                only needed for reproducing the build but not
                evaluated as part of policy. Depending on the
                recipe Type, the structure may be different.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        defined_in_material: int = proto.Field(
            proto.INT64,
            number=2,
        )
        entry_point: str = proto.Field(
            proto.STRING,
            number=3,
        )
        arguments: any_pb2.Any = proto.Field(
            proto.MESSAGE,
            number=4,
            message=any_pb2.Any,
        )
        environment: any_pb2.Any = proto.Field(
            proto.MESSAGE,
            number=5,
            message=any_pb2.Any,
        )

    class SlsaCompleteness(proto.Message):
        r"""Indicates that the builder claims certain fields in this
        message to be complete.

        Attributes:
            arguments (bool):
                If true, the builder claims that
                recipe.arguments is complete, meaning that all
                external inputs are properly captured in the
                recipe.
            environment (bool):
                If true, the builder claims that
                recipe.environment is claimed to be complete.
            materials (bool):
                If true, the builder claims that materials
                are complete, usually through some controls to
                prevent network access. Sometimes called
                "hermetic".
        """

        arguments: bool = proto.Field(
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

    class SlsaMetadata(proto.Message):
        r"""Other properties of the build.

        Attributes:
            build_invocation_id (str):
                Identifies the particular build invocation,
                which can be useful for finding associated logs
                or other ad-hoc analysis. The value SHOULD be
                globally unique, per in-toto Provenance spec.
            build_started_on (google.protobuf.timestamp_pb2.Timestamp):
                The timestamp of when the build started.
            build_finished_on (google.protobuf.timestamp_pb2.Timestamp):
                The timestamp of when the build completed.
            completeness (grafeas.grafeas_v1.types.SlsaProvenance.SlsaCompleteness):
                Indicates that the builder claims certain
                fields in this message to be complete.
            reproducible (bool):
                If true, the builder claims that running the
                recipe on materials will produce bit-for-bit
                identical output.
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
        completeness: "SlsaProvenance.SlsaCompleteness" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="SlsaProvenance.SlsaCompleteness",
        )
        reproducible: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class SlsaBuilder(proto.Message):
        r"""

        Attributes:
            id (str):

        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Material(proto.Message):
        r"""

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

    builder: SlsaBuilder = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SlsaBuilder,
    )
    recipe: SlsaRecipe = proto.Field(
        proto.MESSAGE,
        number=2,
        message=SlsaRecipe,
    )
    metadata: SlsaMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SlsaMetadata,
    )
    materials: MutableSequence[Material] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Material,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
