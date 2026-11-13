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
import google.api_core as api_core

from grafeas.grafeas_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "grafeas.grafeas_v1.services.grafeas",
    "grafeas.grafeas_v1.types.attestation",
    "grafeas.grafeas_v1.types.build",
    "grafeas.grafeas_v1.types.common",
    "grafeas.grafeas_v1.types.compliance",
    "grafeas.grafeas_v1.types.cvss",
    "grafeas.grafeas_v1.types.deployment",
    "grafeas.grafeas_v1.types.discovery",
    "grafeas.grafeas_v1.types.dsse_attestation",
    "grafeas.grafeas_v1.types.grafeas",
    "grafeas.grafeas_v1.types.image",
    "grafeas.grafeas_v1.types.intoto_provenance",
    "grafeas.grafeas_v1.types.intoto_statement",
    "grafeas.grafeas_v1.types.package",
    "grafeas.grafeas_v1.types.provenance",
    "grafeas.grafeas_v1.types.risk",
    "grafeas.grafeas_v1.types.sbom",
    "grafeas.grafeas_v1.types.secret",
    "grafeas.grafeas_v1.types.severity",
    "grafeas.grafeas_v1.types.slsa_provenance",
    "grafeas.grafeas_v1.types.slsa_provenance_zero_two",
    "grafeas.grafeas_v1.types.upgrade",
    "grafeas.grafeas_v1.types.vex",
    "grafeas.grafeas_v1.types.vulnerability",
}


from .services.grafeas import GrafeasAsyncClient, GrafeasClient
from .types.attestation import AttestationNote, AttestationOccurrence, Jwt
from .types.build import BuildNote, BuildOccurrence
from .types.common import (
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
from .types.compliance import (
    ComplianceNote,
    ComplianceOccurrence,
    ComplianceVersion,
    NonCompliantFile,
)
from .types.cvss import CVSS, CVSSv3, CVSSVersion
from .types.deployment import DeploymentNote, DeploymentOccurrence
from .types.discovery import DiscoveryNote, DiscoveryOccurrence
from .types.dsse_attestation import DSSEAttestationNote, DSSEAttestationOccurrence
from .types.grafeas import (
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
from .types.image import Fingerprint, ImageNote, ImageOccurrence, Layer
from .types.intoto_provenance import (
    BuilderConfig,
    Completeness,
    InTotoProvenance,
    Metadata,
    Recipe,
)
from .types.intoto_statement import InTotoSlsaProvenanceV1, InTotoStatement, Subject
from .types.package import (
    Architecture,
    Distribution,
    Location,
    PackageNote,
    PackageOccurrence,
    Version,
)
from .types.provenance import (
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
from .types.risk import (
    CISAKnownExploitedVulnerabilities,
    ExploitPredictionScoringSystem,
    Risk,
)
from .types.sbom import (
    SbomReferenceIntotoPayload,
    SbomReferenceIntotoPredicate,
    SBOMReferenceNote,
    SBOMReferenceOccurrence,
)
from .types.secret import (
    SecretKind,
    SecretLocation,
    SecretNote,
    SecretOccurrence,
    SecretStatus,
)
from .types.severity import Severity
from .types.slsa_provenance import SlsaProvenance
from .types.slsa_provenance_zero_two import SlsaProvenanceZeroTwo
from .types.upgrade import (
    UpgradeDistribution,
    UpgradeNote,
    UpgradeOccurrence,
    WindowsUpdate,
)
from .types.vex import VulnerabilityAssessmentNote
from .types.vulnerability import VulnerabilityNote, VulnerabilityOccurrence

__all__ = (
    "GrafeasAsyncClient",
    "AliasContext",
    "Architecture",
    "Artifact",
    "AttestationNote",
    "AttestationOccurrence",
    "BaseImage",
    "BatchCreateNotesRequest",
    "BatchCreateNotesResponse",
    "BatchCreateOccurrencesRequest",
    "BatchCreateOccurrencesResponse",
    "BuildNote",
    "BuildOccurrence",
    "BuildProvenance",
    "BuilderConfig",
    "CISAKnownExploitedVulnerabilities",
    "CVSS",
    "CVSSVersion",
    "CVSSv3",
    "CloudRepoSourceContext",
    "Command",
    "Completeness",
    "ComplianceNote",
    "ComplianceOccurrence",
    "ComplianceVersion",
    "CreateNoteRequest",
    "CreateOccurrenceRequest",
    "DSSEAttestationNote",
    "DSSEAttestationOccurrence",
    "DeleteNoteRequest",
    "DeleteOccurrenceRequest",
    "DeploymentNote",
    "DeploymentOccurrence",
    "Digest",
    "DiscoveryNote",
    "DiscoveryOccurrence",
    "Distribution",
    "Envelope",
    "EnvelopeSignature",
    "ExploitPredictionScoringSystem",
    "FileHashes",
    "FileLocation",
    "Fingerprint",
    "GerritSourceContext",
    "GetNoteRequest",
    "GetOccurrenceNoteRequest",
    "GetOccurrenceRequest",
    "GitSourceContext",
    "GrafeasClient",
    "Hash",
    "ImageNote",
    "ImageOccurrence",
    "InTotoProvenance",
    "InTotoSlsaProvenanceV1",
    "InTotoStatement",
    "Jwt",
    "Layer",
    "LayerDetails",
    "License",
    "ListNoteOccurrencesRequest",
    "ListNoteOccurrencesResponse",
    "ListNotesRequest",
    "ListNotesResponse",
    "ListOccurrencesRequest",
    "ListOccurrencesResponse",
    "Location",
    "Metadata",
    "NonCompliantFile",
    "Note",
    "NoteKind",
    "Occurrence",
    "PackageNote",
    "PackageOccurrence",
    "ProjectRepoId",
    "Recipe",
    "RelatedUrl",
    "RepoId",
    "Risk",
    "SBOMReferenceNote",
    "SBOMReferenceOccurrence",
    "SbomReferenceIntotoPayload",
    "SbomReferenceIntotoPredicate",
    "SecretKind",
    "SecretLocation",
    "SecretNote",
    "SecretOccurrence",
    "SecretStatus",
    "Severity",
    "Signature",
    "SlsaProvenance",
    "SlsaProvenanceZeroTwo",
    "Source",
    "SourceContext",
    "Subject",
    "UpdateNoteRequest",
    "UpdateOccurrenceRequest",
    "UpgradeDistribution",
    "UpgradeNote",
    "UpgradeOccurrence",
    "Version",
    "VulnerabilityAssessmentNote",
    "VulnerabilityNote",
    "VulnerabilityOccurrence",
    "WindowsUpdate",
)

api_core.check_python_version("grafeas.grafeas_v1")
api_core.check_dependency_versions("grafeas.grafeas_v1")
