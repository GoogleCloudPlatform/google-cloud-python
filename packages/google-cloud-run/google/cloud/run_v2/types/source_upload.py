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

from google.cloud.run_v2.types import k8s_min

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "UploadSourceRequest",
        "UploadSourceResponse",
    },
)


class UploadSourceRequest(proto.Message):
    r"""The request message for the UploadSource method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The project and location in which the source
            archive should be uploaded to, specified in the format
            ``projects/*/locations/*``.
        service (str):
            The name of Cloud Run Service upload source
            archive will be used for.

            This field is a member of `oneof`_ ``target``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="target",
    )


class UploadSourceResponse(proto.Message):
    r"""The response message for the UploadSource method.

    Attributes:
        cloud_storage_source (google.cloud.run_v2.types.SourceCode.CloudStorageSource):
            The Cloud Storage object path the source
            archive is uploaded to.
    """

    cloud_storage_source: k8s_min.SourceCode.CloudStorageSource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=k8s_min.SourceCode.CloudStorageSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
