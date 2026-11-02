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

from google.cloud.security.publicca_v1beta1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.security.publicca.v1beta1",
    manifest={
        "CreateExternalAccountKeyRequest",
    },
)


class CreateExternalAccountKeyRequest(proto.Message):
    r"""Creates a new
    [ExternalAccountKey][google.cloud.security.publicca.v1beta1.ExternalAccountKey]
    in a given project.

    Attributes:
        parent (str):
            Required. The parent resource where this
            external_account_key will be created. Format:
            projects/[project_id]/locations/[location]. At present only
            the "global" location is supported.
        external_account_key (google.cloud.security.publicca_v1beta1.types.ExternalAccountKey):
            Required. The external account key to create.
            This field only exists to future-proof the API.
            At present, all fields in ExternalAccountKey are
            output only and all values are ignored. For the
            purpose of the CreateExternalAccountKeyRequest,
            set it to a default/empty value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    external_account_key: resources.ExternalAccountKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.ExternalAccountKey,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
