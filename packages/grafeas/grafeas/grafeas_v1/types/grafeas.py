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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from grafeas.grafeas_v1.types import attestation as g_attestation
from grafeas.grafeas_v1.types import build as g_build
from grafeas.grafeas_v1.types import common, sbom, vex
from grafeas.grafeas_v1.types import compliance as g_compliance
from grafeas.grafeas_v1.types import deployment as g_deployment
from grafeas.grafeas_v1.types import discovery as g_discovery
from grafeas.grafeas_v1.types import dsse_attestation as g_dsse_attestation
from grafeas.grafeas_v1.types import image as g_image
from grafeas.grafeas_v1.types import package as g_package
from grafeas.grafeas_v1.types import secret as g_secret
from grafeas.grafeas_v1.types import upgrade as g_upgrade
from grafeas.grafeas_v1.types import vulnerability as g_vulnerability

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "Occurrence",
        "Note",
        "GetOccurrenceRequest",
        "ListOccurrencesRequest",
        "ListOccurrencesResponse",
        "DeleteOccurrenceRequest",
        "CreateOccurrenceRequest",
        "UpdateOccurrenceRequest",
        "GetNoteRequest",
        "GetOccurrenceNoteRequest",
        "ListNotesRequest",
        "ListNotesResponse",
        "DeleteNoteRequest",
        "CreateNoteRequest",
        "UpdateNoteRequest",
        "ListNoteOccurrencesRequest",
        "ListNoteOccurrencesResponse",
        "BatchCreateNotesRequest",
        "BatchCreateNotesResponse",
        "BatchCreateOccurrencesRequest",
        "BatchCreateOccurrencesResponse",
    },
)


