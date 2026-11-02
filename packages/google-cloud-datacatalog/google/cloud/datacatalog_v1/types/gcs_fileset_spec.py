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

from google.cloud.datacatalog_v1.types import timestamps

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "GcsFilesetSpec",
        "GcsFileSpec",
    },
)


class GcsFilesetSpec(proto.Message):
    r"""Describes a Cloud Storage fileset entry.

    Attributes:
        file_patterns (MutableSequence[str]):
            Required. Patterns to identify a set of files in Google
            Cloud Storage.

            For more information, see [Wildcard Names]
            (https://cloud.google.com/storage/docs/wildcards).

            Note: Currently, bucket wildcards are not supported.

            Examples of valid ``file_patterns``:

            - ``gs://bucket_name/dir/*``: matches all files in
              ``bucket_name/dir`` directory
            - ``gs://bucket_name/dir/**``: matches all files in
              ``bucket_name/dir`` and all subdirectories
            - ``gs://bucket_name/file*``: matches files prefixed by
              ``file`` in ``bucket_name``
            - ``gs://bucket_name/??.txt``: matches files with two
              characters followed by ``.txt`` in ``bucket_name``
            - ``gs://bucket_name/[aeiou].txt``: matches files that
              contain a single vowel character followed by ``.txt`` in
              ``bucket_name``
            - ``gs://bucket_name/[a-m].txt``: matches files that contain
              ``a``, ``b``, ... or ``m`` followed by ``.txt`` in
              ``bucket_name``
            - ``gs://bucket_name/a/*/b``: matches all files in
              ``bucket_name`` that match the ``a/*/b`` pattern, such as
              ``a/c/b``, ``a/d/b``
            - ``gs://another_bucket/a.txt``: matches
              ``gs://another_bucket/a.txt``

            You can combine wildcards to match complex sets of files,
            for example:

            ``gs://bucket_name/[a-m]??.j*g``
        sample_gcs_file_specs (MutableSequence[google.cloud.datacatalog_v1.types.GcsFileSpec]):
            Output only. Sample files contained in this
            fileset, not all files contained in this fileset
            are represented here.
    """

    file_patterns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    sample_gcs_file_specs: MutableSequence["GcsFileSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="GcsFileSpec",
    )


class GcsFileSpec(proto.Message):
    r"""Specification of a single file in Cloud Storage.

    Attributes:
        file_path (str):
            Required. Full file path. Example:
            ``gs://bucket_name/a/b.txt``.
        gcs_timestamps (google.cloud.datacatalog_v1.types.SystemTimestamps):
            Output only. Creation, modification, and
            expiration timestamps of a Cloud Storage file.
        size_bytes (int):
            Output only. File size in bytes.
    """

    file_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_timestamps: timestamps.SystemTimestamps = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamps.SystemTimestamps,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
