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
        "VulnerabilityAssessmentNote",
    },
)


class VulnerabilityAssessmentNote(proto.Message):
    r"""A single VulnerabilityAssessmentNote represents
    one particular product's vulnerability assessment for one CVE.

    Attributes:
        title (str):
            The title of the note. E.g. ``Vex-Debian-11.4``
        short_description (str):
            A one sentence description of this Vex.
        long_description (str):
            A detailed description of this Vex.
        language_code (str):
            Identifies the language used by this
            document, corresponding to IETF BCP 47 / RFC
            5646.
        publisher (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Publisher):
            Publisher details of this Note.
        product (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Product):
            The product affected by this vex.
        assessment (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment):
            Represents a vulnerability assessment for the
            product.
    """

    class Publisher(proto.Message):
        r"""Publisher contains information about the publisher of
        this Note.
        (-- api-linter: core::0123::resource-annotation=disabled
        aip.dev/not-precedent: Publisher is not a separate resource. --)

        Attributes:
            name (str):
                Name of the publisher.
                Examples: 'Google', 'Google Cloud Platform'.
            issuing_authority (str):
                Provides information about the authority of
                the issuing party to release the document, in
                particular, the party's constituency and
                responsibilities or other obligations.
            publisher_namespace (str):
                The context or namespace.
                Contains a URL which is under control of the
                issuing party and can be used as a globally
                unique identifier for that issuing party.
                Example: https://csaf.io
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        issuing_authority: str = proto.Field(
            proto.STRING,
            number=2,
        )
        publisher_namespace: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Product(proto.Message):
        r"""Product contains information about a product and how to
        uniquely identify it.
        (-- api-linter: core::0123::resource-annotation=disabled
        aip.dev/not-precedent: Product is not a separate resource. --)


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            name (str):
                Name of the product.
            id (str):
                Token that identifies a product so that it
                can be referred to from other parts in the
                document. There is no predefined format as long
                as it uniquely identifies a group in the context
                of the current document.
            generic_uri (str):
                Contains a URI which is vendor-specific.
                Example: The artifact repository URL of an
                image.

                This field is a member of `oneof`_ ``identifier``.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        generic_uri: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="identifier",
        )

    class Assessment(proto.Message):
        r"""Assessment provides all information that is related to a
        single vulnerability for this product.

        Attributes:
            cve (str):
                Holds the MITRE standard Common Vulnerabilities and
                Exposures (CVE) tracking number for the vulnerability.
                Deprecated: Use vulnerability_id instead to denote CVEs.
            vulnerability_id (str):
                The vulnerability identifier for this
                Assessment. Will hold one of common identifiers
                e.g. CVE, GHSA etc.
            short_description (str):
                A one sentence description of this Vex.
            long_description (str):
                A detailed description of this Vex.
            related_uris (MutableSequence[grafeas.grafeas_v1.types.RelatedUrl]):
                Holds a list of references associated with
                this vulnerability item and assessment. These
                uris have additional information about the
                vulnerability and the assessment itself. E.g.
                Link to a document which details how this
                assessment concluded the state of this
                vulnerability.
            state (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment.State):
                Provides the state of this Vulnerability
                assessment.
            impacts (MutableSequence[str]):
                Contains information about the impact of this
                vulnerability, this will change with time.
            justification (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment.Justification):
                Justification provides the justification when the state of
                the assessment if NOT_AFFECTED.
            remediations (MutableSequence[grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment.Remediation]):
                Specifies details on how to handle (and
                presumably, fix) a vulnerability.
        """

        class State(proto.Enum):
            r"""Provides the state of this Vulnerability assessment.

            Values:
                STATE_UNSPECIFIED (0):
                    No state is specified.
                AFFECTED (1):
                    This product is known to be affected by this
                    vulnerability.
                NOT_AFFECTED (2):
                    This product is known to be not affected by
                    this vulnerability.
                FIXED (3):
                    This product contains a fix for this
                    vulnerability.
                UNDER_INVESTIGATION (4):
                    It is not known yet whether these versions
                    are or are not affected by the vulnerability.
                    However, it is still under investigation.
            """

            STATE_UNSPECIFIED = 0
            AFFECTED = 1
            NOT_AFFECTED = 2
            FIXED = 3
            UNDER_INVESTIGATION = 4

        class Justification(proto.Message):
            r"""Justification provides the justification when the state of the
            assessment if NOT_AFFECTED.

            Attributes:
                justification_type (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment.Justification.JustificationType):
                    The justification type for this
                    vulnerability.
                details (str):
                    Additional details on why this justification
                    was chosen.
            """

            class JustificationType(proto.Enum):
                r"""Provides the type of justification.

                Values:
                    JUSTIFICATION_TYPE_UNSPECIFIED (0):
                        JUSTIFICATION_TYPE_UNSPECIFIED.
                    COMPONENT_NOT_PRESENT (1):
                        The vulnerable component is not present in
                        the product.
                    VULNERABLE_CODE_NOT_PRESENT (2):
                        The vulnerable code is not present. Typically
                        this case occurs when source code is configured
                        or built in a way that excludes the vulnerable
                        code.
                    VULNERABLE_CODE_NOT_IN_EXECUTE_PATH (3):
                        The vulnerable code can not be executed.
                        Typically this case occurs when the product
                        includes the vulnerable code but does not call
                        or use the vulnerable code.
                    VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY (4):
                        The vulnerable code cannot be controlled by
                        an attacker to exploit the vulnerability.
                    INLINE_MITIGATIONS_ALREADY_EXIST (5):
                        The product includes built-in protections or
                        features that prevent exploitation of the
                        vulnerability. These built-in protections cannot
                        be subverted by the attacker and cannot be
                        configured or disabled by the user. These
                        mitigations completely prevent exploitation
                        based on known attack vectors.
                """

                JUSTIFICATION_TYPE_UNSPECIFIED = 0
                COMPONENT_NOT_PRESENT = 1
                VULNERABLE_CODE_NOT_PRESENT = 2
                VULNERABLE_CODE_NOT_IN_EXECUTE_PATH = 3
                VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY = 4
                INLINE_MITIGATIONS_ALREADY_EXIST = 5

            justification_type: "VulnerabilityAssessmentNote.Assessment.Justification.JustificationType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="VulnerabilityAssessmentNote.Assessment.Justification.JustificationType",
            )
            details: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class Remediation(proto.Message):
            r"""Specifies details on how to handle (and presumably, fix) a
            vulnerability.

            Attributes:
                remediation_type (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote.Assessment.Remediation.RemediationType):
                    The type of remediation that can be applied.
                details (str):
                    Contains a comprehensive human-readable
                    discussion of the remediation.
                remediation_uri (grafeas.grafeas_v1.types.RelatedUrl):
                    Contains the URL where to obtain the
                    remediation.
            """

            class RemediationType(proto.Enum):
                r"""The type of remediation that can be applied.

                Values:
                    REMEDIATION_TYPE_UNSPECIFIED (0):
                        No remediation type specified.
                    MITIGATION (1):
                        A MITIGATION is available.
                    NO_FIX_PLANNED (2):
                        No fix is planned.
                    NONE_AVAILABLE (3):
                        Not available.
                    VENDOR_FIX (4):
                        A vendor fix is available.
                    WORKAROUND (5):
                        A workaround is available.
                """

                REMEDIATION_TYPE_UNSPECIFIED = 0
                MITIGATION = 1
                NO_FIX_PLANNED = 2
                NONE_AVAILABLE = 3
                VENDOR_FIX = 4
                WORKAROUND = 5

            remediation_type: "VulnerabilityAssessmentNote.Assessment.Remediation.RemediationType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="VulnerabilityAssessmentNote.Assessment.Remediation.RemediationType",
            )
            details: str = proto.Field(
                proto.STRING,
                number=2,
            )
            remediation_uri: common.RelatedUrl = proto.Field(
                proto.MESSAGE,
                number=3,
                message=common.RelatedUrl,
            )

        cve: str = proto.Field(
            proto.STRING,
            number=1,
        )
        vulnerability_id: str = proto.Field(
            proto.STRING,
            number=9,
        )
        short_description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        long_description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        related_uris: MutableSequence[common.RelatedUrl] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=common.RelatedUrl,
        )
        state: "VulnerabilityAssessmentNote.Assessment.State" = proto.Field(
            proto.ENUM,
            number=5,
            enum="VulnerabilityAssessmentNote.Assessment.State",
        )
        impacts: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=6,
        )
        justification: "VulnerabilityAssessmentNote.Assessment.Justification" = (
            proto.Field(
                proto.MESSAGE,
                number=7,
                message="VulnerabilityAssessmentNote.Assessment.Justification",
            )
        )
        remediations: MutableSequence[
            "VulnerabilityAssessmentNote.Assessment.Remediation"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="VulnerabilityAssessmentNote.Assessment.Remediation",
        )

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    short_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    long_description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    publisher: Publisher = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Publisher,
    )
    product: Product = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Product,
    )
    assessment: Assessment = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Assessment,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
