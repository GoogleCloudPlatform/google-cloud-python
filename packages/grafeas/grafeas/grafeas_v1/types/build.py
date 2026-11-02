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

from grafeas.grafeas_v1.types import intoto_provenance as g_intoto_provenance
from grafeas.grafeas_v1.types import intoto_statement as g_intoto_statement
from grafeas.grafeas_v1.types import provenance as g_provenance

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "BuildNote",
        "BuildOccurrence",
    },
)


class BuildNote(proto.Message):
    r"""Note holding the version of the provider's builder and the
    signature of the provenance message in the build details
    occurrence.

    Attributes:
        builder_version (str):
            Required. Immutable. Version of the builder
            which produced this build.
    """

    builder_version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BuildOccurrence(proto.Message):
    r"""Details of a build occurrence.

    Attributes:
        provenance (grafeas.grafeas_v1.types.BuildProvenance):
            The actual provenance for the build.
        provenance_bytes (str):
            Serialized JSON representation of the provenance, used in
            generating the build signature in the corresponding build
            note. After verifying the signature, ``provenance_bytes``
            can be unmarshalled and compared to the provenance to
            confirm that it is unchanged. A base64-encoded string
            representation of the provenance bytes is used for the
            signature in order to interoperate with openssl which
            expects this format for signature verification.

            The serialized form is captured both to avoid ambiguity in
            how the provenance is marshalled to json as well to prevent
            incompatibilities with future changes.
        intoto_provenance (grafeas.grafeas_v1.types.InTotoProvenance):
            Deprecated. See InTotoStatement for the
            replacement. In-toto Provenance representation
            as defined in spec.
        intoto_statement (grafeas.grafeas_v1.types.InTotoStatement):
            In-toto Statement representation as defined in spec. The
            intoto_statement can contain any type of provenance. The
            serialized payload of the statement can be stored and signed
            in the Occurrence's envelope.
        in_toto_slsa_provenance_v1 (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1):
            In-Toto Slsa Provenance V1 represents a slsa
            provenance meeting the slsa spec, wrapped in an
            in-toto statement. This allows for direct
            jsonification of a to-spec in-toto slsa
            statement with a to-spec slsa provenance.
    """

    provenance: g_provenance.BuildProvenance = proto.Field(
        proto.MESSAGE,
        number=1,
        message=g_provenance.BuildProvenance,
    )
    provenance_bytes: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intoto_provenance: g_intoto_provenance.InTotoProvenance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=g_intoto_provenance.InTotoProvenance,
    )
    intoto_statement: g_intoto_statement.InTotoStatement = proto.Field(
        proto.MESSAGE,
        number=4,
        message=g_intoto_statement.InTotoStatement,
    )
    in_toto_slsa_provenance_v1: g_intoto_statement.InTotoSlsaProvenanceV1 = proto.Field(
        proto.MESSAGE,
        number=5,
        message=g_intoto_statement.InTotoSlsaProvenanceV1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
