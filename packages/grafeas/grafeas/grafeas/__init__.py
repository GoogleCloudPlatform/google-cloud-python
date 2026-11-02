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
from grafeas.grafeas import gapic_version as package_version

__version__ = package_version.__version__


from grafeas.grafeas_v1.services.grafeas.async_client import GrafeasAsyncClient
from grafeas.grafeas_v1.services.grafeas.client import GrafeasClient
from grafeas.grafeas_v1.types.attestation import (
    AttestationNote,
    AttestationOccurrence,
    Jwt,
)
from grafeas.grafeas_v1.types.build import BuildNote, BuildOccurrence
from grafeas.grafeas_v1.types.common import (
    BaseImage,
    Digest,
    Envelope,
    EnvelopeSignature,
    FileLocation,
    LayerDetails,
    License,
    NoteKind,
    RelatedUrl,
    Signature,
)
from grafeas.grafeas_v1.types.compliance import (
    ComplianceNote,
    ComplianceOccurrence,
    ComplianceVersion,
    NonCompliantFile,
)
from grafeas.grafeas_v1.types.cvss import CVSS, CVSSv3, CVSSVersion
from grafeas.grafeas_v1.types.deployment import DeploymentNote, DeploymentOccurrence
from grafeas.grafeas_v1.types.discovery import DiscoveryNote, DiscoveryOccurrence
from grafeas.grafeas_v1.types.dsse_attestation import (
    DSSEAttestationNote,
    DSSEAttestationOccurrence,
)
from grafeas.grafeas_v1.types.grafeas import (
    BatchCreateNotesRequest,
    BatchCreateNotesResponse,
    BatchCreateOccurrencesRequest,
    BatchCreateOccurrencesResponse,
    CreateNoteRequest,
    CreateOccurrenceRequest,
    DeleteNoteRequest,
    DeleteOccurrenceRequest,
    GetNoteRequest,
    GetOccurrenceNoteRequest,
    GetOccurrenceRequest,
    ListNoteOccurrencesRequest,
    ListNoteOccurrencesResponse,
    ListNotesRequest,
    ListNotesResponse,
    ListOccurrencesRequest,
    ListOccurrencesResponse,
    Note,
    Occurrence,
    UpdateNoteRequest,
    UpdateOccurrenceRequest,
)
from grafeas.grafeas_v1.types.image import (
    Fingerprint,
    ImageNote,
    ImageOccurrence,
    Layer,
)
from grafeas.grafeas_v1.types.intoto_provenance import (
    BuilderConfig,
    Completeness,
    InTotoProvenance,
    Metadata,
    Recipe,
)
from grafeas.grafeas_v1.types.intoto_statement import (
    InTotoSlsaProvenanceV1,
    InTotoStatement,
    Subject,
)
from grafeas.grafeas_v1.types.package import (
    Architecture,
    Distribution,
    Location,
    PackageNote,
    PackageOccurrence,
    Version,
)
from grafeas.grafeas_v1.types.provenance import (
    AliasContext,
    Artifact,
    BuildProvenance,
    CloudRepoSourceContext,
    Command,
    FileHashes,
    GerritSourceContext,
    GitSourceContext,
    Hash,
    ProjectRepoId,
    RepoId,
    Source,
    SourceContext,
)
from grafeas.grafeas_v1.types.risk import (
    CISAKnownExploitedVulnerabilities,
    ExploitPredictionScoringSystem,
    Risk,
)
from grafeas.grafeas_v1.types.sbom import (
    SbomReferenceIntotoPayload,
    SbomReferenceIntotoPredicate,
    SBOMReferenceNote,
    SBOMReferenceOccurrence,
)
from grafeas.grafeas_v1.types.secret import (
    SecretKind,
    SecretLocation,
    SecretNote,
    SecretOccurrence,
    SecretStatus,
)
from grafeas.grafeas_v1.types.severity import Severity
from grafeas.grafeas_v1.types.slsa_provenance import SlsaProvenance
from grafeas.grafeas_v1.types.slsa_provenance_zero_two import SlsaProvenanceZeroTwo
from grafeas.grafeas_v1.types.upgrade import (
    UpgradeDistribution,
    UpgradeNote,
    UpgradeOccurrence,
    WindowsUpdate,
)
from grafeas.grafeas_v1.types.vex import VulnerabilityAssessmentNote
from grafeas.grafeas_v1.types.vulnerability import (
    VulnerabilityNote,
    VulnerabilityOccurrence,
)

__all__ = (
    "GrafeasClient",
    "GrafeasAsyncClient",
    "AttestationNote",
    "AttestationOccurrence",
    "Jwt",
    "BuildNote",
    "BuildOccurrence",
    "BaseImage",
    "Digest",
    "Envelope",
    "EnvelopeSignature",
    "FileLocation",
    "LayerDetails",
    "License",
    "RelatedUrl",
    "Signature",
    "NoteKind",
    "ComplianceNote",
    "ComplianceOccurrence",
    "ComplianceVersion",
    "NonCompliantFile",
    "CVSS",
    "CVSSv3",
    "CVSSVersion",
    "DeploymentNote",
    "DeploymentOccurrence",
    "DiscoveryNote",
    "DiscoveryOccurrence",
    "DSSEAttestationNote",
    "DSSEAttestationOccurrence",
    "BatchCreateNotesRequest",
    "BatchCreateNotesResponse",
    "BatchCreateOccurrencesRequest",
    "BatchCreateOccurrencesResponse",
    "CreateNoteRequest",
    "CreateOccurrenceRequest",
    "DeleteNoteRequest",
    "DeleteOccurrenceRequest",
    "GetNoteRequest",
    "GetOccurrenceNoteRequest",
    "GetOccurrenceRequest",
    "ListNoteOccurrencesRequest",
    "ListNoteOccurrencesResponse",
    "ListNotesRequest",
    "ListNotesResponse",
    "ListOccurrencesRequest",
    "ListOccurrencesResponse",
    "Note",
    "Occurrence",
    "UpdateNoteRequest",
    "UpdateOccurrenceRequest",
    "Fingerprint",
    "ImageNote",
    "ImageOccurrence",
    "Layer",
    "BuilderConfig",
    "Completeness",
    "InTotoProvenance",
    "Metadata",
    "Recipe",
    "InTotoSlsaProvenanceV1",
    "InTotoStatement",
    "Subject",
    "Distribution",
    "Location",
    "PackageNote",
    "PackageOccurrence",
    "Version",
    "Architecture",
    "AliasContext",
    "Artifact",
    "BuildProvenance",
    "CloudRepoSourceContext",
    "Command",
    "FileHashes",
    "GerritSourceContext",
    "GitSourceContext",
    "Hash",
    "ProjectRepoId",
    "RepoId",
    "Source",
    "SourceContext",
    "CISAKnownExploitedVulnerabilities",
    "ExploitPredictionScoringSystem",
    "Risk",
    "SbomReferenceIntotoPayload",
    "SbomReferenceIntotoPredicate",
    "SBOMReferenceNote",
    "SBOMReferenceOccurrence",
    "SecretLocation",
    "SecretNote",
    "SecretOccurrence",
    "SecretStatus",
    "SecretKind",
    "Severity",
    "SlsaProvenance",
    "SlsaProvenanceZeroTwo",
    "UpgradeDistribution",
    "UpgradeNote",
    "UpgradeOccurrence",
    "WindowsUpdate",
    "VulnerabilityAssessmentNote",
    "VulnerabilityNote",
    "VulnerabilityOccurrence",
)
