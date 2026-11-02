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

from google.cloud.artifactregistry_v1.types import file, version

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1",
    manifest={
        "ExportArtifactRequest",
        "ExportArtifactResponse",
        "ExportArtifactMetadata",
    },
)


class ExportArtifactRequest(proto.Message):
    r"""The request for exporting an artifact to a destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_version (str):
            The artifact version to export.
            Format:

            projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/versions/{version}

            This field is a member of `oneof`_ ``source_artifact``.
        source_tag (str):
            The artifact tag to export.
            Format:projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}

            This field is a member of `oneof`_ ``source_artifact``.
        gcs_path (str):
            The Cloud Storage path to export the artifact to. Should
            start with the bucket name, and optionally have a directory
            path. Examples: ``dst_bucket``, ``dst_bucket/sub_dir``.
            Existing objects with the same path will be overwritten.

            This field is a member of `oneof`_ ``destination``.
        repository (str):
            Required. The repository of the artifact to
            export. Format:
            projects/{project}/locations/{location}/repositories/{repository}
    """

    source_version: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source_artifact",
    )
    source_tag: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source_artifact",
    )
    gcs_path: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="destination",
    )
    repository: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportArtifactResponse(proto.Message):
    r"""The response for exporting an artifact to a destination.

    Attributes:
        exported_version (google.cloud.artifactregistry_v1.types.Version):
            The exported version. Should be the same as
            the request version with fingerprint resource
            name.
    """

    exported_version: version.Version = proto.Field(
        proto.MESSAGE,
        number=1,
        message=version.Version,
    )


class ExportArtifactMetadata(proto.Message):
    r"""The LRO metadata for exporting an artifact.

    Attributes:
        exported_files (MutableSequence[google.cloud.artifactregistry_v1.types.ExportArtifactMetadata.ExportedFile]):
            The exported artifact files.
    """

    class ExportedFile(proto.Message):
        r"""The exported artifact file.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            gcs_object_path (str):
                Cloud Storage Object path of the exported file. Examples:
                ``dst_bucket/file1``, ``dst_bucket/sub_dir/file1``

                This field is a member of `oneof`_ ``destination``.
            name (str):
                Name of the exported artifact file. Format:
                ``projects/p1/locations/us/repositories/repo1/files/file1``
            hashes (MutableSequence[google.cloud.artifactregistry_v1.types.Hash]):
                The hashes of the file content.
        """

        gcs_object_path: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="destination",
        )
        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        hashes: MutableSequence[file.Hash] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=file.Hash,
        )

    exported_files: MutableSequence[ExportedFile] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ExportedFile,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
