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

from grafeas.grafeas_v1.types import common, intoto_statement

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "SBOMReferenceNote",
        "SBOMReferenceOccurrence",
        "SbomReferenceIntotoPayload",
        "SbomReferenceIntotoPredicate",
    },
)


class SBOMReferenceNote(proto.Message):
    r"""The note representing an SBOM reference.

    Attributes:
        format_ (str):
            The format that SBOM takes. E.g. may be spdx,
            cyclonedx, etc...
        version (str):
            The version of the format that the SBOM
            takes. E.g. if the format is spdx, the version
            may be 2.3.
    """

    format_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SBOMReferenceOccurrence(proto.Message):
    r"""The occurrence representing an SBOM reference as applied to a
    specific resource. The occurrence follows the DSSE
    specification. See
    https://github.com/secure-systems-lab/dsse/blob/master/envelope.md
    for more details.

    Attributes:
        payload (grafeas.grafeas_v1.types.SbomReferenceIntotoPayload):
            The actual payload that contains the SBOM
            reference data.
        payload_type (str):
            The kind of payload that
            SbomReferenceIntotoPayload takes. Since it's in
            the intoto format, this value is expected to be
            'application/vnd.in-toto+json'.
        signatures (MutableSequence[grafeas.grafeas_v1.types.EnvelopeSignature]):
            The signatures over the payload.
    """

    payload: "SbomReferenceIntotoPayload" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SbomReferenceIntotoPayload",
    )
    payload_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    signatures: MutableSequence[common.EnvelopeSignature] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=common.EnvelopeSignature,
    )


class SbomReferenceIntotoPayload(proto.Message):
    r"""The actual payload that contains the SBOM Reference data.
    The payload follows the intoto statement specification. See
    https://github.com/in-toto/attestation/blob/main/spec/v1.0/statement.md
    for more details.

    Attributes:
        type_ (str):
            Identifier for the schema of the Statement.
        predicate_type (str):
            URI identifying the type of the Predicate.
        subject (MutableSequence[grafeas.grafeas_v1.types.Subject]):
            Set of software artifacts that the
            attestation applies to. Each element represents
            a single software artifact.
        predicate (grafeas.grafeas_v1.types.SbomReferenceIntotoPredicate):
            Additional parameters of the Predicate.
            Includes the actual data about the SBOM.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    predicate_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subject: MutableSequence[intoto_statement.Subject] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=intoto_statement.Subject,
    )
    predicate: "SbomReferenceIntotoPredicate" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SbomReferenceIntotoPredicate",
    )


class SbomReferenceIntotoPredicate(proto.Message):
    r"""A predicate which describes the SBOM being referenced.

    Attributes:
        referrer_id (str):
            The person or system referring this predicate
            to the consumer.
        location (str):
            The location of the SBOM.
        mime_type (str):
            The mime type of the SBOM.
        digest (MutableMapping[str, str]):
            A map of algorithm to digest of the contents
            of the SBOM.
    """

    referrer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    digest: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
