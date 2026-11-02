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

from grafeas.grafeas_v1.types import common

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "AttestationNote",
        "Jwt",
        "AttestationOccurrence",
    },
)


class AttestationNote(proto.Message):
    r"""Note kind that represents a logical attestation "role" or
    "authority". For example, an organization might have one
    ``Authority`` for "QA" and one for "build". This note is intended to
    act strictly as a grouping mechanism for the attached occurrences
    (Attestations). This grouping mechanism also provides a security
    boundary, since IAM ACLs gate the ability for a principle to attach
    an occurrence to a given note. It also provides a single point of
    lookup to find all attached attestation occurrences, even if they
    don't all live in the same project.

    Attributes:
        hint (grafeas.grafeas_v1.types.AttestationNote.Hint):
            Hint hints at the purpose of the attestation
            authority.
    """

    class Hint(proto.Message):
        r"""This submessage provides human-readable hints about the
        purpose of the authority. Because the name of a note acts as its
        resource reference, it is important to disambiguate the
        canonical name of the Note (which might be a UUID for security
        purposes) from "readable" names more suitable for debug output.
        Note that these hints should not be used to look up authorities
        in security sensitive contexts, such as when looking up
        attestations to verify.

        Attributes:
            human_readable_name (str):
                Required. The human readable name of this
                attestation authority, for example "qa".
        """

        human_readable_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    hint: Hint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Hint,
    )


class Jwt(proto.Message):
    r"""

    Attributes:
        compact_jwt (str):
            The compact encoding of a JWS, which is
            always three base64 encoded strings joined by
            periods. For details, see:

            https://tools.ietf.org/html/rfc7515.html#section-3.1
    """

    compact_jwt: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AttestationOccurrence(proto.Message):
    r"""Occurrence that represents a single "attestation". The
    authenticity of an attestation can be verified using the
    attached signature. If the verifier trusts the public key of the
    signer, then verifying the signature is sufficient to establish
    trust. In this circumstance, the authority to which this
    attestation is attached is primarily useful for lookup (how to
    find this attestation if you already know the authority and
    artifact to be verified) and intent (for which authority this
    attestation was intended to sign.

    Attributes:
        serialized_payload (bytes):
            Required. The serialized payload that is verified by one or
            more ``signatures``.
        signatures (MutableSequence[grafeas.grafeas_v1.types.Signature]):
            One or more signatures over ``serialized_payload``. Verifier
            implementations should consider this attestation message
            verified if at least one ``signature`` verifies
            ``serialized_payload``. See ``Signature`` in common.proto
            for more details on signature structure and verification.
        jwts (MutableSequence[grafeas.grafeas_v1.types.Jwt]):
            One or more JWTs encoding a self-contained attestation. Each
            JWT encodes the payload that it verifies within the JWT
            itself. Verifier implementation SHOULD ignore the
            ``serialized_payload`` field when verifying these JWTs. If
            only JWTs are present on this AttestationOccurrence, then
            the ``serialized_payload`` SHOULD be left empty. Each JWT
            SHOULD encode a claim specific to the ``resource_uri`` of
            this Occurrence, but this is not validated by Grafeas
            metadata API implementations. The JWT itself is opaque to
            Grafeas.
    """

    serialized_payload: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    signatures: MutableSequence[common.Signature] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=common.Signature,
    )
    jwts: MutableSequence["Jwt"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Jwt",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
