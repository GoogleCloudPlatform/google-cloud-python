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
    package="google.maps.mapsplatformdatasets.v1",
    manifest={
        "FileFormat",
        "LocalFileSource",
        "GcsSource",
    },
)


class FileFormat(proto.Enum):
    r"""The format of the file being uploaded.

    Values:
        FILE_FORMAT_UNSPECIFIED (0):
            Unspecified file format.
        FILE_FORMAT_GEOJSON (1):
            GeoJson file.
        FILE_FORMAT_KML (2):
            KML file.
        FILE_FORMAT_CSV (3):
            CSV file.
    """

    FILE_FORMAT_UNSPECIFIED = 0
    FILE_FORMAT_GEOJSON = 1
    FILE_FORMAT_KML = 2
    FILE_FORMAT_CSV = 3


class LocalFileSource(proto.Message):
    r"""The details about the data source when it is a local file.

    Attributes:
        filename (str):
            The file name of the uploaded file.
        file_format (google.maps.mapsplatformdatasets_v1.types.FileFormat):
            The format of the file that is being
            uploaded.
    """

    filename: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_format: "FileFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="FileFormat",
    )


class GcsSource(proto.Message):
    r"""The details about the data source when it is in Google Cloud
    Storage.

    Attributes:
        input_uri (str):
            Source data URI. For example, ``gs://my_bucket/my_object``.
        file_format (google.maps.mapsplatformdatasets_v1.types.FileFormat):
            The file format of the Google Cloud Storage
            object. This is used mainly for validation.
    """

    input_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_format: "FileFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="FileFormat",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
