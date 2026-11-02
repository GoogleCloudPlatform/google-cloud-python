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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from grafeas.grafeas_v1.types import common

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "DiscoveryNote",
        "DiscoveryOccurrence",
    },
)


class DiscoveryNote(proto.Message):
    r"""A note that indicates a type of analysis a provider would perform.
    This note exists in a provider's project. A ``Discovery`` occurrence
    is created in a consumer's project at the start of analysis.

    Attributes:
        analysis_kind (grafeas.grafeas_v1.types.NoteKind):
            Required. Immutable. The kind of analysis
            that is handled by this discovery.
    """

    analysis_kind: common.NoteKind = proto.Field(
        proto.ENUM,
        number=1,
        enum=common.NoteKind,
    )


class DiscoveryOccurrence(proto.Message):
    r"""Provides information about the analysis status of a
    discovered resource.

    Attributes:
        continuous_analysis (grafeas.grafeas_v1.types.DiscoveryOccurrence.ContinuousAnalysis):
            Whether the resource is continuously
            analyzed.
        analysis_status (grafeas.grafeas_v1.types.DiscoveryOccurrence.AnalysisStatus):
            The status of discovery for the resource.
        analysis_completed (grafeas.grafeas_v1.types.DiscoveryOccurrence.AnalysisCompleted):

        analysis_error (MutableSequence[google.rpc.status_pb2.Status]):
            Indicates any errors encountered during
            analysis of a resource. There could be 0 or more
            of these errors.
        analysis_status_error (google.rpc.status_pb2.Status):
            When an error is encountered this will
            contain a LocalizedMessage under details to show
            to the user. The LocalizedMessage is output only
            and populated by the API.
        cpe (str):
            The CPE of the resource being scanned.
        last_scan_time (google.protobuf.timestamp_pb2.Timestamp):
            The last time this resource was scanned.
        archive_time (google.protobuf.timestamp_pb2.Timestamp):
            The time occurrences related to this
            discovery occurrence were archived.
        sbom_status (grafeas.grafeas_v1.types.DiscoveryOccurrence.SBOMStatus):
            The status of an SBOM generation.
        vulnerability_attestation (grafeas.grafeas_v1.types.DiscoveryOccurrence.VulnerabilityAttestation):
            The status of an vulnerability attestation
            generation.
        files (MutableSequence[grafeas.grafeas_v1.types.DiscoveryOccurrence.File]):
            Files that make up the resource described by
            the occurrence.
        last_vulnerability_update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last time vulnerability scan results
            changed.
    """

    class ContinuousAnalysis(proto.Enum):
        r"""Whether the resource is continuously analyzed.

        Values:
            CONTINUOUS_ANALYSIS_UNSPECIFIED (0):
                Unknown.
            ACTIVE (1):
                The resource is continuously analyzed.
            INACTIVE (2):
                The resource is ignored for continuous
                analysis.
        """

        CONTINUOUS_ANALYSIS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2

    class AnalysisStatus(proto.Enum):
        r"""Analysis status for a resource. Currently for initial
        analysis only (not updated in continuous analysis).

        Values:
            ANALYSIS_STATUS_UNSPECIFIED (0):
                Unknown.
            PENDING (1):
                Resource is known but no action has been
                taken yet.
            SCANNING (2):
                Resource is being analyzed.
            FINISHED_SUCCESS (3):
                Analysis has finished successfully.
            COMPLETE (3):
                Analysis has completed.
            FINISHED_FAILED (4):
                Analysis has finished unsuccessfully, the
                analysis itself is in a bad state.
            FINISHED_UNSUPPORTED (5):
                The resource is known not to be supported.
        """

        _pb_options = {"allow_alias": True}
        ANALYSIS_STATUS_UNSPECIFIED = 0
        PENDING = 1
        SCANNING = 2
        FINISHED_SUCCESS = 3
        COMPLETE = 3
        FINISHED_FAILED = 4
        FINISHED_UNSUPPORTED = 5

    class AnalysisCompleted(proto.Message):
        r"""Indicates which analysis completed successfully. Multiple
        types of analysis can be performed on a single resource.

        Attributes:
            analysis_type (MutableSequence[str]):

        """

        analysis_type: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class SBOMStatus(proto.Message):
        r"""The status of an SBOM generation.

        Attributes:
            sbom_state (grafeas.grafeas_v1.types.DiscoveryOccurrence.SBOMStatus.SBOMState):
                The progress of the SBOM generation.
            error (str):
                If there was an error generating an SBOM,
                this will indicate what that error was.
        """

        class SBOMState(proto.Enum):
            r"""An enum indicating the progress of the SBOM generation.

            Values:
                SBOM_STATE_UNSPECIFIED (0):
                    Default unknown state.
                PENDING (1):
                    SBOM scanning is pending.
                COMPLETE (2):
                    SBOM scanning has completed.
            """

            SBOM_STATE_UNSPECIFIED = 0
            PENDING = 1
            COMPLETE = 2

        sbom_state: "DiscoveryOccurrence.SBOMStatus.SBOMState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DiscoveryOccurrence.SBOMStatus.SBOMState",
        )
        error: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class VulnerabilityAttestation(proto.Message):
        r"""The status of an vulnerability attestation generation.

        Attributes:
            last_attempt_time (google.protobuf.timestamp_pb2.Timestamp):
                The last time we attempted to generate an
                attestation.
            state (grafeas.grafeas_v1.types.DiscoveryOccurrence.VulnerabilityAttestation.VulnerabilityAttestationState):
                The success/failure state of the latest
                attestation attempt.
            error (str):
                If failure, the error reason for why the
                attestation generation failed.
        """

        class VulnerabilityAttestationState(proto.Enum):
            r"""An enum indicating the state of the attestation generation.

            Values:
                VULNERABILITY_ATTESTATION_STATE_UNSPECIFIED (0):
                    Default unknown state.
                SUCCESS (1):
                    Attestation was successfully generated and
                    stored.
                FAILURE (2):
                    Attestation was unsuccessfully generated and
                    stored.
            """

            VULNERABILITY_ATTESTATION_STATE_UNSPECIFIED = 0
            SUCCESS = 1
            FAILURE = 2

        last_attempt_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        state: "DiscoveryOccurrence.VulnerabilityAttestation.VulnerabilityAttestationState" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DiscoveryOccurrence.VulnerabilityAttestation.VulnerabilityAttestationState",
        )
        error: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class File(proto.Message):
        r"""

        Attributes:
            name (str):

            digest (MutableMapping[str, str]):

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

    continuous_analysis: ContinuousAnalysis = proto.Field(
        proto.ENUM,
        number=1,
        enum=ContinuousAnalysis,
    )
    analysis_status: AnalysisStatus = proto.Field(
        proto.ENUM,
        number=2,
        enum=AnalysisStatus,
    )
    analysis_completed: AnalysisCompleted = proto.Field(
        proto.MESSAGE,
        number=7,
        message=AnalysisCompleted,
    )
    analysis_error: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )
    analysis_status_error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    cpe: str = proto.Field(
        proto.STRING,
        number=4,
    )
    last_scan_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    archive_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    sbom_status: SBOMStatus = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SBOMStatus,
    )
    vulnerability_attestation: VulnerabilityAttestation = proto.Field(
        proto.MESSAGE,
        number=10,
        message=VulnerabilityAttestation,
    )
    files: MutableSequence[File] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=File,
    )
    last_vulnerability_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
