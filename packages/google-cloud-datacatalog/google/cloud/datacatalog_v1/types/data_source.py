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

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "DataSource",
        "StorageProperties",
    },
)


class DataSource(proto.Message):
    r"""Physical location of an entry.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        service (google.cloud.datacatalog_v1.types.DataSource.Service):
            Service that physically stores the data.
        resource (str):
            Full name of a resource as defined by the service. For
            example:

            ``//bigquery.googleapis.com/projects/{PROJECT_ID}/locations/{LOCATION}/datasets/{DATASET_ID}/tables/{TABLE_ID}``
        source_entry (str):
            Output only. Data Catalog entry name, if
            applicable.
        storage_properties (google.cloud.datacatalog_v1.types.StorageProperties):
            Detailed properties of the underlying
            storage.

            This field is a member of `oneof`_ ``properties``.
    """

    class Service(proto.Enum):
        r"""Name of a service that stores the data.

        Values:
            SERVICE_UNSPECIFIED (0):
                Default unknown service.
            CLOUD_STORAGE (1):
                Google Cloud Storage service.
            BIGQUERY (2):
                BigQuery service.
        """

        SERVICE_UNSPECIFIED = 0
        CLOUD_STORAGE = 1
        BIGQUERY = 2

    service: Service = proto.Field(
        proto.ENUM,
        number=1,
        enum=Service,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_entry: str = proto.Field(
        proto.STRING,
        number=3,
    )
    storage_properties: "StorageProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="properties",
        message="StorageProperties",
    )


class StorageProperties(proto.Message):
    r"""Details the properties of the underlying storage.

    Attributes:
        file_pattern (MutableSequence[str]):
            Patterns to identify a set of files for this fileset.

            Examples of a valid ``file_pattern``:

            - ``gs://bucket_name/dir/*``: matches all files in the
              ``bucket_name/dir`` directory
            - ``gs://bucket_name/dir/**``: matches all files in the
              ``bucket_name/dir`` and all subdirectories recursively
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
        file_type (str):
            File type in MIME format, for example, ``text/plain``.
    """

    file_pattern: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    file_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
