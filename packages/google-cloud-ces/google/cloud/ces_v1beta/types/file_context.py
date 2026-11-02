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
    package="google.cloud.ces.v1beta",
    manifest={
        "FileContext",
    },
)


class FileContext(proto.Message):
    r"""Files to be used as context. Files can be provided as raw
    bytes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        file_bytes (google.cloud.ces_v1beta.types.FileContext.FileBytes):
            Optional. File provided as raw bytes.

            This field is a member of `oneof`_ ``file``.
    """

    class FileBytes(proto.Message):
        r"""File provided as raw bytes.

        Attributes:
            file_name (str):
                Required. The name of the file provided as
                raw bytes.
            mime_type (str):
                Required. The IANA standard MIME type of the
                source data.
            data (bytes):
                Required. Raw bytes of the file.
        """

        file_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        mime_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        data: bytes = proto.Field(
            proto.BYTES,
            number=3,
        )

    file_bytes: FileBytes = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="file",
        message=FileBytes,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
