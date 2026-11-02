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

from grafeas.grafeas_v1.types import intoto_provenance
from grafeas.grafeas_v1.types import slsa_provenance as g_slsa_provenance
from grafeas.grafeas_v1.types import (
    slsa_provenance_zero_two as g_slsa_provenance_zero_two,
)

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "InTotoStatement",
        "Subject",
        "InTotoSlsaProvenanceV1",
    },
)


class InTotoStatement(proto.Message):
    r"""Spec defined at
    https://github.com/in-toto/attestation/tree/main/spec#statement
    The serialized InTotoStatement will be stored as
    Envelope.payload. Envelope.payloadType is always
    "application/vnd.in-toto+json".

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (str):
            Always ``https://in-toto.io/Statement/v0.1``.
        subject (MutableSequence[grafeas.grafeas_v1.types.Subject]):

        predicate_type (str):
            ``https://slsa.dev/provenance/v0.1`` for SlsaProvenance.
        provenance (grafeas.grafeas_v1.types.InTotoProvenance):

            This field is a member of `oneof`_ ``predicate``.
        slsa_provenance (grafeas.grafeas_v1.types.SlsaProvenance):

            This field is a member of `oneof`_ ``predicate``.
        slsa_provenance_zero_two (grafeas.grafeas_v1.types.SlsaProvenanceZeroTwo):

            This field is a member of `oneof`_ ``predicate``.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: MutableSequence["Subject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Subject",
    )
    predicate_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    provenance: intoto_provenance.InTotoProvenance = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="predicate",
        message=intoto_provenance.InTotoProvenance,
    )
    slsa_provenance: g_slsa_provenance.SlsaProvenance = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="predicate",
        message=g_slsa_provenance.SlsaProvenance,
    )
    slsa_provenance_zero_two: g_slsa_provenance_zero_two.SlsaProvenanceZeroTwo = (
        proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="predicate",
            message=g_slsa_provenance_zero_two.SlsaProvenanceZeroTwo,
        )
    )


class Subject(proto.Message):
    r"""

    Attributes:
        name (str):

        digest (MutableMapping[str, str]):
            ``"<ALGORITHM>": "<HEX_VALUE>"`` Algorithms can be e.g.
            sha256, sha512 See
            https://github.com/in-toto/attestation/blob/main/spec/field_types.md#DigestSet
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    digest: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class InTotoSlsaProvenanceV1(proto.Message):
    r"""

    Attributes:
        type_ (str):
            InToto spec defined at
            https://github.com/in-toto/attestation/tree/main/spec#statement
        subject (MutableSequence[grafeas.grafeas_v1.types.Subject]):

        predicate_type (str):

        predicate (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.SlsaProvenanceV1):

    """

    class SlsaProvenanceV1(proto.Message):
        r"""Keep in sync with schema at
        https://github.com/slsa-framework/slsa/blob/main/docs/provenance/schema/v1/provenance.proto
        Builder renamed to ProvenanceBuilder because of Java conflicts.

        Attributes:
            build_definition (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.BuildDefinition):

            run_details (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.RunDetails):

        """

        build_definition: "InTotoSlsaProvenanceV1.BuildDefinition" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="InTotoSlsaProvenanceV1.BuildDefinition",
        )
        run_details: "InTotoSlsaProvenanceV1.RunDetails" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="InTotoSlsaProvenanceV1.RunDetails",
        )

    class BuildDefinition(proto.Message):
        r"""

        Attributes:
            build_type (str):

            external_parameters (google.protobuf.struct_pb2.Struct):

            internal_parameters (google.protobuf.struct_pb2.Struct):

            resolved_dependencies (MutableSequence[grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.ResourceDescriptor]):

        """

        build_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        external_parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )
        internal_parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Struct,
        )
        resolved_dependencies: MutableSequence[
            "InTotoSlsaProvenanceV1.ResourceDescriptor"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="InTotoSlsaProvenanceV1.ResourceDescriptor",
        )

    class ResourceDescriptor(proto.Message):
        r"""

        Attributes:
            name (str):

            uri (str):

            digest (MutableMapping[str, str]):

            content (bytes):

            download_location (str):

            media_type (str):

            annotations (MutableMapping[str, google.protobuf.struct_pb2.Value]):

        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        digest: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=3,
        )
        content: bytes = proto.Field(
            proto.BYTES,
            number=4,
        )
        download_location: str = proto.Field(
            proto.STRING,
            number=5,
        )
        media_type: str = proto.Field(
            proto.STRING,
            number=6,
        )
        annotations: MutableMapping[str, struct_pb2.Value] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=7,
            message=struct_pb2.Value,
        )

    class RunDetails(proto.Message):
        r"""

        Attributes:
            builder (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.ProvenanceBuilder):

            metadata (grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.BuildMetadata):

            byproducts (MutableSequence[grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.ResourceDescriptor]):

        """

        builder: "InTotoSlsaProvenanceV1.ProvenanceBuilder" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="InTotoSlsaProvenanceV1.ProvenanceBuilder",
        )
        metadata: "InTotoSlsaProvenanceV1.BuildMetadata" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="InTotoSlsaProvenanceV1.BuildMetadata",
        )
        byproducts: MutableSequence["InTotoSlsaProvenanceV1.ResourceDescriptor"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="InTotoSlsaProvenanceV1.ResourceDescriptor",
            )
        )

    class ProvenanceBuilder(proto.Message):
        r"""

        Attributes:
            id (str):

            version (MutableMapping[str, str]):

            builder_dependencies (MutableSequence[grafeas.grafeas_v1.types.InTotoSlsaProvenanceV1.ResourceDescriptor]):

        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        version: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        builder_dependencies: MutableSequence[
            "InTotoSlsaProvenanceV1.ResourceDescriptor"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="InTotoSlsaProvenanceV1.ResourceDescriptor",
        )

    class BuildMetadata(proto.Message):
        r"""

        Attributes:
            invocation_id (str):

            started_on (google.protobuf.timestamp_pb2.Timestamp):

            finished_on (google.protobuf.timestamp_pb2.Timestamp):

        """

        invocation_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        started_on: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        finished_on: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: MutableSequence["Subject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Subject",
    )
    predicate_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    predicate: SlsaProvenanceV1 = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SlsaProvenanceV1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
