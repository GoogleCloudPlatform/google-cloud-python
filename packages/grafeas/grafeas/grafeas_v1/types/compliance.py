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

from grafeas.grafeas_v1.types import severity as g_severity

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "ComplianceNote",
        "ComplianceVersion",
        "ComplianceOccurrence",
        "NonCompliantFile",
    },
)


class ComplianceNote(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        title (str):
            The title that identifies this compliance
            check.
        description (str):
            A description about this compliance check.
        version (MutableSequence[grafeas.grafeas_v1.types.ComplianceVersion]):
            The OS and config versions the benchmark
            applies to.
        rationale (str):
            A rationale for the existence of this
            compliance check.
        remediation (str):
            A description of remediation steps if the
            compliance check fails.
        cis_benchmark (grafeas.grafeas_v1.types.ComplianceNote.CisBenchmark):

            This field is a member of `oneof`_ ``compliance_type``.
        scan_instructions (bytes):
            Serialized scan instructions with a
            predefined format.
        impact (str):

            This field is a member of `oneof`_ ``potential_impact``.
    """

    class CisBenchmark(proto.Message):
        r"""A compliance check that is a CIS benchmark.

        Attributes:
            profile_level (int):

            severity (grafeas.grafeas_v1.types.Severity):

        """

        profile_level: int = proto.Field(
            proto.INT32,
            number=1,
        )
        severity: g_severity.Severity = proto.Field(
            proto.ENUM,
            number=2,
            enum=g_severity.Severity,
        )

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: MutableSequence["ComplianceVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ComplianceVersion",
    )
    rationale: str = proto.Field(
        proto.STRING,
        number=4,
    )
    remediation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cis_benchmark: CisBenchmark = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="compliance_type",
        message=CisBenchmark,
    )
    scan_instructions: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )
    impact: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="potential_impact",
    )


class ComplianceVersion(proto.Message):
    r"""Describes the CIS benchmark version that is applicable to a
    given OS and os version.

    Attributes:
        cpe_uri (str):
            The CPE URI
            (https://cpe.mitre.org/specification/) this
            benchmark is applicable to.
        benchmark_document (str):
            The name of the document that defines this
            benchmark, e.g. "CIS Container-Optimized OS".
        version (str):
            The version of the benchmark. This is set to
            the version of the OS-specific CIS document the
            benchmark is defined in.
    """

    cpe_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    benchmark_document: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ComplianceOccurrence(proto.Message):
    r"""An indication that the compliance checks in the associated
    ComplianceNote were not satisfied for particular resources or a
    specified reason.

    Attributes:
        non_compliant_files (MutableSequence[grafeas.grafeas_v1.types.NonCompliantFile]):

        non_compliance_reason (str):

        version (grafeas.grafeas_v1.types.ComplianceVersion):
            The OS and config version the benchmark was
            run on.
    """

    non_compliant_files: MutableSequence["NonCompliantFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="NonCompliantFile",
    )
    non_compliance_reason: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: "ComplianceVersion" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ComplianceVersion",
    )


class NonCompliantFile(proto.Message):
    r"""Details about files that caused a compliance check to fail.

    Attributes:
        path (str):
            Empty if ``display_command`` is set.
        display_command (str):
            Command to display the non-compliant files.
        reason (str):
            Explains why a file is non compliant for a
            CIS check.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_command: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
