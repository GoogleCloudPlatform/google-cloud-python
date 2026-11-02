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
        "DSSEAttestationNote",
        "DSSEAttestationOccurrence",
    },
)


class DSSEAttestationNote(proto.Message):
    r"""

    Attributes:
        hint (grafeas.grafeas_v1.types.DSSEAttestationNote.DSSEHint):
            DSSEHint hints at the purpose of the
            attestation authority.
    """

    class DSSEHint(proto.Message):
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
                attestation authority, for example
                "cloudbuild-prod".
        """

        human_readable_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    hint: DSSEHint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=DSSEHint,
    )


class DSSEAttestationOccurrence(proto.Message):
    r"""Deprecated. Prefer to use a regular Occurrence, and populate
    the Envelope at the top level of the Occurrence.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        envelope (grafeas.grafeas_v1.types.Envelope):
            If doing something security critical, make
            sure to verify the signatures in this metadata.
        statement (grafeas.grafeas_v1.types.InTotoStatement):

            This field is a member of `oneof`_ ``decoded_payload``.
    """

    envelope: common.Envelope = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.Envelope,
    )
    statement: intoto_statement.InTotoStatement = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="decoded_payload",
        message=intoto_statement.InTotoStatement,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