class Occurrence(proto.Message):
    r"""An instance of an analysis type that has been found on a
    resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the occurrence in the form of
            ``projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]``.
        resource_uri (str):
            Required. Immutable. A URI that represents the resource for
            which the occurrence applies. For example,
            ``https://gcr.io/project/image@sha256:123abc`` for a Docker
            image.
        note_name (str):
            Required. Immutable. The analysis note associated with this
            occurrence, in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``. This field can
            be used as a filter in list requests.
        kind (grafeas.grafeas_v1.types.NoteKind):
            Output only. This explicitly denotes which of
            the occurrence details are specified. This field
            can be used as a filter in list requests.
        remediation (str):
            A description of actions that can be taken to
            remedy the note.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this occurrence was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this occurrence was
            last updated.
        vulnerability (grafeas.grafeas_v1.types.VulnerabilityOccurrence):
            Describes a security vulnerability.

            This field is a member of `oneof`_ ``details``.
        build (grafeas.grafeas_v1.types.BuildOccurrence):
            Describes a verifiable build.

            This field is a member of `oneof`_ ``details``.
        image (grafeas.grafeas_v1.types.ImageOccurrence):
            Describes how this resource derives from the
            basis in the associated note.

            This field is a member of `oneof`_ ``details``.
        package (grafeas.grafeas_v1.types.PackageOccurrence):
            Describes the installation of a package on
            the linked resource.

            This field is a member of `oneof`_ ``details``.
        deployment (grafeas.grafeas_v1.types.DeploymentOccurrence):
            Describes the deployment of an artifact on a
            runtime.

            This field is a member of `oneof`_ ``details``.
        discovery (grafeas.grafeas_v1.types.DiscoveryOccurrence):
            Describes when a resource was discovered.

            This field is a member of `oneof`_ ``details``.
        attestation (grafeas.grafeas_v1.types.AttestationOccurrence):
            Describes an attestation of an artifact.

            This field is a member of `oneof`_ ``details``.
        upgrade (grafeas.grafeas_v1.types.UpgradeOccurrence):
            Describes an available package upgrade on the
            linked resource.

            This field is a member of `oneof`_ ``details``.
        compliance (grafeas.grafeas_v1.types.ComplianceOccurrence):
            Describes a compliance violation on a linked
            resource.

            This field is a member of `oneof`_ ``details``.
        dsse_attestation (grafeas.grafeas_v1.types.DSSEAttestationOccurrence):
            Describes an attestation of an artifact using
            dsse.

            This field is a member of `oneof`_ ``details``.
        sbom_reference (grafeas.grafeas_v1.types.SBOMReferenceOccurrence):
            Describes a specific SBOM reference
            occurrences.

            This field is a member of `oneof`_ ``details``.
        secret (grafeas.grafeas_v1.types.SecretOccurrence):
            Describes a secret.

            This field is a member of `oneof`_ ``details``.
        envelope (grafeas.grafeas_v1.types.Envelope):
            https://github.com/secure-systems-lab/dsse
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    note_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kind: common.NoteKind = proto.Field(
        proto.ENUM,
        number=4,
        enum=common.NoteKind,
    )
    remediation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    vulnerability: g_vulnerability.VulnerabilityOccurrence = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="details",
        message=g_vulnerability.VulnerabilityOccurrence,
    )
    build: g_build.BuildOccurrence = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="details",
        message=g_build.BuildOccurrence,
    )
    image: g_image.ImageOccurrence = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="details",
        message=g_image.ImageOccurrence,
    )
    package: g_package.PackageOccurrence = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="details",
        message=g_package.PackageOccurrence,
    )
    deployment: g_deployment.DeploymentOccurrence = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="details",
        message=g_deployment.DeploymentOccurrence,
    )
    discovery: g_discovery.DiscoveryOccurrence = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="details",
        message=g_discovery.DiscoveryOccurrence,
    )
    attestation: g_attestation.AttestationOccurrence = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="details",
        message=g_attestation.AttestationOccurrence,
    )
    upgrade: g_upgrade.UpgradeOccurrence = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="details",
        message=g_upgrade.UpgradeOccurrence,
    )
    compliance: g_compliance.ComplianceOccurrence = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="details",
        message=g_compliance.ComplianceOccurrence,
    )
    dsse_attestation: g_dsse_attestation.DSSEAttestationOccurrence = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="details",
        message=g_dsse_attestation.DSSEAttestationOccurrence,
    )
    sbom_reference: sbom.SBOMReferenceOccurrence = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="details",
        message=sbom.SBOMReferenceOccurrence,
    )
    secret: g_secret.SecretOccurrence = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="details",
        message=g_secret.SecretOccurrence,
    )
    envelope: common.Envelope = proto.Field(
        proto.MESSAGE,
        number=18,
        message=common.Envelope,
    )


class Note(proto.Message):
    r"""A type of analysis that can be done for a resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the note in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``.
        short_description (str):
            A one sentence description of this note.
        long_description (str):
            A detailed description of this note.
        kind (grafeas.grafeas_v1.types.NoteKind):
            Output only. The type of analysis. This field
            can be used as a filter in list requests.
        related_url (MutableSequence[grafeas.grafeas_v1.types.RelatedUrl]):
            URLs associated with this note.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Time of expiration for this note. Empty if
            note does not expire.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this note was created.
            This field can be used as a filter in list
            requests.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this note was last
            updated. This field can be used as a filter in
            list requests.
        related_note_names (MutableSequence[str]):
            Other notes related to this note.
        vulnerability (grafeas.grafeas_v1.types.VulnerabilityNote):
            A note describing a package vulnerability.

            This field is a member of `oneof`_ ``type``.
        build (grafeas.grafeas_v1.types.BuildNote):
            A note describing build provenance for a
            verifiable build.

            This field is a member of `oneof`_ ``type``.
        image (grafeas.grafeas_v1.types.ImageNote):
            A note describing a base image.

            This field is a member of `oneof`_ ``type``.
        package (grafeas.grafeas_v1.types.PackageNote):
            A note describing a package hosted by various
            package managers.

            This field is a member of `oneof`_ ``type``.
        deployment (grafeas.grafeas_v1.types.DeploymentNote):
            A note describing something that can be
            deployed.

            This field is a member of `oneof`_ ``type``.
        discovery (grafeas.grafeas_v1.types.DiscoveryNote):
            A note describing the initial analysis of a
            resource.

            This field is a member of `oneof`_ ``type``.
        attestation (grafeas.grafeas_v1.types.AttestationNote):
            A note describing an attestation role.

            This field is a member of `oneof`_ ``type``.
        upgrade (grafeas.grafeas_v1.types.UpgradeNote):
            A note describing available package upgrades.

            This field is a member of `oneof`_ ``type``.
        compliance (grafeas.grafeas_v1.types.ComplianceNote):
            A note describing a compliance check.

            This field is a member of `oneof`_ ``type``.
        dsse_attestation (grafeas.grafeas_v1.types.DSSEAttestationNote):
            A note describing a dsse attestation note.

            This field is a member of `oneof`_ ``type``.
        vulnerability_assessment (grafeas.grafeas_v1.types.VulnerabilityAssessmentNote):
            A note describing a vulnerability assessment.

            This field is a member of `oneof`_ ``type``.
        sbom_reference (grafeas.grafeas_v1.types.SBOMReferenceNote):
            A note describing an SBOM reference.

            This field is a member of `oneof`_ ``type``.
        secret (grafeas.grafeas_v1.types.SecretNote):
            A note describing a secret.

            This field is a member of `oneof`_ ``type``.
    """

    name: str = proto.Field(
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
    kind: common.NoteKind = proto.Field(
        proto.ENUM,
        number=4,
        enum=common.NoteKind,
    )
    related_url: MutableSequence[common.RelatedUrl] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=common.RelatedUrl,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    related_note_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    vulnerability: g_vulnerability.VulnerabilityNote = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="type",
        message=g_vulnerability.VulnerabilityNote,
    )
    build: g_build.BuildNote = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="type",
        message=g_build.BuildNote,
    )
    image: g_image.ImageNote = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="type",
        message=g_image.ImageNote,
    )
    package: g_package.PackageNote = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="type",
        message=g_package.PackageNote,
    )
    deployment: g_deployment.DeploymentNote = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="type",
        message=g_deployment.DeploymentNote,
    )
    discovery: g_discovery.DiscoveryNote = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="type",
        message=g_discovery.DiscoveryNote,
    )
    attestation: g_attestation.AttestationNote = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="type",
        message=g_attestation.AttestationNote,
    )
    upgrade: g_upgrade.UpgradeNote = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="type",
        message=g_upgrade.UpgradeNote,
    )
    compliance: g_compliance.ComplianceNote = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="type",
        message=g_compliance.ComplianceNote,
    )
    dsse_attestation: g_dsse_attestation.DSSEAttestationNote = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="type",
        message=g_dsse_attestation.DSSEAttestationNote,
    )
    vulnerability_assessment: vex.VulnerabilityAssessmentNote = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="type",
        message=vex.VulnerabilityAssessmentNote,
    )
    sbom_reference: sbom.SBOMReferenceNote = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="type",
        message=sbom.SBOMReferenceNote,
    )
    secret: g_secret.SecretNote = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="type",
        message=g_secret.SecretNote,
    )


class GetOccurrenceRequest(proto.Message):
    r"""Request to get an occurrence.

    Attributes:
        name (str):
            The name of the occurrence in the form of
            ``projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOccurrencesRequest(proto.Message):
    r"""Request to list occurrences.

    Attributes:
        parent (str):
            The name of the project to list occurrences for in the form
            of ``projects/[PROJECT_ID]``.
        filter (str):
            The filter expression.
        page_size (int):
            Number of occurrences to return in the list.
            Must be positive. Max allowed page size is 1000.
            If not specified, page size defaults to 20.
        page_token (str):
            Token to provide to skip to a particular spot
            in the list.
        return_partial_success (bool):
            If set, the request will return all reachable Occurrences
            and report all unreachable regions in the ``unreachable``
            field in the response.

            Only applicable for requests in the global region.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListOccurrencesResponse(proto.Message):
    r"""Response for listing occurrences.

    Attributes:
        occurrences (MutableSequence[grafeas.grafeas_v1.types.Occurrence]):
            The occurrences requested.
        next_page_token (str):
            The next pagination token in the list response. It should be
            used as ``page_token`` for the following request. An empty
            value means no more results.
        unreachable (MutableSequence[str]):
            Unreachable regions. Populated for requests from the global
            region when ``return_partial_success`` is set.

            Format: ``projects/[PROJECT_ID]/locations/[LOCATION]``
    """

    @property
    def raw_page(self):
        return self

    occurrences: MutableSequence["Occurrence"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Occurrence",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteOccurrenceRequest(proto.Message):
    r"""Request to delete an occurrence.

    Attributes:
        name (str):
            The name of the occurrence in the form of
            ``projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOccurrenceRequest(proto.Message):
    r"""Request to create a new occurrence.

    Attributes:
        parent (str):
            The name of the project in the form of
            ``projects/[PROJECT_ID]``, under which the occurrence is to
            be created.
        occurrence (grafeas.grafeas_v1.types.Occurrence):
            The occurrence to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    occurrence: "Occurrence" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Occurrence",
    )


class UpdateOccurrenceRequest(proto.Message):
    r"""Request to update an occurrence.

    Attributes:
        name (str):
            The name of the occurrence in the form of
            ``projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]``.
        occurrence (grafeas.grafeas_v1.types.Occurrence):
            The updated occurrence.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to update.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    occurrence: "Occurrence" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Occurrence",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetNoteRequest(proto.Message):
    r"""Request to get a note.

    Attributes:
        name (str):
            The name of the note in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetOccurrenceNoteRequest(proto.Message):
    r"""Request to get the note to which the specified occurrence is
    attached.

    Attributes:
        name (str):
            The name of the occurrence in the form of
            ``projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNotesRequest(proto.Message):
    r"""Request to list notes.

    Attributes:
        parent (str):
            The name of the project to list notes for in the form of
            ``projects/[PROJECT_ID]``.
        filter (str):
            The filter expression.
        page_size (int):
            Number of notes to return in the list. Must
            be positive. Max allowed page size is 1000. If
            not specified, page size defaults to 20.
        page_token (str):
            Token to provide to skip to a particular spot
            in the list.
        return_partial_success (bool):
            If set, the request will return all reachable Notes and
            report all unreachable regions in the ``unreachable`` field
            in the response.

            Only applicable for requests in the global region.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListNotesResponse(proto.Message):
    r"""Response for listing notes.

    Attributes:
        notes (MutableSequence[grafeas.grafeas_v1.types.Note]):
            The notes requested.
        next_page_token (str):
            The next pagination token in the list response. It should be
            used as ``page_token`` for the following request. An empty
            value means no more results.
        unreachable (MutableSequence[str]):
            Unreachable regions. Populated for requests from the global
            region when ``return_partial_success`` is set.

            Format: ``projects/[PROJECT_ID]/locations/[LOCATION]``
    """

    @property
    def raw_page(self):
        return self

    notes: MutableSequence["Note"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Note",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteNoteRequest(proto.Message):
    r"""Request to delete a note.

    Attributes:
        name (str):
            The name of the note in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateNoteRequest(proto.Message):
    r"""Request to create a new note.

    Attributes:
        parent (str):
            The name of the project in the form of
            ``projects/[PROJECT_ID]``, under which the note is to be
            created.
        note_id (str):
            The ID to use for this note.
        note (grafeas.grafeas_v1.types.Note):
            The note to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    note_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    note: "Note" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Note",
    )


class UpdateNoteRequest(proto.Message):
    r"""Request to update a note.

    Attributes:
        name (str):
            The name of the note in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``.
        note (grafeas.grafeas_v1.types.Note):
            The updated note.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to update.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    note: "Note" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Note",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class ListNoteOccurrencesRequest(proto.Message):
    r"""Request to list occurrences for a note.

    Attributes:
        name (str):
            The name of the note to list occurrences for in the form of
            ``projects/[PROVIDER_ID]/notes/[NOTE_ID]``.
        filter (str):
            The filter expression.
        page_size (int):
            Number of occurrences to return in the list.
        page_token (str):
            Token to provide to skip to a particular spot
            in the list.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListNoteOccurrencesResponse(proto.Message):
    r"""Response for listing occurrences for a note.

    Attributes:
        occurrences (MutableSequence[grafeas.grafeas_v1.types.Occurrence]):
            The occurrences attached to the specified
            note.
        next_page_token (str):
            Token to provide to skip to a particular spot
            in the list.
    """

    @property
    def raw_page(self):
        return self

    occurrences: MutableSequence["Occurrence"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Occurrence",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchCreateNotesRequest(proto.Message):
    r"""Request to create notes in batch.

    Attributes:
        parent (str):
            The name of the project in the form of
            ``projects/[PROJECT_ID]``, under which the notes are to be
            created.
        notes (MutableMapping[str, grafeas.grafeas_v1.types.Note]):
            The notes to create. Max allowed length is
            1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    notes: MutableMapping[str, "Note"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="Note",
    )


class BatchCreateNotesResponse(proto.Message):
    r"""Response for creating notes in batch.

    Attributes:
        notes (MutableSequence[grafeas.grafeas_v1.types.Note]):
            The notes that were created.
    """

    notes: MutableSequence["Note"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Note",
    )


class BatchCreateOccurrencesRequest(proto.Message):
    r"""Request to create occurrences in batch.

    Attributes:
        parent (str):
            The name of the project in the form of
            ``projects/[PROJECT_ID]``, under which the occurrences are
            to be created.
        occurrences (MutableSequence[grafeas.grafeas_v1.types.Occurrence]):
            The occurrences to create. Max allowed length
            is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    occurrences: MutableSequence["Occurrence"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Occurrence",
    )


class BatchCreateOccurrencesResponse(proto.Message):
    r"""Response for creating occurrences in batch.

    Attributes:
        occurrences (MutableSequence[grafeas.grafeas_v1.types.Occurrence]):
            The occurrences that were created.
    """

    occurrences: MutableSequence["Occurrence"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Occurrence",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
